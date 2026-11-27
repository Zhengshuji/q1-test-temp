import Mathlib

/-! # 549 最小秩层例子的 Lean 核验

$q=3,k=2,n=4$、$r_2=r_3=0$ 的情形下，$(5b)$ 的公共根条件化简为
$\lambda^2=0$ 且 $r_3-r_1\lambda^2=0$。
本文件证明：若 $r_3\ne0$，则无公共根 ⇒ $(5b)$ 成立。
-/

namespace Q1Gadget549

/-- $r_3\ne0$ 时 $\lambda^2=0$ 与 $r_3-r_1\lambda^2=0$ 不能同时成立。 -/
theorem no_common_root (r1 r3 lam : ℚ) (hr : r3 ≠ 0)
    (h1 : lam ^ 2 = 0) (h2 : r3 - lam ^ 2 * r1 = 0) : False := by
  have hlam : lam ^ 2 = 0 := h1
  rw [hlam] at h2
  norm_num at h2
  exact hr h2

/-- 等价形式：$(5b)$ 在 $r_3\ne0$ 时成立。 -/
theorem gcd_one (r1 r3 lam : ℚ) (hr : r3 ≠ 0) :
    ¬ (lam ^ 2 = 0 ∧ r3 - lam ^ 2 * r1 = 0) := by
  rintro ⟨h1, h2⟩
  exact no_common_root r1 r3 lam hr h1 h2

end Q1Gadget549
