set -e

alias python="/usr/bin/env python"

uv pip install build twine

rm dist/ -rf
python -m build
python -m twine check dist/*

echo "done, now run `python -m twine upload dist/*`"
