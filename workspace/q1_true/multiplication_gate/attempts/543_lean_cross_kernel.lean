import Mathlib

/-! # 542 非线性接口：叉积核向量的 Lean 核验

对 $u=(u_1,u_2,u_3)$、$v=(v_1,v_2,v_3)$，令
$w=u\times v=(u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1)$。
则 $u\cdot w=0$、$v\cdot w=0$（三重积恒等式）——即 $w\in\ker[u;v]$。
-/

namespace Q1Gadget542

/-- 叉积的第一分量。 -/
def w1 (u1 u2 u3 v1 v2 v3 : ℚ) : ℚ := u2 * v3 - u3 * v2
/-- 第二分量。 -/
def w2 (u1 u2 u3 v1 v2 v3 : ℚ) : ℚ := u3 * v1 - u1 * v3
/-- 第三分量。 -/
def w3 (u1 u2 u3 v1 v2 v3 : ℚ) : ℚ := u1 * v2 - u2 * v1

/-- $u\cdot(u\times v)=0$。 -/
theorem dot_u_cross (u1 u2 u3 v1 v2 v3 : ℚ) :
    u1 * w1 u1 u2 u3 v1 v2 v3 + u2 * w2 u1 u2 u3 v1 v2 v3
      + u3 * w3 u1 u2 u3 v1 v2 v3 = 0 := by
  unfold w1 w2 w3
  ring

/-- $v\cdot(u\times v)=0$。 -/
theorem dot_v_cross (u1 u2 u3 v1 v2 v3 : ℚ) :
    v1 * w1 u1 u2 u3 v1 v2 v3 + v2 * w2 u1 u2 u3 v1 v2 v3
      + v3 * w3 u1 u2 u3 v1 v2 v3 = 0 := by
  unfold w1 w2 w3
  ring

/-- $e_1\cdot(u\times v)=\det[e_1;u;v]$。 -/
theorem e1_dot_cross (u1 u2 u3 v1 v2 v3 : ℚ) :
    w1 u1 u2 u3 v1 v2 v3 = u2 * v3 - u3 * v2 := by
  unfold w1
  ring

end Q1Gadget542
