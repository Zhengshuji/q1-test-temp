import Mathlib

/-! # 593 乘积等式 gadget 的行列式（Lean）

$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&1\end{bmatrix}$，则 $\det H=r_1r_2-z$。
-/

namespace Q1Gadget593

def det3 (a b c d e f g h i : ℚ) : ℚ :=
  a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

/-- $\det H=r_1r_2-z$。 -/
theorem det_H (r1 r2 z : ℚ) :
    det3 r1 z 0 1 r2 0 0 0 1 = r1 * r2 - z := by
  unfold det3
  ring

end Q1Gadget593
