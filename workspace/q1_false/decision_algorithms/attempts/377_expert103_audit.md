# 377 专家 103 号审计：漏了预设行 $L_0$；相对 Graßmannian；三处修正

> 送审件 [103](../../../for_expert/archive/103_hyperplane_parameterization.md)（已归档），
> 答复 [103-reply](../../../for_expert/archive/103_hyperplane_parameterization-reply.md)（1904 行）。
> 总评：**"substantial and promising development, not merely a correction"**；核心几何被确认，
> 但**最紧急的修正是我漏掉了预设行 $V_0=\operatorname{row}L_0$**。

## 目标

1. 记录 103 号的逐条裁决与修正。
2. 把修正写进 374/375。
3. 补上反例的完整证书（103 号 §9.2/§9.3 要求）。

## 设想与理由

103 号是新一轮审计（1904 行），重点是"参数化定理是否真的覆盖原问题"。我的预期是"修正细节"，
实际结果里有一条**结构性遗漏**（预设行 $L_0$），以及一条**维数公式写错**——这两条都必须处理。

## 做法

逐条读裁决 → 归类为"确认 / 必须修 / 建议" → 按影响面改 374（参数化）、375（复杂度）、
并补上 103 号点名的反例证书（完整数据 + 六方向 gcd + 公因子整除 + 好方向有理点）。

## 进展

1. 三处必须修已写入 374/375 的更正块（预设行、相对 Graßmannian、特征层维数）。
2. 反例证书已完成（[c357](../../../../tools/verification/c357_counterexample_certificates.py)），
   并发现方向 $(1,1)$ 是**特征方向**（$A_{21}(1,1)=0$），其纤维有 4 个参数（不是 3）。
3. $L_0$ 的修正不破坏 $p$ 的界（$(s-\delta)(r-s)\le p^2$）。

## 裁决总表
| 组件 | 裁决 |
|---|---|
| 压缩特征向量刻画 | **正确** |
| 特征/非特征分层 | **正确** |
| 常秩丛构造 | 原则上正确 |
| Graßmannian 纤维 | 对**无约束**行空间正确 |
| **带预设 $L_0$ 的完整参数化** | **不完整（必须修）** |
| 乘积表示 | **须换成相对 Graßmannian** |
| **特征层维数** | **写错了**（应是 $h_\mu-1$，不是 $d_\mu-1$） |
| 重特征值反例 | 重要，但需完整数据与证书 |
| 固定 $p$ 几何界 | 本质上正确 |
| 极大子式计数 | 正确且有用 |
| 固定 $p$ 位复杂度 | 需更细 |
| 随机化重复情形算法 | 有前景（单侧保证） |
| 与 Paper II 的联系 | 强，值得发展 |

## 三处必须修正

### 1. 预设行 $L_0$ 被漏掉了（最重要）

原问题要求 $\mathcal L=[L_0;R]$，即 $V_0=\operatorname{row}L_0\subseteq V$，且 $L_0v=L_0Av=0$。
所以：

- **底要限制**：$E_\mu^0=E_\mu\cap\ker L_0\cap\ker(L_0A)$；
- **纤维是"扩张"而非任意子空间**：$\delta=\dim V_0-\dim(V_0\cap K_0)$，
  $$\text{纤维}=\operatorname{Gr}\bigl(s-\delta,\ \mathcal Q_v/\overline V_{0,v}\bigr),\qquad s=q-k+1,\ \mathcal Q_v=U_v^\perp/D_v,$$
  维数 $(s-\delta)(r(v)-s)$，非空 $\iff \delta\le s\le r(v)$；
- **generic gcd 必须在受约束的族上算**。

好在这不破坏 $p$ 的界：$(s-\delta)(r-s)\le p^2$ 仍成立（$p=1$ 时 $q=k$、$\delta=0$，我们此前所有实例正是这一档）。

### 2. 相对 Graßmannian，不是乘积

$U_v^\perp/D_v$ 随 $v$ 变，**没有全局平凡化**，所以不能写成 $\mathbb P(E_\mu)\times\operatorname{Gr}(\cdot)$；
正确写法是 $\operatorname{Gr}_{B}(s,\mathcal Q)$（相对 Graßmann 丛）。

### 3. 特征层维数写错

特征层的底是 $\mathbb P(E_\mu\cap\ker A_{21})$，维数 $h_\mu-1$（$h_\mu=\dim(E_\mu\cap\ker A_{21})$），**不是** $d_\mu-1$。正确公式：
$$\dim X_{\text{eig}}=h_\mu-1+s(\rho-s),\qquad \dim X_{\text{non}}=d_\mu-1+s(\rho-1-s).$$

