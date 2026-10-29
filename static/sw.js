/* LexStudy Ghana v0.2 service worker: cache static assets only.
   It does not cache account, quiz or IRAC submissions, and it does
   not make full notes available offline yet — that is a v0.3 step. */
const CACHE = "lexstudy-v0.2";
self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(["/static/style.css", "/static/icon.svg"])));
});
self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  const url = new URL(event.request.url);
  if (url.pathname.startsWith("/static/")) {
    event.respondWith(caches.match(event.request).then((hit) => hit || fetch(event.request)));
  }
});
