#!/bin/bash
export PATH="$HOME/.elan/bin:$PATH"

echo "=== 测试 git 连通性 ==="
timeout 90 git ls-remote https://github.com/leanprover-community/mathlib4 HEAD 2>&1 | head -3
echo "git-ls-remote exit: $?"

echo
echo "=== 若失败，尝试 git 配置调整 ==="
git config --global http.postBuffer 524288000
git config --global http.version HTTP/1.1
git config --global http.lowSpeedLimit 0
git config --global http.lowSpeedTime 999999
git config --global core.compression 0

timeout 120 git ls-remote https://github.com/leanprover-community/mathlib4 HEAD 2>&1 | head -3
echo "retry exit: $?"

echo
echo "=== 测试镜像 gitee ==="
timeout 60 curl -sI https://gitee.com 2>&1 | head -2
timeout 60 curl -sI https://mirror.ghproxy.com 2>&1 | head -2
timeout 60 curl -sI https://ghfast.top 2>&1 | head -2
