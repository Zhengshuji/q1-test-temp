# 专家 61 号裁决落实：约定分层、$c=1$ 例外、求解器架构

> 2026-11-08。汇总 61 号答复：$c=0$ 与 $c=1$ 确认；$c=2$ 在约定下有效；全 $q$ 结论需按
> $\mathsf P_{\rm ind}$/$\mathsf P_{\rm full}$ 分层；求解器需补 $r>1$ 的商秩与提升层。
> 状态：**M2（记录）**。

## 目标

把 61 号答复逐条落实，明确哪些结论与约定无关、哪些依赖约定。

## 设想与理由

专家区分两个问题：
$$\mathsf P_{\rm ind}:\ \operatorname{rank}L=q,\ \operatorname{rank}[C;L]=p+q,\ (5a),(5b);$$
$$\mathsf P_{\rm full}:\ \operatorname{rank}L=q,\ (5a),(5b).$$
关键：$V\subseteq W_L$ 与“$\dim W_L=c\Rightarrow V=W_L$”**只由 $(5a)$ 推出**，与约定无关；
依赖约定的是**提升**（$L$ 的行是否独立模 $\operatorname{row}C$）。

## 做法：逐条落实

### 1. 约定（Q1）

- $V\subseteq W_L$：由 $(5a)$ + 固定顶行，**与约定无关**；
- $V=W_L$（当 $\dim W_L=c$）：由维数，**与约定无关**；
- 提升：$\mathsf P_{\rm ind}$ 用 $d'_C\ge\dim\ker Z_{\rm pair}$；$\mathsf P_{\rm full}$ 下需重新分析。

**推论（本文件新增）**：16/21 的 $q=3,c=2$ 不可行论证只用压缩方程（$H_A|_V=0$、$b$ 强制），
**与约定无关**；$c=1$ 引理用 $l_i$ 的任意提升（$l_iN=h_i$），也**与约定无关**；$c=0$ 行列式同理。
所以只要“不存在压缩对”，$\mathsf P_{\rm ind}$ 与 $\mathsf P_{\rm full}$ 都不可行——提升条件在无压缩对时无关紧要。
（专家要求先核对原始定义；本推论说明即便原始是 $\mathsf P_{\rm full}$，结论也可能不变。）

### 2. $c=1$ 引理（Q2）

- 超平面论证确认，任意 $\omega$（不只 $\omega=3$），条件 $W_L\subseteq D$；
- **特征线方程恒零**是独立分支：若 $\dim W_L\ge2$ 且所有 $v\in W_L$ 都是特征向量，则 $A|_{W_L}=\lambda I$，
  超平面论证失效，需另查；
- 两个 seed 的特征线多项式非零（21：$a(a-b)$；16：$2a^2-2ab+b^2$），故不触发该分支；
- 专家建议为每条特征线输出完整证书（$v$、$\lambda$、$w$、$\operatorname{Ann}(V)$ 基、$\varphi$ 的坐标、非零见证）。

### 3. $c=0$（Q3）

- 确认：$k=q=\omega\ge1$、$H$ 可逆，$\det P$ 次数恰为 $k$，在 $\mathbb C$ 上有根；
- 边界：$k=0$ 单独处理；实 $\lambda$ 不适用（需要代数闭域）。

### 4. $c=2$（Q4）

- 确认：行式强制与 $q$ 无关；$\alpha=(-1,0)$ 证书正确；
- 建议把 $\mathrm{Des}_i$、$\alpha$、$\alpha^{\mathsf T}\mathrm{Des}_i=e_b$ 明写进论文。

### 5. 求解器（Q4/Q5）

专家指出四点：
1. **$r>1$**：$\operatorname{rank}H=\omega$ 的正确条件是底部行在
   $$\operatorname{Ann}(V)/\operatorname{row}(L_0N)$$
   中的投影秩为 $\omega-\rho_0$（$\rho_0=\operatorname{rank}(L_0N)$），不是 $\omega-1$；
   当前工具只对 $r=1$ 正确；
2. **$V$ 的枚举**：$\operatorname{Gr}(c,W_L)$ 连续，有限枚举不是判定；需要多项式系统/分层；
3. **提升层**：压缩对不等于实际 $L$；应作为独立层（$\Psi$、$d'_C$）；
4. **四层架构**：几何 → 压缩行 → 谱检验 → 实际提升。

