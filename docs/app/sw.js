self.addEventListener('install', e=>{self.skipWaiting();e.waitUntil(caches.open('scdr-002-v3-0-8-platino').then(c=>c.addAll(['./','./manifest.json'])));});
self.addEventListener('activate', e=>{e.waitUntil(clients.claim());});
self.addEventListener('fetch', e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));});
