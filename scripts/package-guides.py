"""Make reproducible offline guide bundles from the published HTML and media."""
import hashlib
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parent.parent
checksums = []
for slug, name in [('cold-open', 'ColdOpen'), ('backlot', 'Backlot')]:
    source = root / 'guides' / slug
    destination = root / 'downloads' / f'{name}-user-guide.zip'
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for file in sorted(source.rglob('*')):
            if not file.is_file():
                continue
            info = zipfile.ZipInfo(f'{name}-user-guide/{file.relative_to(source).as_posix()}')
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, file.read_bytes())
    checksums.append(f'{hashlib.sha256(destination.read_bytes()).hexdigest()}  {destination.name}')
    print(f'{destination.name}: {destination.stat().st_size:,} bytes')
(root / 'downloads' / 'GUIDE-SHA256SUMS').write_text('\n'.join(checksums) + '\n')
