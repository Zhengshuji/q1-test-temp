# A2 收尾：谱可行性、纤维几何、剩余问题

> 2026-10-31 收尾文档。**证明本体在 [proof/incidence_strata/](../../../trash/README.md)**（§1–16）；
> 本文只做**汇总、问题清单、思路与教训**。实验脚本在 `proof/layer_program/c265–c276`；Lean 在 `tools/lean/MyProof/`。

## 1. A2 是什么

固定可容许 $S\subseteq G=\mathcal V\cap H$，纤维
$$\mathcal F_S=\{U:\ T_S\subseteq U\subseteq H/S,\ \dim U=r,\ U\cap B_S=0\},$$
问题：$\exists U\in\mathcal F_S$ 使 $Z=S\oplus U$ 满足谱条件 $(S)$（$T_\lambda$ 对所有 $\lambda$ 满列秩）？

**关键更正（QA17）**：$U$ 活在 $H/S$ 而 $P$ 的像在 $W/S$，故相关对象是
$$I_\lambda:=\operatorname{im}P(\lambda)\cap(H/S),\qquad r_\lambda=\dim I_\lambda,$$
失败条件 $=\big[\ker P(\lambda)\ne0\big]$ **或** $\big[U\cap I_\lambda\ne0\big]$。

## 2. 已建立的成果

| # | 结果 | 等级 | 位置 |
|---|---|---|---|
| 1 | **核障碍**：$\exists\lambda,v\notin S,A v=\lambda v$（模 $S$）⟹ 任何 $U$ 失败 | **Lean** `A2.lean` + 实例 120/120 | §2 |
| 2 | **$T_S$ 障碍**：$\exists\lambda,T_S\cap I_\lambda\ne0$ ⟹ 任何 $U$ 失败 | 纸面 | §2 |
| 3 | **命题 2**：$m\ge r+t+1$（+ 无核 + $T_S\cap I_\lambda=0$）⟹ 可行 | 纸面 + 维数核 **Lean** `A2dim.lean` | §4 |
| 4 | **命题 3**：全超平面情形，可行 $\iff f_0\|_L\ne0$ | 纸面 + 代数核 **Lean** `A2prop3`+`A2root` | §5 |
| 5 | **命题 4**：$r=1,k=0$ 四分类（按 $d_{\max}$）| 纸面 + 两实例 | §6 |
| 6 | **命题 5**：一般 $r$ 三分（$c_\lambda\ge2$/$\le0$/=1）| 纸面 | §7 |
| 7 | $r=1$、$k=1$：$U=T_S$ 唯一，直接检验 | 纸面 | §6 |
| 8 | **引理 10.1'**：$\operatorname{rank}P$ 与 $\dim I_\lambda$ **双常数** ⟹ 多项式基 | 纸面（专家给子丛论证）| §10 |
| 9 | **Plücker 线性化**：$q_{U,j}$ 是 Plücker 坐标的线性泛函 | 纸面 | §11.1 |
| 10 | **精确判据**：可行 $\iff \operatorname{Gr}\cap L\not\subseteq\{q_0=0\}$ | 纸面 | §11.2 |
| 11 | **提升判据**（$r=1$）：可行 $\iff\exists u\in K\setminus B_S,\ f_\lambda(u)\ne0\ \forall\lambda$ | 纸面 + 抽象双向验证 | §11.2b′–b‴ |
| 12 | 结构性条件：$\dim(H/G)\le p$；可行全超平面实例需 $\dim(H/G)\ge2$ | 纸面 + 核算 | §11.2b⁗ |
| 13 | **正反两类实例**：反例（c272，42 个全失败，证明需 $B_S$）+ 正向（c276，3 个，$(A)$✓$(S)$✓）| 精确算术 | §11.2b‴/b⁙ |
| 14 | R17 两个例子的**显式左逆证书** | **Lean** `R17Cert.lean` + Python | §13 |
| 15 | G3 适用域：$D<m-r$ 时判据是线性代数 | 纸面 + Gr(2,4) 实验 | §15–16 |

