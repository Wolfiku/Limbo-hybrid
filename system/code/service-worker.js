// service-worker.js

const cacheName = 'limbo-hybrid-cache-v1';

// Installiere den Service Worker und cache nur die index.html
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(cacheName).then((cache) => {
      return cache.addAll([
        '/index.html',  // Hier wird nur index.html gecacht
      ]);
    })
  );
});

// Aktiviere den Service Worker
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((thisCache) => {
          if (thisCache !== cacheName) {
            return caches.delete(thisCache);
          }
        })
      );
    })
  );
});

// Hole die gecachte index.html oder fetch sie aus dem Netzwerk
self.addEventListener('fetch', (event) => {
  if (event.request.url.endsWith('index.html')) {
    event.respondWith(
      caches.match(event.request).then((cachedResponse) => {
        if (cachedResponse) {
          return cachedResponse; // Benutze die gecachte index.html
        }
        return fetch(event.request); // Hole die index.html aus dem Netzwerk, falls sie nicht im Cache ist
      })
    );
  }
});
