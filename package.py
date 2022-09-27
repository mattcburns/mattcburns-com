#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile

# Delete the old deployment, if exists
z = Path('deploy.zip')
z.unlink(missing_ok=True)

# Gather up any html
p = Path('.')
file_set = list(p.glob('**/*.html'))

# Write all our html to zip
with ZipFile('deploy.zip', 'w') as deployzip:
    for f in file_set:
        deployzip.write(f)

# Finally, just do an upload to Cloudflare
