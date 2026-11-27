#!/bin/bash
# 建立 Lean 项目并尝试拉取 Mathlib
set -x
cd ~/qproof
rm -rf QProof
mkdir -p QProof && cd QProof

# 固定到本地已安装的工具链（避免下载新 Lean）
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

echo "=== lake update (拉取 mathlib 源码) ==="
lake update 2>&1 | tail -30

echo "=== 开始构建（仅 mathlib 的核心部分，用缓存） ==="
lake exe cache get 2>&1 | tail -20 || echo "(cache get 失败，可能需要完整构建)"

echo "=== DONE ==="
ls -la
