import Mathlib

/-! # 563 第二参数族（$AN=I$）核心矛盾的 Lean 核验

设 $a\ne b$、$a\ne1$、$b\ne1$、$u\ne0$、$v\ne0$。
若 $m_{12}=(\lambda-a)(\lambda-b)=0$、$m_{13}=(\lambda-a)(\lambda-1)v=0$、
$m_{23}=-(\lambda-b)(\lambda-1)u=0$，则矛盾。
-/

namespace Q1Gadget563

theorem no_common_root (a b u v lam : ℚ)
    (hab : a ≠ b) (ha1 : a ≠ 1) (hb1 : b ≠ 1)
    (hu : u ≠ 0) (hv : v ≠ 0)
    (h12 : (lam - a) * (lam - b) = 0)
    (h13 : (lam - a) * (lam - 1) * v = 0)
    (h23 : -((lam - b) * (lam - 1) * u) = 0) : False := by
  have h12' : lam - a = 0 ∨ lam - b = 0 := mul_eq_zero.mp h12
  rcases h12' with h | h
  · have hl : lam = a := by linarith
    rw [hl] at h23
    have hzero : (a - b) * (a - 1) * u = 0 := by linarith
    rcases mul_eq_zero.mp hzero with h1 | h2
    · rcases mul_eq_zero.mp h1 with h1a | h1b
      · exact hab (by linarith)
      · exact ha1 (by linarith)
    · exact hu h2
  · have hl : lam = b := by linarith
    rw [hl] at h13
    have hzero : (b - a) * (b - 1) * v = 0 := by linarith
    rcases mul_eq_zero.mp hzero with h1 | h2
    · rcases mul_eq_zero.mp h1 with h1a | h1b
      · exact hab (by linarith)
      · exact hb1 (by linarith)
    · exact hv h2

end Q1Gadget563
