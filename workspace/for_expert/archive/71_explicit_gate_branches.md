# An explicit multiplication gate in (5a), and the branch problem

This note reports an explicit observer instance whose \((5a)\) condition is exactly the rank-one gate \(ad=bc\), with \((5b)\) automatic. The remaining problem is soundness: the rank-one variety has a branch that does not decode to \(z=xy\).

## Part I. The instance

Let \(n=5\), \(p=1\), \(q=2\),
\[
A=\begin{bmatrix}
1&1&-1&0&1\\
-1&0&0&-1&1\\
0&1&-1&0&1\\
0&0&0&-1&0\\
-1&1&0&0&0
\end{bmatrix},\qquad
C=e_5^*,\qquad L_0=e_1^*,\qquad L=\begin{bmatrix}e_1^*\\ l\end{bmatrix},
\]
with \(l=(a,b,c,d,e)\).

## Part II. \((5a)\) is exactly the rank-one gate

Let \(M=[lA;L_0;l;CA;C]\) (a \(5\times5\) matrix) and \(M_0=[L_0;l;CA;C]\). Direct exact computation gives
\[
\det M=ad-bc.
\]
Since \(\operatorname{rank}M_0=4\) generically, \((5a)\) is equivalent to
\[
\boxed{ad=bc,}
\]
i.e. the block \(\begin{bmatrix}a&b\\c&d\end{bmatrix}\) has rank at most one.

On the chart \(l=(1,x,y,z,0)\), this is
\[
\det M=z-xy,\qquad (5a)\iff z=xy.
\]

## Part III. \((5b)\) is automatic

Let \(N=\ker[C;CA]\) (\(5\times3\)), \(H=LN\), \(H_A=LAN\), \(P(\lambda)=\lambda H-H_A\). The three \(2\times2\) minors of \(P\) have gcd
\[
\gcd=1
\]
as polynomials in \(\lambda\) over \(\mathbb Q(a,b,c,d,e)\). Hence \((5b)\) holds for **every** \(L\), without any additional guard.

On the chart \(l=(1,x,y,z,0)\), the row-independence condition also holds: \(\operatorname{rank}[C;L]=3=p+q\).

## Part IV. The branch problem

The feasible set is \(\{ad=bc\}\), a rank-one variety with several components:
- if \(a\ne0\), then \(x=b/a\), \(y=c\), \(z=d\) give \(z=xy\);
- if \(a=0\), then \(bc=0\): the branches \(a=b=0\) (with \(c,d\) free) and \(a=c=0\) (with \(b,d\) free).

The \(a=0\) branches satisfy \((5a)(5b)\) but do not decode to \(z=xy\). For example, \(l=(0,1,0,0,0)\) is feasible with \(\operatorname{rank}H=1\). These are spurious witnesses.

## Part V. Questions

**Question 1.** How can the \(a=0\) components be eliminated by observer conditions? We would like a fixed pivot that forces the anchor \(a\) to be nonzero (or replaces \(a\) by a fixed \(1\)), without destroying \((5b)\).

**Question 2.** Is there an anchored version in which the \((1,1)\) entry of the gate is a fixed \(1\) coming from \(L_0\) or \(C\), so that the determinant is \(z-xy\) for all feasible \(L\) (no division by \(a\))?

**Question 3.** The spurious branches have \(\operatorname{rank}H=1\), while the intended gate chart has \(\operatorname{rank}H=2\). Can the instance be modified so that \(\operatorname{rank}H=2\) is forced (for example by a second fixed row), while keeping \((5b)\) automatic?

**Question 4.** If the branches can be removed, does this one-gate instance give a sound reduction for one multiplication, and is the next step variable sharing/circuit composition?

## Part V-bis. What we tried for the branch

- An anchored search for \(\det=d-bc\) (fixed \(1\)) over 600 random \(A\) (and 500 more with varied \(L_0,C\)) found no example.
- Forcing \(a\ne0\) by \(p=3\) with \(\operatorname{rank}[C;L]=p+q\): in \(n=5\), this makes \([L;CA;C]\) full rank, so \((5a)\) becomes automatic and the gate disappears.
- Hence the branch needs a larger dimension or a different anchor.

## Part VI. What is verified

- \(\det M=ad-bc\): exact symbolic computation.
- \((5b)\) for all \(L\): gcd of the maximal minors is \(1\) (symbolic).
- The chart \(l=(1,x,y,z,0)\) satisfies the row-independence convention and gives \(z=xy\).
- The \(a=0\) branch is a genuine spurious witness, not an artifact of the chart.
