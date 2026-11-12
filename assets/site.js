// Copy buttons
document.querySelectorAll('.copy').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var text = document.getElementById(btn.dataset.copy).textContent;
    var done = function () {
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = 'Copy'; }, 1600);
    };
    try {
      navigator.clipboard.writeText(text).then(done, function () { btn.textContent = 'Select and copy'; });
    } catch (e) { btn.textContent = 'Select and copy'; }
  });
});

// Pick up new releases from GitHub so the pages don't go stale.
// The links written into the HTML are the fallback if this fails.
var APPS = {
  'cold-open':     { repo: 'MIM18-code/cold-open', prefix: /^Cold Open\s+/i, dmg: /^ColdOpen-.*\.dmg$/, source: /-source\.tar\.gz$/, sums: /^SHA256SUMS$/ },
  'backlot':       { repo: 'MIM18-code/homebrew-backlot', prefix: /^Backlot\s+/i, dmg: /^Backlot-.*\.dmg$/, source: /-source\.tar\.gz$/, sums: /^SHA256SUMS$/ },
  'dumptruck':     { repo: 'MIM18-code/dumptruck', prefix: /^Dumptruck\s+/i, dmg: /\.dmg$/ },
  'lacquer':       { repo: 'MIM18-code/lacquer', prefix: /^Lacquer\s+/i, dmg: /^Lacquer-.*\.dmg$/, source: /-source\.tar\.gz$/, sums: /^SHA256SUMS$/ },
  'writers-block': { repo: 'MIM18-code/writers-block-releases', prefix: /^Writers Block\s+/i, dmg: /^WritersBlock-.*\.dmg$/, sums: /^SHA256SUMS$/ }
};
function setAll(app, attr, key, fn) {
  document.querySelectorAll('[data-app="' + app + '"][' + attr + '="' + key + '"]').forEach(fn);
}
Object.keys(APPS).forEach(function (app) {
  // Only ask GitHub about the apps this page shows.
  if (!document.querySelector('[data-app="' + app + '"]')) return;
  var cfg = APPS[app];
  fetch('https://api.github.com/repos/' + cfg.repo + '/releases?per_page=10')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (list) {
      var rel = list.filter(function (r) { return !r.draft; })[0];
      if (!rel) return;
      var find = function (re) { return re && rel.assets.filter(function (a) { return re.test(a.name); })[0]; };
      var dmg = find(cfg.dmg);
      if (!dmg) return;
      var version = (rel.name || rel.tag_name).replace(cfg.prefix, '').replace(/^v/, '');
      var mb = Math.round(dmg.size / 1e6) + ' MB';
      setAll(app, 'data-field', 'version', function (el) { el.textContent = version; });
      setAll(app, 'data-field', 'size', function (el) { el.textContent = mb; });
      setAll(app, 'data-href', 'dmg', function (el) { el.href = dmg.browser_download_url; });
      setAll(app, 'data-href', 'release', function (el) { el.href = rel.html_url; });
      ['source', 'sums'].forEach(function (k) {
        var a = find(cfg[k]);
        if (a) setAll(app, 'data-href', k, function (el) { el.href = a.browser_download_url; });
      });
      // The checksum written in the HTML belongs to that exact file. Keep it only if the file hasn't changed.
      var shaInBody = (rel.body || '').match(/SHA-256:\s*`?([0-9a-f]{64})/i);
      setAll(app, 'data-field', 'sha', function (el) {
        if (shaInBody) el.textContent = 'DMG SHA-256: ' + shaInBody[1];
        else if (el.dataset.file !== dmg.name) el.hidden = true;
      });
    })
    .catch(function () { /* keep the built-in links */ });
});
