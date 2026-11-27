import Mathlib

/-! # 594 改进的乘积等式 gadget（Lean）

$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&1\end{bmatrix}$，$Z=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$（幂零 Jordan）。
- $\det H=r_1r_2-z$；
- $\det(\lambda I-Z)=\lambda^3$。
-/

namespace Q1Gadget594

def det3 (a b c d e f g h i : ℚ) : ℚ :=
  a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

theorem det_H (r1 r2 z : ℚ) :
    det3 r1 z 0 1 r2 0 0 0 1 = r1 * r2 - z := by
  unfold det3
  ring

theorem det_lambdaI_sub_Z (lam : ℚ) :
    det3 lam (-1) 0 0 lam (-1) 0 0 lam = lam ^ 3 := by
  unfold det3
  ring

end Q1Gadget594
