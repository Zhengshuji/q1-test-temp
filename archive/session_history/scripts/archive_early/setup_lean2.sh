#!/bin/bash
# 建立 Lean 项目并尝试拉取 Mathlib（修正 PATH）
export PATH="$HOME/.elan/bin:$PATH"
cd ~/qproof
rm -rf QProof
mkdir -p QProof && cd QProof

echo "leanprover/lean4:v4.34.1" > lean-toolchain

cat > lakefile.toml <<'EOF'
name = "qproof"
defaultTargets = ["QProof"]

[[require]]
name = "mathlib"
scope = "leanprover-community"
rev = "master"

[[lean_lib]]
name = "QProof"
EOF

echo "=== which lake ==="
which lake && lake --version

echo "=== lake update ==="
lake update 2>&1 | tail -40

echo "=== DONE update ==="
