# $P$ 的 $O(n^4)$ 算法

> 由 `theorem.md` 的递归定理 + 终止性直接得到。

## 4. 算法与终止性

$$P=\sum_{k\ge0}\dim T_k,\qquad
(T_{k+1},C_{k+1},\Phi_{k+1})=\Big(\pi_k\Phi_k(T_k),\ \pi_k\Phi_k(T_k+C_k),\ \Phi_k\bmod M_k\Big)$$

每步 $\dim Y_{k+1}=\dim Y_k-\dim M_k\le\dim Y_k-\dim T_k$，故 $T_k\ne0$ 时至多 $n$ 步；每步 $O(n^3)$。

$$\Longrightarrow\quad O(n^4)$$

---

