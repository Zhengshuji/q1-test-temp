# 353 工具选择：MATLAB 的符号计算在"数域瓶颈"上比 sympy 快两个数量级

> 承接 352（数域判定器；三次域计算太慢）。本轮测了 MATLAB 是否更好——**是的，在这个瓶颈上**。

## 目标

判断把数域判定器换到 MATLAB 是否值得。

## 设想与理由

瓶颈是：系数为三次代数数 $\mu$ 的多项式 gcd（$f_i(\lambda)\in\mathbb Q(\mu)[\lambda]$）。
sympy 用根式表达处理，太慢（>20 分钟未出结果）。MATLAB 的 Symbolic Math Toolbox（MuPAD 内核）
在多项式算术上通常更强。

## 做法与结果

**环境**：MATLAB R2023b，`license('test','Symbolic_Toolbox') = 1` ✓（有 Symbolic Math Toolbox）。

**基准**（$\mu$ 取 $x^3+4x^2+2x-5$ 的根，$f_1=(\lambda-1)(\lambda^2+\mu)$、$f_2=(\lambda-2)(\lambda^2+\mu)$）：

| 工具 | 三次系数上的 gcd |
|---|---|
| sympy 1.13.2 | **> 20 分钟**（未完成） |
| MATLAB symbolic | **0.08 秒** ✓ |

**移植**：`decider_matlab.m`（读 $A,C$ 的 CSV → 符号化 → $K_0$ → 压缩 $M$ → `eig` → 各特征向量的纤维 → gcd）。
数据导出：[export4246.py](../../../../workspace/_exchange/export4246.py)（临时脚本，在 `_scratch`）。

## 进展

1. **MATLAB 确实更好**（对这个任务）：三次域的 gcd 快两个数量级。
2. 移植脚本已跑通前半段：`rank[C;CA] = 4`、$k=4$、$\omega=3$、特征多项式 $x^4+3x^3-2x^2-7x+5$ ✓
   （与 sympy 的 $(x-1)(x^3+4x^2+2x-5)$ 一致）。
3. 完整判定（含每个特征向量的纤维 gcd）在跑，`simplify` 仍是主要耗时。

## 最终结论

1. **数域瓶颈该用 MATLAB（或 Sage/PARI）**，不该用 sympy。
2. 移植是可行的，且前半段已验证与 sympy 一致。
3. 4246 的最终判定仍待 MATLAB 跑完（本文不预判）。

## 放弃原因

- 4246 的完整判定未跑完（MATLAB 的 `simplify` 在四次特征多项式上仍慢）；
- 没有把 MATLAB 脚本纳入 `tools/`（它依赖 `_scratch` 里的数据文件，且 `-batch` 的 UTF-8 输出在 PowerShell 下会乱码）；
- 没有测 Sage/PARI（未安装）。

## 残留价值

- 一条**工具结论**：数域 gcd 在 MATLAB 里快两个数量级（0.08 s vs >20 min）；
- 一个可复跑的移植脚本（`workspace/_exchange/decider_matlab.m`）；
- 明确了"以后遇到数域运算该用什么"。

## 相关文件

- [attempts/352](352_number_field_decider.md)（sympy 版判定器）
- [attempts/350](350_admissible_v_are_eigenvectors.md)（可容许 $v$）
- [attempts/351](351_retract_instance_infeasibility.md)（撤回实例级结论）

## 状态

- 工具对比：**[精确验证]**（同一 gcd，0.08 s vs >20 min）。
- MATLAB 移植：**前半段已验证**；完整判定**未完成**。
- 4246：**仍未判定**。
