# feasibility_geometry · 成果

> 阶段基线：attempts 677–755（2026-11-27）。等级：Lean / 已证-纸面 / 精确验证。

| 成果 | 等级 | 位置 |
|---|---|---|
| 引理 S：$(5b)\iff\gcd(\text{全部 }d'\text{-子式})=1$ | 已证-纸面 | 677 |
| $d=2$ 定理 | 已证-纸面 | 674 |
| $q=r_0$ 时多项式时间判定 | 已证-纸面 | 679 |
| $T=\{lW:lN=0\}$ 与相容性 $UZ'\subseteq U+T$ | 已证-纸面 | 692/697/755 |
| $d'=1$：可行 ⇒ $U\subseteq T$ | 已证-纸面 | 715 |
| $a\ge1$、$g_\mu\le a$、$d'\le\operatorname{rank}(HM)+\dim E_H$ | 已证-纸面 | 725/726/734 |
| $\dim E_H=\dim(U\cap T)+\operatorname{cls}$（可行时等式） | 已证-纸面 | 737/739/743 |
| $\rho_{d'}=1$ ⇒ 不可行 | 已证-纸面 | 705 |
| 638 正秩不可行 | 已证-纸面 | 707–710 |
| 733：$d'=2>s=t=1$ 可行（$\omega>s$） | 已证+精确+子 agent | 733 |
| 747：$B=Z'_{12}$ 判别（625 例） | 精确验证+符号 | 747 |
| 749 被 695 支配（任意 $k,d',t,H$） | 已证-纸面 | 753 |
| Lean 内核：$rank(f-g)\le rank f+rank g$ 等 | Lean | 740–742 |
| 精确对照脚本（638 vs 733） | 精确验证 | `certificates/verify_prefilter_733_638.py` |
| 747 恒等式符号验证 | 符号验证 | `certificates/verify_747_identities.py` |

**已撤回**：$q_{\min}=\dim V+1$；闭包+1；“$q_0$ 阶总是薄”；638 的 $\omega>s$ 证书；661 的“实例级不可行”；631 的“$W$ 满行秩 ⇒ 可行”（需 $T=S$）。

**最大缺口**：$\exists H$（$\exists G\in T^q$ 使 $\gcd=1$）的复杂度；695+705 的完备性未证；$d'<k$ 的结构理论。
