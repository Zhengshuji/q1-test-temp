# arm_reduction · 现状

> 上级：[q1_true](../STATUS.md)。**关闭**（2026-11-27）：做过可行性分析，未构造翻译；attempts 见 196–199、254、390、488、489。

## 已知（[PLAN.md](PLAN.md)）

- 载体界 $d_0\le n-p$：已证 + 精确验证（七模式取等）；
- 仿射控制只有“钉住前 $r_0$ 行”；
- q1 的条件（秩等式、$(5a)$ 包含、谱 $\forall\lambda$）都不给 $\operatorname{rank}\Phi\le3$；
- 乘法 gadget unsound ⟹ 门关系不能用秩 gadget 表达。

## 当前里程碑（2026-11-27）

按 ChatGPT 评估只做**短程检验**：候选接口 $X=[L;L_{\rm fix}]$ 的行包含。
**结果：失败**（[488](attempts/488_arm_interface_rowcount_nogo.md)）——$\operatorname{rank}X=\operatorname{rank}L$，
q1 不约束 $\operatorname{rank}L$（$L=I_n$ 反例）；接口 no-go 已写。

A 项（谱机制）也已做（[489](attempts/489_spectral_rank_forcing.md)）：$(5b)\iff Z$ 无特征向量，
不提供秩上界；剩余靶子是“谱秩强制 gadget”，未构造。

**子方向状态：关闭（不再活跃推进）**；只保留 no-go 与靶子。
