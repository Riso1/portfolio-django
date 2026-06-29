{% load static %}
const CACHE_NAME = '{{ cache_version }}';
const OFFLINE_URL = '{% url "offline_page" %}';
const PRECACHE_URLS = [
    '{% url "home" %}',
    OFFLINE_URL,
    '{% static "portfolio/css/style.css" %}',
    '{{ pwa_icon_url }}',
    '{% static "portfolio/icons/icon-192.png" %}',
    '{% static "portfolio/icons/icon-512.png" %}',
    '{% static "portfolio/icons/maskable-512.png" %}'
];

self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                return cache.addAll(PRECACHE_URLS);
            })
            .then(function () {
                return self.skipWaiting();
            })
    );
});

self.addEventListener('activate', function (event) {
    event.waitUntil(
        caches.keys()
            .then(function (cacheNames) {
                return Promise.all(
                    cacheNames
                        .filter(function (cacheName) {
                            return cacheName !== CACHE_NAME;
                        })
                        .map(function (cacheName) {
                            return caches.delete(cacheName);
                        })
                );
            })
            .then(function () {
                return self.clients.claim();
            })
    );
});

self.addEventListener('fetch', function (event) {
    const request = event.request;

    if (request.method !== 'GET') {
        return;
    }

    if (request.mode === 'navigate') {
        event.respondWith(
            fetch(request)
                .then(function (response) {
                    const responseCopy = response.clone();

                    caches.open(CACHE_NAME).then(function (cache) {
                        cache.put(request, responseCopy);
                    });

                    return response;
                })
                .catch(function () {
                    return caches.match(request)
                        .then(function (cachedResponse) {
                            return cachedResponse || caches.match(OFFLINE_URL);
                        });
                })
        );
        return;
    }

    event.respondWith(
        caches.match(request)
            .then(function (cachedResponse) {
                if (cachedResponse) {
                    return cachedResponse;
                }

                return fetch(request).then(function (response) {
                    if (!response || response.status !== 200 || response.type !== 'basic') {
                        return response;
                    }

                    const responseCopy = response.clone();

                    caches.open(CACHE_NAME).then(function (cache) {
                        cache.put(request, responseCopy);
                    });

                    return response;
                });
            })
    );
});
