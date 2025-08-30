const BASIC_FILTERS = [
  'www.google-analytics.com',
  'connect.facebook.net',
  'doubleclick.net',
  'api.mixpanel.com',
  'script.hotjar.com',
  'cdn.segment.com',
  'js.hs-scripts.com',
  'snap.licdn.com',
  'analytics.twitter.com',
  's.pinimg.com'
];

function basicScan(log) {
  return log.filter(entry =>
    BASIC_FILTERS.some(tracker => entry.url.includes(tracker))
  );
}
