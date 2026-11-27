import Mathlib

/-! # 557 非平凡 $(5a)$ 例子：pencil 行列式的 Lean 核验

$H=[e_1;e_2;r]$、$H_A=[[1,0,1],[0,1,0],[r_1,r_2,r_1]]$、$r=(r_1,r_2,r_3)$。
则 $\det P(\lambda)=\lambda(\lambda-1)^2 r_3$——与 $r_1,r_2$ 无关。
-/

namespace Q1Gadget557

def det3 (a b c d e f g h i : ℚ) : ℚ :=
  a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

/-- $\det P(\lambda)=\lambda(\lambda-1)^2 r_3$。 -/
theorem det_P (r1 r2 r3 lam : ℚ) :
    det3 (lam - 1) 0 (-1)
         0 (lam - 1) 0
         ((lam - 1) * r1) ((lam - 1) * r2) (lam * r3 - r1)
      = lam * (lam - 1) ^ 2 * r3 := by
  unfold det3
  ring

/-- 推论：$r_3\ne0$ 时 $\lambda=0$ 是根。 -/
theorem det_at_zero (r1 r2 r3 : ℚ) :
    det3 (-1) 0 (-1) 0 (-1) 0 (-r1) (-r2) (-r1) = 0 := by
  unfold det3
  ring

end Q1Gadget557
