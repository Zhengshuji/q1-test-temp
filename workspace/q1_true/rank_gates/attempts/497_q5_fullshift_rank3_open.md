# 497 $q=5$ 完整移位 $A$：rank-4 排除，rank-3 仍开放

> 2026-11-27。$n=6$、$C=e_6^{\mathsf T}$、$A$ 为完整移位（$e_1\mapsto\cdots\mapsto e_6\mapsto0$）、$E=e_4^*$、
> $L_0=[e_1;e_1]$。随机扫描 + 结构化构造。**rank-4 由特征值论证排除；rank-3 的 172 个构造点全部
> $(5b)$ 失败，但没有结构性 no-go**（ChatGPT 判定：rank-3 分支未解决）。

## 扫描

400 个随机 $L$（$5\times6$，$L_0$ 固定）：

| 量 | 数值 |
|---|---|
| $\operatorname{rank}H=4$ | 373（全部满足 $(5a)$） |
| $\operatorname{rank}H=3$ | 27（0 个满足 $(5a)$） |
| 可行 | **0** |

rank-4 全灭由 493 引理 A（$\omega=4$ 时 $Z$ 有特征值）解释。

## 结构化 rank-3 构造（497b）

取 $v=(0,a,b,c)$，$u=Pv$、$w=Qv$（$P$ 取 $L$ 的 1–4 列，$Q$ 取 2–5 列），令 $S$ 的行落在
$\operatorname{span}(u,w)^\perp$，则 $H=S P$、$H_A=S Q$ 自动满足 $Hv=H_Av=0$。
再要求 $\operatorname{rank}H=3$。

| 量 | 数值 |
|---|---|
| 构造出的 rank-3 且满足 $(5a)$ 的点 | **172** |
| 其中 $(5b)$ 成立 | **0** |

## ChatGPT 的判定

> **不能判定该 $A$ 在 $q=5$ 上根本不可行**；现有数据不足以推出结构性 no-go。
> - rank $H=4$：特征向量论证确实排除；
> - rank $H=3$：不能直接沿用——$Z$ 的特征向量未必落在 $\operatorname{im}H$；
> - $\operatorname{rank}H_A\le2$：没有证明；(5a) 未必迫使它。
>
> 最值得检验的结构量：$\operatorname{im}H\cap E_\mu(Z)$（$E_\mu(Z)=\ker(Z-\mu I)$，遍历复特征值）。
> 若某 $\mu$ 处交集非零，对应 pencil 必掉秩；若所有特征空间都与 $\operatorname{im}H$ 横截，
> 特征值论证就不能排除 rank-3 分支。

## 结论

- rank-4 分支：**排除**（$\omega=4$ 不可行）；
- rank-3 分支：**未解决**；172 个失败点只是搜索证据；
- 下一步：对构造出的 rank-3 点算 $Z$ 与 $\operatorname{im}H\cap E_\mu(Z)$，判断失败是否都由某个 $\mu$ 的横截失败解释；
  若是，则得到 rank-3 的谱判据；若否，说明还有别的机制。

## 状态

- rank-4：**[已证-纸面]**；
- rank-3：**[未解决]**（有 172 个失败点，无 no-go）。