## 其余修正与澄清

- **非退化假设是多余的**：标准欧氏内积正定 ⟹ $K_0\cap K_0^\perp=0$ 自动成立。**删掉这条假设**。
- **"单谱"应改为"几何单谱"**：只需 $\dim\ker(M-\mu I)=1$（代数重数可 $>1$），覆盖更大一类。
- **Theorem 2 是 promise-class 定理**：超出承诺类时**拒绝**（而不是报不可行）——这正是我们在做的。
- **全行秩归一化引理**：$q$ 是行数不是秩；行相关的可行解可扩张为 $q$ 维行空间（当 $q\le\dim U_v^\perp$），故存在性可假设满行秩。
- **坐标无关写法**推荐：用余向量 $\alpha_v(u)=\langle u,v\rangle$、$\beta_v(u)=\langle u,Av\rangle$，条件即 $\beta_v=\mu\alpha_v$；纤维 $=\operatorname{Gr}(s-\delta,\mathcal A_v/\mathcal D_v)$。
- **$V\cap K_0$ 的记号**：$V\subset X^*$、$K_0\subset X$ 是不同的空间，"$V\cap K_0$"要靠内积识别；坐标无关写法应改用 $\operatorname{res}_K$。
- **与 Paper II 的统一**（Q5，强）：层里方向 $[v]$ 与 Paper II 的公共投影 $U=\pi_1(W)=\pi_2(W)=a^\circ$ **对偶**：
  $$[a]=\mathbb P(\operatorname{Ann}(U)),\qquad U=a^\circ .$$
  于是"压缩特征向量"就是 Paper II 子空间几何在 $\dim U=k-1$ 的特化。
- **Q1**：正确的群是**完整数据的稳定子**，不是 $M$ 的中心化子；用 $A_{21}|_{E_\mu}$ 的秩正规形分三种情形（$s=0$ / $0<s<d$ / $s=d$）。
- **Q2**：扰动只能单向（Perturbation lemma：$\exists D$ 使 $Dv=0$ 且 $LDN=0$ 时可行解保持）；反向不成立（可行性可在极限处消失）。
- **Q3**：随机化单侧可接受（输出 {FEASIBLE, UNKNOWN}），但**不能**叫完整判定算法。

## 已落实（本轮）

1. **反例证书**（103 号 §9.2/§9.3）：[c357](../../../../tools/verification/c357_counterexample_certificates.py) 给出
   $A,C,N,M,A_{21}$ 全部数据；六个方向的符号 gcd；坏方向验证"公因子整除全部子式"；
   好方向给出有理图卡点 $x_0=(1,2,3,4)$（$\gcd=1$）。
   **新发现**：方向 $(1,1)$ 其实是**特征方向**（$A_{21}(1,1)=0$），所以它的纤维有 $4$ 个参数（不是 3）。
2. 374/375 加更正块（预设行、相对丛、维数、非退化、几何单谱、promise-class）。

## 最终结论

1. **核心几何被确认**（压缩特征向量、Graßmann 丛、极大子式计数、$p^2$ 纤维界）。
2. **必须修**：预设行 $L_0$（最重要）、相对 Graßmannian、特征层维数。
3. 反例现在有完整数据与证书。
4. 下一步（103 号给的优先级）：① 修参数化 ② 反例证书（已完成）③ 位复杂度 ④ Paper II 字典 ⑤ 重复谱算法。

## 放弃原因

- 没有重写 374 的完整定理（只加更正块）；
- 没有做预设行的实现（当前代码 $L_0$ 为空，$\delta=0$）；
- 没有做坐标无关改写。

## 残留价值

- 一份**逐条裁决**与三处硬修正；
- 反例的**完整可复现证书**；
- Paper II 的对偶表述（$[a]=\mathbb P(\operatorname{Ann}(U))$）。

## 相关文件

- [attempts/374](../../c_stratification/attempts/374_complete_parameterization.md)（参数化，加更正）
- [attempts/375](../../c_stratification/attempts/375_stage2_bit_complexity.md)（位复杂度，加更正）
- [attempts/376](../../c_stratification/attempts/376_repeated_eigenvalue_matters.md)（反例）
- [c357](../../../../tools/verification/c357_counterexample_certificates.py)（证书）

## 状态

- 核心几何：**被确认**。
- 完整参数化（带 $L_0$）：**[待修]**。
- 反例证书：**[已完成]**。
- 位复杂度：**[待细]**。