## 3. 剩余问题

### A. 真正的开放数学问题

**G3：退化线性截面。** $X=\operatorname{Gr}(r,m)\cap L$ 的张成 $\operatorname{span}(X)\subsetneq L$ 时，
$q_0$ 可能在 $\operatorname{span}(X)$ 上为零而不在 $L$ 上 ⟹ 判据失效。
- 仅当 $D\ge m-r$（薄参数区）才可能退化；
- 需要计算线性截面的线性张成（Gröbner/理想成员判定）；
- **这是 A2 唯一的真缺口**。

### B. 未形式化（已证明，未 Lean）

| 项 | 缺少什么 |
|---|---|
| 命题 4 四分类 | 射影维数理论 + 上半连续（与结论无关，可缓）|
| 引理 10.1' | $\mathbb C[\lambda]$ 的模论（Quillen–Suslin）|
| G5 一般/例外分段 | 层论式的"截面在 $\Omega$ 上无零点"表述 |

### C. 已降级/已明确

- **G1 次数界**：不需要（$\exists\R$ 编码用左逆，不依赖基的次数）；
- **G6 实/复**：判据是复的、编码是实的，两者不等价**未被排除**；论文里必须分开写。

### D. 隐性缺口

1. $r\ge2$ **且** $k\ge1$ 的除子情形没有单独验证；
2. **所有已验证实例都是 $r=1$**（含 R17 的 $t=2$ 族点）。

## 4. 下一步的想法

| 路线 | 内容 | 成本/风险 |
|---|---|---|
| **G3-a** | 写 G3 简报给专家（含 §15/§16），确认是否值得投入 | 低 |
| **G3-b** | 对最小退化例（$m=4,r=2$、$D\ge2$）用 Gröbner 基算 $\operatorname{span}(X)$ | 中 |
| **G3-c** | 若退化情形可判 ⟹ 除子情形完全解决 ⟹ A2 完成 | 高 |
| **辅** | 补 $r\ge2$ 的实例、补命题 4 的 Lean | 低价值 |

**我的判断**：G3 的难度在"计算线性截面的张成"，是**计算代数几何**问题，不是本项目独有的困难；
若专家认为它可接受为"薄集、可忽略"，则 A2 可以就此收尾（判据在非退化情形成立、退化情形显式标出）。

## 5. 教训（本阶段三次自纠 + 两次采样陷阱）

| # | 错误 | 根源 |
|---|---|---|
| 1 | §4.1 把坏条件写成"单个线性形式" | 只在 $\operatorname{rank}P=m-1$ 时成立 |
| 2 | §8 说"首项系数给 Schubert 除子" | $B_D$ 不必满列秩 |
| 3 | 引理 10.2 的假设不足 | $\operatorname{rank}P$ 常数推不出 $\dim I_\lambda$ 常数 |
| 4 | "1006 例全超平面、0 例纤维非空" | **把线性条件当稀有事件采样**——$(A)$ 是闭的线性条件，不该采样 |
| 5 | "全超平面 ⟺ 常值"判据（B.5）| 把**射影闭包**的交点当成**实际像**上的点 |

**共同模式**：把"一般情形"的直觉用在需要额外假设的地方；以及**用采样代替代数判定**（CLAUDE §10.1 的禁区）。

## 6. 文件索引

- 证明：[proof/incidence_strata/README.md](../../../trash/README.md)（§1–16）
- Lean（11 文件，全部退出码 0）：`tools/lean/MyProof/{A2,A2dim,A2root,A2prop3,R17Cert}.lean` + 早前 6 个；回归 `tools/lean/check_lean.sh`
- 实验：`proof/layer_program/c265`（边界）、`c267`（R17 纤维）、`c268`（左逆证书）、`c270–c276`（G4 判据与实例）
- 专家往来：`archive/expert_correspondence/QA17–QA20`
