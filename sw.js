const CACHE_NAME = 'eviatar-app-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/manifest.json'
];

// התקנת ה-Service Worker ושמירת הקבצים
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS_TO_CACHE))
  );
});

// שליפת מידע מהמטמון כשאפשר
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
