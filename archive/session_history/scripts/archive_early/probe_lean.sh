#!/bin/bash
# 探测 Mathlib 可用性
set -e
echo "=== 磁盘空间 ==="
df -h ~ | tail -1
echo
echo "=== Mathlib master 要求的工具链 ==="
timeout 60 curl -sL https://raw.githubusercontent.com/leanprover-community/mathlib4/master/lean-toolchain || echo "(fetch failed)"
echo
echo "=== 本地 Lean 版本 ==="
lean --version
echo
echo "=== 最新 release tag ==="
timeout 60 curl -sL "https://api.github.com/repos/leanprover-community/mathlib4/tags?per_page=5" \
  | grep -o '"name": "[^"]*"' | head -5
