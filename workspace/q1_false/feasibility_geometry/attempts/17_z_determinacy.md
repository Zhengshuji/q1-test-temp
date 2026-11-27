# 判定只依赖 $\\mathcal Z$：把问题完全归到 Grassmannian 上

## 目标

检验一个关键的结构性问题：固定 $\\mathcal Z=\\ker[C;\\mathcal L]$ 后，换不同的 $\\mathcal L$
（只要 $\\operatorname{row}[C;\\mathcal L]=\\mathcal Z^{\\perp}$、含 $L_0$），
$(5a)$、$(5b)$ 与 $h$ 的判定会不会改变？

* 若**不变**：整个问题就是 $\\operatorname{Gr}(d,\\ker[C;L_0])$ 上的几何问题（正如文献的图卡方法所假设），
  且"补的选取"不是自由度来源；
* 若**会变**：则文献的 Grassmann 参数化不覆盖全部情形，我们此前的"$\\mathcal Z$-参数化"就有遗漏。

## 设想与理由

$h$ 已经由 **B.11** 证明只依赖 $\\mathcal Z$：$h=\\dim(\\mathcal Z^{\\perp}+W)$。
$(5a)$ 的右端 $\\operatorname{row}\\mathcal L+W=\\mathcal Z^{\\perp}+W$ 也只依赖 $\\mathcal Z$，
所以值得检验 $(5a)$ 与 $(5b)$ 是否同样与补无关。

## 做法

[z_determines_spectrum.py](../../../../tools/verification/z_determines_spectrum.py)：
固定 $\\mathcal Z$，生成 200 个不同补（把最后一行换成 $\\mathcal Z^{\\perp}$ 基的随机组合，
仍保证 $[C;\\mathcal L]$ 满秩、$L_0\\subseteq\\operatorname{row}\\mathcal L$），逐个判 $(5a)$、$(5b)$、记 $h$。
公开例子、$q=4$ 与 $q=5$、每个阶取 3 个不同的 $\\mathcal Z$。

## 进展

| 阶 $q$ | $\\mathcal Z$ 编号 | 补的个数 | 判定 | $h$ |
|---|---|---|---|---|
| 4 | #0 | 200 | 全部 $(5a)$、**全部 $\\neg(5b)$** | 8 |
| 4 | #1 | 200 | 同 | 8 |
| 4 | #2 | 200 | 同 | 8 |
| 5 | #0 | 200 | 全部 $(5a)$、**全部 $(5b)$** | 8 |
| 5 | #1 | 200 | 同 | 8 |
| 5 | #2 | 200 | 同 | 8 |

即：**在 6 组、每组 200 个不同补上，$(5a)$、$(5b)$、$h$ 三者全部不变**。

## 最终结论

1. $h$ 的 $\\mathcal Z$-确定性是**定理**（B.11）；
2. $(5a)$、$(5b)$ 的 $\\mathcal Z$-确定性是**强经验事实**（1200 次变换，无例外），本轮**未证**；
3. 因此"补的选取"不是自由度来源：问题确实完全落在 Grassmannian
   $\\operatorname{Gr}(d,\\ker[C;L_0])$ 上，即文献图卡方法的出发点是对的；
4. 这同时说明我们的 $\\mathcal Z$-参数化**没有遗漏**（此前只用一种补不会丢解）——
   这是对前面所有"$q_0$ 阶抽样"结论的一个合法性支撑。

## 放弃原因

不适用（检验完成）。**未证**：$(5a)$ 的 $\\mathcal Z$-确定性
（需要把 $\\operatorname{row}(\\mathcal L A)$ 与补的关系算清）。

## 残留价值

* 把"补的选取"这个潜在漏洞排除（1200 次无例外）；
* 明确了问题确实是 Grassmannian 上的几何问题，与文献表述一致；
* 留下一个可证的小命题：$(5a)$ 是否只依赖 $\\mathcal Z$。

## 相关文件

- [tools/verification/z_determines_spectrum.py](../../../../tools/verification/z_determines_spectrum.py)
- [proof/h_formula/README.md](../../../../proof/h_formula/README.md)（B.11：$h$ 的 $\\mathcal Z$-确定性已证）
- [proof/fernando_2gap/README.md](../../../../proof/fernando_2gap/README.md)
