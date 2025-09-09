set -e

alias python="/usr/bin/env python"
alias pip="python -m pip"

pip install build twine

rm dist/ -rf
python -m build
python -m twine check dist/*

echo "done, now run `python -m twine check dist/*`"
