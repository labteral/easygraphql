#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
rm -rf dist build
python3 -m build
python3 -m twine check --strict dist/*
python3 -m twine upload dist/*
