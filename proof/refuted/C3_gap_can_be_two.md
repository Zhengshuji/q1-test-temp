# C3 —— "$q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$"被公开例子推翻（2026-11-02）

## 被推翻的陈述

**C3**（本项目 2026-11-02 晚的经验陈述）：在功能可观测实例上
$$q_{\min}\in\{\mathrm{cl},\ \mathrm{cl}+1\},$$
其中 $\mathrm{cl}$ 是 $(5a)$ 下的最小维数。

## 反例（文献，已在本项目复现）

Fernando 2026（arXiv:2609.37992）§VII 的例子：$n=8$、$p=r=2$、$\eta=(2,1)$，故 $q_0=3$；
而最小功能观测器阶为
$$\nu_{\min}=5=q_0+2 .$$
论文用**全部 Grassmann 图卡**证明 $q=3$ 与 $q=4$ 的代数可行族全部谱不可行，并给出显式的 order-5 实现。

本项目复现结果（[proof/fernando_2gap](../fernando_2gap/README.md)）：

* $\mathcal L_5$ 精确核验：$(5a)$、$(5b)$ 成立，$h=8$、$s=5$、$r_1=4$、$\varepsilon=[5]$、$d_{\rm fin}=0$；
* $q=4$ 抽样 20 个代数可行的增广：$(5b)$ 成立 **0** 个；
* $q=5$ 抽样 40 个：$(5b)$ 成立 **40** 个。

⟹ 差可以达到 **2**。C3 是错的。

## 顺带的第二个更正

同一次复现暴露：本项目的"闭包"（贪心加入 $xA$）在该例上给出 4，而真正的最小维数是 3。
所以**闭包不是精确最小维数**（专家 §8.1 已提醒），权威量是功能指标算法的 $q_0=\sum_j\eta_j$。
这条记在 [ferrando_2gap](../fernando_2gap/README.md) 与本目录的 README。

## 幸存的（文献给出的）界

$$\boxed{\ q_0=\mathrm{cl}=\sum_j\eta_j\ \le\ q_{\min}\le\ n_0-p\ }$$

上端点在功能可观测下**保证可行**；中间可以有间隔（本例间隔 2）。

## 相关

- [proof/fernando_2gap](../fernando_2gap/README.md)（复现与证书）
- [C1](C1_closure_plus_one.md)（更早被推翻的 $q_{\min}=\mathrm{cl}+1$）
