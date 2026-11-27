#!/bin/bash
# Lean 4 回归：编译全部定理文件（两组）。
# 用法（Windows）：wsl -e bash tools/lean/check_lean.sh
# 前置：文件已拷进 WSL 的 ~/WorkSpace/lean4/MyProof/MyProof/（Mathlib 预构建）。
#
# 第 0 步：`lake build MyProof.Prelude` 生成共享引理的 .olean（其余文件 import 它）。
# 第 1 组 MyProof/*.lean：逐个 `lake env lean`（不产生 olean，快）。
# 第 2 组 tools/lean/*.lean：P 递归 / (3,1) 层的支撑文件；其中几个 import MyProof.X，
#   需要对应 .olean（`lake build MyProof.PVal` 等；本工程已有）。
set -u
DEST=~/WorkSpace/lean4/MyProof/MyProof
SRC="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SRC/../.." && pwd)"
mkdir -p "$DEST"
# 源文件有两处：共享工具类在 tools/lean/MyProof/，按命题归档的在 proof/<claim>/lean/MyProof/
cp "$SRC"/MyProof/*.lean "$DEST"/ 2>/dev/null
cp "$SRC"/*.lean "$DEST"/ 2>/dev/null
for d in "$ROOT"/proof/*/lean/MyProof; do
  [ -d "$d" ] && cp "$d"/*.lean "$DEST"/ 2>/dev/null
done
cd ~/WorkSpace/lean4/MyProof || exit 1
fail=0
echo "== 第 0 步：核心模块（生成 .olean，供其它文件 import）=="
for m in Prelude ProjW CyclicVector RowSpace; do
  if /home/zsj/.elan/bin/lake build "MyProof.$m" >/dev/null 2>&1; then
    echo "$m OK"
  else
    echo "$m FAIL"
    fail=1
  fi
done
echo "== 组 1：MyProof/ =="
for f in Prelude R17A G4 A3sem A3id A3 TheoremC TheoremD TheoremE QuotientPencil CoreLemma ExistsRLemmas A2 A2dim A2root A2prop3 R17Cert QuotientEquivalence RankBarrier D0Boundary AlphaBridge Rho0Layer Isotropy PencilEquivalence Eigen A3Bound C1Closure B4FullSpace CyclicVector PBH DimArithmetic ProjW CyclicStructural B2Block D1Core KronCoeff KronFactor TypeII TypeIGeom RowSpace A0Row; do
  if /home/zsj/.elan/bin/lake env lean "MyProof/$f.lean" >/dev/null 2>&1; then
    echo "$f OK"
  else
    echo "$f FAIL"
    fail=1
  fi
done
echo "== 组 2：P 递归 / (3,1) 层 =="
for f in PRecursion PRecursionInduced PRecursionLift PRecursionLin PRecursionSigma PRecursionSigmaPoint PRecursionSigmaRange PRecursionStep PVal Perturbation QuadraticMu2 Theorem12; do
  if /home/zsj/.elan/bin/lake env lean "MyProof/$f.lean" >/dev/null 2>&1; then
    echo "$f OK"
  else
    echo "$f FAIL"
    fail=1
  fi
done
exit $fail
