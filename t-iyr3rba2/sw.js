/* 앱 설치용 최소 서비스워커: 항상 새 버전을 먼저 받고, 인터넷이 끊기면 마지막 화면을 보여 준다 */
self.addEventListener('install', function (e) { self.skipWaiting(); });
self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });
self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(fetch(e.request).then(function (r) { var c = r.clone(); caches.open('daily-v1').then(function (k) { k.put(e.request, c); }); return r; })
    .catch(function () { return caches.match(e.request); }));
});
