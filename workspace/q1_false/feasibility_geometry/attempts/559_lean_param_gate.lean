import Mathlib

/-! # 559 参数化 520 例子：可行条件 $w=0\wedge v\ne0\wedge u\ne v$ 的核心矛盾

$w=0$ 时三个 $2\times2$ 子式为
$m_{12}=(\lambda-1)(\lambda-2)$、$m_{13}=\lambda v(\lambda-1)$、$m_{23}=-(\lambda-2)(\lambda u-v)$。
若 $v\ne0$、$u\ne v$ 且三者同时为零，则矛盾。
-/

namespace Q1Gadget559

theorem no_common_root (u v lam : ℚ) (huv : u ≠ v) (hv : v ≠ 0)
    (h12 : (lam - 1) * (lam - 2) = 0)
    (h13 : lam * v * (lam - 1) = 0)
    (h23 : -((lam - 2) * (lam * u - v)) = 0) : False := by
  have h12' : lam - 1 = 0 ∨ lam - 2 = 0 := mul_eq_zero.mp h12
  rcases h12' with h | h
  · have hl : lam = 1 := by linarith
    rw [hl] at h23
    have : u - v = 0 := by linarith
    exact huv (by linarith)
  · have hl : lam = 2 := by linarith
    rw [hl] at h13
    have : v = 0 := by linarith
    exact hv this

end Q1Gadget559
