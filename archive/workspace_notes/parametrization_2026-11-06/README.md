# parametrization —— $\Phi_R$ 的参数化与不变量

> 目标（专家 Task 2）：把"选候选"从 $R\in\mathbb C^{(q-r)\times n}$ 降到更低维的对象，
> 或证明这样的降维不存在。

## 内容

| 文件 | 内容 |
|---|---|
| `attempts/01_phi_invariant.md` | 低维不变量的尝试：三条引理（双线性/构造集/有理依赖）、维数记账、为什么手算小例不可靠 |

## 现状

* 已证：$(5a)$ 的等价形式 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ 关于 $R$ 与 $(\Lambda,G_0,G_1)$ 分别线性；
  可容许集是构造集；$\Phi_R$ 的条目是 $R$ 的有理函数（详见 `proof/B.37/README.md`）。
* 未定：是否存在**规范**低维不变量。判定它需要可靠的实例生成（`tools/verification/consistency_checks.py`）。
