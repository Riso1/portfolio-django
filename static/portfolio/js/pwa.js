(function () {
    if (!('serviceWorker' in navigator)) {
        return;
    }

    const isLocalhost = ['localhost', '127.0.0.1'].includes(window.location.hostname);
    const isSecure = window.location.protocol === 'https:';

    if (!isSecure && !isLocalhost) {
        return;
    }

    window.addEventListener('load', function () {
        navigator.serviceWorker.register('/service-worker.js', { scope: '/' }).catch(function () {
            return null;
        });
    });
})();
