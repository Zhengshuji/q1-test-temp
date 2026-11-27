# arm_reduction · 成果

| 结果 | 等级 | 位置 |
|---|---|---|
| 载体界 $d_0\le n-p$；逐行忠实编码不可能 | 已证-纸面 + 精确验证 | `attempts/390` |
| 仿射控制只有“钉住前 $r_0$ 行”（限于当前参数化） | 已证-纸面 | `attempts/390` |
| 表达力引理的第一限制：$H$ 的约束是行空间型 | 分析 | `attempts/197` |
| $V$-chart / incidence 线性化：不是任意仿射 | 分析 | `attempts/198/199` |
| **接口 no-go**：$X=[L;L_{\rm fix}]$ 下 $\operatorname{rank}X=\operatorname{rank}L$，q1 不约束 $\operatorname{rank}L$ | 已证-纸面 + 精确验证 | `attempts/488_arm_interface_rowcount_nogo.md` |
| $(5b)\iff Z$ 在 $W$ 上无特征向量；不提供秩上界 | 已证-纸面（线性代数） | `attempts/489_spectral_rank_forcing.md` |
| 谱秩强制 gadget（rank $X\ge4$ ⇒ $Z$ 有特征向量） | 未构造 | 同上 |

**没有**：翻译引理、归约、谱秩强制 gadget 的不可能性。

## 外部复核（ChatGPT，2026-11-27）

| 条目 | 判定 |
|---|---|
| 1 载体界 $d_0\le n-p$ | **正确**；七模式取等是紧性证据，不替代一般证明（本仓库已有一般证明） |
| 2 逐行忠实编码不可能 | **正确**，但需明确“编码”的定义；不排除非逐行/非线性编码 |
| 3 约束传递与 $\operatorname{rank}$ 等价 | **正确**，需补 $M$ 满列秩与维数匹配 |
| 4 仿射控制只有钉住前 $r_0$ 行 | **需限定**：只对当前 q1 参数化成立；不能声称对所有等价参数化成立 |
| 5 接口 no-go | **正确，但范围有限**：只排除该接口，不排除其他秩 gadget |


