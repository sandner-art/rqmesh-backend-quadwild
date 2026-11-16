#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# Initialise every submodule except the non-free Blossom-V (libs/blossom5-cmake).  satsuma only uses it when
# SATSUMA_ENABLE_BLOSSOM5=ON (default OFF), so the build does not need it.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
git submodule sync --recursive
git config -f .gitmodules --get-regexp '\.path$' | awk '{print $2}' | grep -v '^libs/blossom5-cmake$' |
while read -r p; do
  for i in 1 2 3; do                       # two submodules live on graphics.rwth-aachen.de:9000; retry
    git submodule update --init --recursive -- "$p" && break || { echo "retry $p ($i)"; sleep 10; }
  done
done
git submodule status --recursive
