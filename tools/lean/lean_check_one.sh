#!/bin/bash
# 单文件 Lean 检查：把源文件同步进 WSL 的 lake 工程，然后只编译指定的一个文件。
# 用法（Windows）：wsl -e bash tools/lean/lean_check_one.sh KronFactor
set -u
DEST=~/WorkSpace/lean4/MyProof/MyProof
SRC="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SRC/../.." && pwd)"
mkdir -p "$DEST"
cp "$SRC"/MyProof/*.lean "$DEST"/ 2>/dev/null
cp "$SRC"/*.lean "$DEST"/ 2>/dev/null
for d in "$ROOT"/proof/*/lean/MyProof; do
  [ -d "$d" ] && cp "$d"/*.lean "$DEST"/ 2>/dev/null
done
cd ~/WorkSpace/lean4/MyProof || exit 1
exec /home/zsj/.elan/bin/lake env lean "MyProof/$1.lean"
