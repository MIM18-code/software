"""Validate local links, fragments and offline bundles before publication."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import zipfile

root = Path(__file__).resolve().parent.parent

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for name in ['href', 'src']:
            if name in attrs:
                self.links.append(attrs[name])

pages = {file: Page(file.read_text()) for file in root.glob('guides/**/*.html')}
pages[root / 'index.html'] = Page((root / 'index.html').read_text())
for app_page in sorted(root.glob('*/index.html')):
    if app_page.parent.name not in ('guides', 'downloads', 'node_modules'):
        pages[app_page] = Page(app_page.read_text())
checked = 0
for file, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        destination = (root / unquote(url.path).lstrip('/') if url.path.startswith('/') else file.parent / unquote(url.path)).resolve() if url.path else file
        assert destination.is_relative_to(root), (file, link, 'outside site')
        assert destination.exists(), (file, link, 'missing file')
        if url.fragment and destination in pages:
            assert unquote(url.fragment) in pages[destination].ids, (file, link, 'missing fragment')
        checked += 1
for line in (root / 'downloads/GUIDE-SHA256SUMS').read_text().splitlines():
    digest, name = line.split()
    bundle = root / 'downloads' / name
    assert hashlib.sha256(bundle.read_bytes()).hexdigest() == digest, name
    with zipfile.ZipFile(bundle) as archive:
        assert archive.testzip() is None, name
        slug = 'cold-open' if name.startswith('ColdOpen') else 'backlot'
        prefix = name.removesuffix('.zip')
        for file in (root / 'guides' / slug).rglob('*'):
            if file.is_file():
                relative = file.relative_to(root / 'guides' / slug)
                assert archive.read(f'{prefix}/{relative.as_posix()}') == file.read_bytes(), relative
print(f'{len(pages)} HTML pages, {checked} local links/fragments, both complete offline bundles: passed')
