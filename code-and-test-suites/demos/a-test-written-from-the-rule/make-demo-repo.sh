#!/usr/bin/env bash
# Rebuilds the demo repository with its two commits:
#   1. "Billing service baseline"
#   2. "Add late fee for overdue invoices (#412)"
# Run from this folder: bash make-demo-repo.sh
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cd "$here/ledgerline-billing"
rm -rf .git
git init -q
git config user.name "Ledgerline"
git config user.email "demo@ledgerline.example"
git apply -R "$here/pull-request-412.patch"
git add -A && git commit -q -m "Billing service baseline"
git apply "$here/pull-request-412.patch"
git add -A && git commit -q -m "Add late fee for overdue invoices (#412)"
git log --oneline
