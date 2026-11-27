# review_2026-11-01 —— 接手方的核对（HANDOVER2 的证据）

> **用途**：存放 HANDOVER2 与专家报告引用的**可复现核对**。前三个脚本核对文档/代码；
> `check_qmin5.py` 是一个**反例证书**，推翻了内部文档的 $q_{\min}=5$（见下第 4 条）。
> **作者**：2026-11-01 接手方。**等级**：精确验证（有理算术），不是证明。

## 内容

| 文件 | 作用 |
|---|---|
| `check_handover2.py` | 三组核对：① §40.1 / §41.8 的维数等式；② c300 的 58 个 (实例,S) 的适用域统计；③ `coeff_forms_of_S` 与 §41 全行版 `a_j` 的对比 |
| `check_qmin5.py` | **第二实例无解的证书**：$e_1,\dots,e_4$ 是 $V$ 中的 1-特征向量 ⟹ 任意 $\mathcal L$ 在 $\lambda=1$ 处 $(5b)$ 秩降；附 $\gcd=(x-1)^4$ 与 rank-barrier 数值 |

## 四组结论（详见脚本输出）

1. **§40.1 的 `r+t = w-q` 是错的**：c282 上 `r+t=4`、`w-q=2`；正确的恒等式是 `r+t = w-q+v-2s`。
   `(r+t=w-s) ⟺ (q=t)` 与 `r ≤ p` 仍成立，但 **`r = w-v` 也是错的**（c282：1 vs 2）。
2. **支5 的 58 个 (实例,S) 全部 `q≠t`**（58/58；`h=w` 的 0 个）。它们都在 `m=r+t` 的
   §33 域里，不在 §40 的方阵域（`q=t`）里。
3. **`coeff_of_S.coeff_forms_of_S` 不是 §41 的对象**：第二实例 `q=2,s=2` 上它返回 2 个 `a_j`
   （长度 2，只用一个 P 列），§41 的全行版是 3 个 `a_j`（长度 3）；前者在随机 `u` 上恒为 0，
   后者非零。该函数在 `r+t≠m` 时没有断言，静默算的是另一个对象。
4. **第二实例无解（$q_{\min}=\infty$）**：$V=\operatorname{span}(e_1..e_4)$ 中的 4 个 1-特征向量
   被 $C,CA,L(I-A)$ 同时消灭，故对**任意** $\mathcal L$ 在 $\lambda=1$ 有
   $\operatorname{rank}[\mathcal L-\mathcal LA;CA;C]\le2<3\le\operatorname{rank}[\mathcal L;CA;C]$。
   内部文档的 $q_{\min}=5$ 由此撤回；专家报告 §4 有完整论证。

## 复现

```bash
python workspace/review_2026-11-01/check_handover2.py
python workspace/review_2026-11-01/check_qmin5.py
```

## 未覆盖

- 没有读 A2 全文（1088 行），只读 §25、§32–§41；
- 没有复核 RCP 全文、`rho1_layer` 的 423/423、T11 的 195/195；
- 58 例的统计依赖 `c300_g3_check.py` 的随机种子（20261101）与 `h-v≥2` 过滤。
