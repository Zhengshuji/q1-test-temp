import Mathlib

/-! # 561 参数族 diag(a,b) 的核心矛盾（Lean）

设 $a\ne b$、$a\ne0$、$b\ne0$、$au\ne v$、$v\ne0$。
若 $m_{12}=(\lambda-a)(\lambda-b)=0$、$m_{13}=\lambda v(\lambda-a)=0$、$m_{23}=-(\lambda-b)(\lambda u-v)=0$，
则矛盾。
-/

namespace Q1Gadget561

theorem no_common_root (a b u v lam : ℚ)
    (hab : a ≠ b) (ha : a ≠ 0) (hb : b ≠ 0)
    (hauv : a * u ≠ v) (hv : v ≠ 0)
    (h12 : (lam - a) * (lam - b) = 0)
    (h13 : lam * v * (lam - a) = 0)
    (h23 : -((lam - b) * (lam * u - v)) = 0) : False := by
  have h12' : lam - a = 0 ∨ lam - b = 0 := mul_eq_zero.mp h12
  rcases h12' with h | h
  · have hl : lam = a := by linarith
    rw [hl] at h23
    have hzero : (a - b) * (a * u - v) = 0 := by linarith
    rcases mul_eq_zero.mp hzero with h1 | h2
    · exact hab (by linarith)
    · exact hauv (by linarith)
  · have hl : lam = b := by linarith
    rw [hl] at h13
    have hzero : b * v * (b - a) = 0 := by linarith
    rcases mul_eq_zero.mp hzero with h1 | h2
    · rcases mul_eq_zero.mp h1 with h1a | h1b
      · exact hb h1a
      · exact hv h1b
    · exact hab (by linarith)

end Q1Gadget561
