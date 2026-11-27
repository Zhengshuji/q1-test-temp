import Mathlib

/-! # 598 右铅笔乘积门的 $2\times2$ 行列式（Lean）

$P=H(\lambda I-Z')$ 的左上 $2\times2$ 块：
$\begin{bmatrix}\lambda r_1&(\lambda-1)z\\\lambda&(\lambda-1)r_2\end{bmatrix}$，
其行列式 $=\lambda(\lambda-1)(r_1r_2-z)$。
-/

namespace Q1Gadget598

theorem det2_P (r1 r2 z lam : ℚ) :
    (lam * r1) * ((lam - 1) * r2) - (lam * (lam - 1) * z)
      = lam * (lam - 1) * (r1 * r2 - z) := by
  ring

end Q1Gadget598
