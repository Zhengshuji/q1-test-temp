import Mathlib

/-! # 591 乘积不等式 gadget 的 Lean 核验

$H=\begin{bmatrix}0&0&0\\r_1&1&0\\z&r_2&0\end{bmatrix}$、$Z=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$、$H_A=ZH$、$P=\lambda H-H_A$。
- $\det P\equiv0$（三行第三坐标全零）；
- $\lambda=0$ 时 $2\times2$ 子式 $=r_1r_2-z$。
-/

namespace Q1Gadget591

def det3 (a b c d e f g h i : ℚ) : ℚ :=
  a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

/-- 三行第三坐标为零 ⇒ $\det P=0$。 -/
theorem det_P_zero (r1 r2 z lam : ℚ) :
    det3 (-r1) (-1) 0
         (lam * r1 - z) (lam - r2) 0
         0 0 0 = 0 := by
  unfold det3
  ring

/-- $\lambda=0$ 的 $2\times2$ 子式 $=r_1r_2-z$。 -/
theorem minor_zero (r1 r2 z : ℚ) :
    (-r1) * (-r2) - (-1) * (-z) = r1 * r2 - z := by
  ring

end Q1Gadget591
