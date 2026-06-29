(function () {
    if (!window.location.pathname.startsWith('/admin/')) {
        return;
    }

    function appendLink(rel, href) {
        if (document.querySelector('link[rel="' + rel + '"][href="' + href + '"]')) {
            return;
        }

        const link = document.createElement('link');
        link.rel = rel;
        link.href = href;
        document.head.appendChild(link);
    }

    appendLink('manifest', '/admin-manifest.json');
    appendLink('apple-touch-icon', '/admin-apple-touch-icon.png');
})();
