# run this file if you'd like to know what assets are left to create
# TODO: re-implement this in powershell, I was too slow.

import os
import re

DIRNAME = os.path.dirname(__file__)
REPO_DIRPATH = os.path.abspath(os.path.join(DIRNAME, '../'))

# run the linter which generates lin.txt
# _scripts/cli.ps1 -Action lint
# print(REPO_DIRPATH)

lint_txt = os.path.join(REPO_DIRPATH, 'lint.txt')
with open(lint_txt) as r:
    lines = r.read().splitlines()

remaining_assets = set()
for line in lines:
    mo = re.search(r"\d '([A-Za-z0-9_]+)' is not an image", line)
    if mo:
        remaining_assets.add(mo.groups()[0])

for asset in sorted(remaining_assets):
    print(asset)