### 6. 复杂性（Q6）

- $\exists\mathbb R$ 成员：确认，但要写清 normal rank、实/虚部编码（$(\operatorname{Re}z)^2+(\operatorname{Im}z)^2>0$）；
- 求解器不建立 RP/BPP；NP 成员/硬度均未定。

## $r>1$ 的实现（2026-11-08 补）

新增 [tools/verification/stratum_solver_general.py](../../../../tools/verification/stratum_solver_general.py)：
把 $(b_{ij})$ 的秩条件换成商空间 $\operatorname{Ann}(V)/\operatorname{row}(L_0N)$ 上的秩 $\omega-\rho_0$
（$\rho_0=\operatorname{rank}(L_0N)$），并在基 $S_0$（$\rho_0$ 个）与 $u_1..u_{\omega-\rho_0}$ 上参数化底部行。

测试：
- $r=1$ 回归：seed10 FOUND，16/21 none——与旧工具一致；
- $r=2$ 合成实例（把 seed10 见证的前两行取作 $L_0$，第三行作底部）：修复一个 $\omega=\rho_0$ 的边界后，
  **random 与 grid 两种模式都 FOUND**。
  修复点：当 $\omega=\rho_0$ 时商维为 0，“每个底部行都被强制”是空真，旧代码据此跳过所有 $V$；
  现改为此时不要求非强制，直接解 $(c,g)$ 并（商条件空）继续。

## 提升层（2026-11-08 补）

`stratum_solver_general.py` 增加 `lift_data(A,C,L0,H,HA)`：
- **可实现性**：每对 $(h_i,h_{A,i})$ 解 $g[N;AN]=(h_i,h_{A,i})$，不可解则该压缩对不可提升；
- $d'_C=\dim E'_C=(\dim\operatorname{row}[C;CA]-\operatorname{rank}\Gamma)-\operatorname{rank}C$，
  $\Gamma(g)=gAN$；
- $\dim\ker Z_{\rm pair}=q-\operatorname{rank}\{(h_i,h_{A,i})\}$；
- 判据：可实现且 $\dim\ker Z_{\rm pair}\le d'_C$。
在谱检验之前调用；不满足则跳过该候选。

测试：$r=1$ 回归（10 FOUND、16/21 none）与 $r=2$ 合成实例（FOUND）都通过。

## 进展

* 约定分层（$\mathsf P_{\rm ind}$/$\mathsf P_{\rm full}$）明确；
* 新增推论：压缩不可行性与约定无关，故 16/21 的全 $q$ 结论对两个问题都可能成立；
* $c=1$ 的恒零分支、求解器的 $r>1$ 与提升层问题已记录；
* 专家要求的证书包（$K_0,N,W_L$ 基、$W_L\subseteq D$、$\mathrm{Des}$ 证书、特征线多项式、$\det$ 首项）列为待办。

## 最终结论

* $c=0$、$c=1$、$c=2$ 的核心论证被确认；
* 全 $q$ 结论的措辞应按 $\mathsf P_{\rm ind}$/$\mathsf P_{\rm full}$ 分层，且压缩部分与约定无关；
* 求解器需补 $r>1$ 商秩与提升层，才配称“判定器”。

## 放弃原因

* 未重做 $\mathsf P_{\rm full}$ 的提升分析（但压缩部分已无关）；
* 未实现 $r>1$ 的商秩与提升层；
* 未输出专家要求的完整证书包。

## 残留价值

* 约定分层的清晰表述；
* “压缩不可行 ⇒ 两个问题都不可行”的论证；
* 求解器四层架构的蓝图。

## 相关文件

* [attempts/185](185_seeds_infeasible_all_q.md)（全 $q$ 结论）
* [attempts/182](182_c1_infeasibility_lemma.md)、[183](183_c1_eigenlines.md)（$c=1$）
* [attempts/184](184_q4_excluded.md)（$c=0$）
* [attempts/180](180_uniform_stratum_solver.md)（求解器）

## 状态

* 裁决落实：**[完成，M2]**。
* $r>1$/提升层/证书包：**[未做]**。
