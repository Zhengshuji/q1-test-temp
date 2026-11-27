# **Mathematical analysis of Report 105: The active-subspace test**

**Report:** `105_active_subspace_tests.md`

## **1. Overall assessment**

This report represents a substantial improvement in the mathematical formulation of the project. More importantly, it identifies a question that is considerably more precise than the previous general question about the expressive power of the compressed observer architecture:

> What is the geometric and algebraic structure of the set of active subspaces \\(W\\), particularly the dependence of the generic spectral-feasibility condition on \\(W\\)?

I consider this the right question to investigate next.

The report has three particularly important achievements:

1\. It replaces the original free-row search by a problem involving the Grassmannian and the intersection\
\\[\
\mathcal T_W=\mathcal S\cap(W\oplus W).\
\\]

2\. It correctly identifies the spectral condition as a coprimality condition on the maximal minors of a matrix pencil, rather than a condition involving higher-order minors.

3\. It recognizes that the possible discrete information in the problem may be associated with the topology or algebraic geometry of the active-subspace set, rather than polynomial relations among free rows.

However, I think several important mathematical issues remain unresolved, and one can make more progress than the report currently suggests.

My principal conclusions are:

| Question                                                  | My conclusion                                                                                                                                                      |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Q1: Type of spectral test as a function of \\(W\\)        | Open on the entire compatibility locus; provably open on constant-rank strata. Global openness requires an additional argument.                                    |
| Q2: Can component indices encode Boolean assignments?     | Potentially yes for real topological components, but not automatically. Zariski connectedness and Euclidean connectedness must be distinguished.                   |
| Q3: Can the active set have exactly \\(2^s\\) components? | Possible in principle under real-topological interpretation, but the proposed product-of-projective-lines construction needs a more careful geometric realization. |
| Q4: Is the top layer the natural reduction target?        | It is a useful separate direction, but it eliminates the Grassmannian choice and does not automatically eliminate all existential expressive power.                |
| Q5: What computation is decisive?                         | Exact symbolic analysis of the generic pencil over the function field of \\(\mathcal T_W\\), followed by elimination in Grassmannian coordinates.                  |

There is also an important structural observation that I believe should become an explicit theorem in the next version:

**The compatibility locus determined by the fixed rows is always a single Grassmannian, not an arbitrary collection of components.**

This substantially sharpens Q1–Q3.

I will develop these points in detail.

# **Part I. Reconstructing the mathematical structure**

## **2. The compressed model**

We start with

\\[ A\in\mathbb Q^{n\times n},\qquad C\in\mathbb Q^{p\times n},\qquad L_0\in\mathbb Q^{r_0\times n}, \\]

and

\\[ \mathcal L= \begin{bmatrix} L_0\\\R \end{bmatrix}, \qquad R\in\mathbb F^{m\times n}. \\]

Let

\\[ K_0=\ker \begin{bmatrix} C\\\CA \end{bmatrix}, \qquad k=\dim K_0, \\]

and let \\(N\in\mathbb F^{n\times k}\\) be a basis matrix of \\(K_0\\).

The compressed matrices are

\\[ H=\mathcal LN,\qquad H_A=\mathcal LAN. \\]

The feasibility conditions are

\\[ \operatorname{row}H_A\subseteq\operatorname{row}H, \tag{1} \\]

and

\\[ \operatorname{rank}(\lambda H-H_A)=\omega \qquad\forall\lambda\in\mathbb C, \tag{2} \\]

where

\\[ \omega=\operatorname{rank}H. \\]

The kernel lemma gives

\\[ \ker H=\ker H_A. \\]

Consequently,

\\[ \operatorname{row}H=\operatorname{row}H_A. \\]

Thus there is an \\(\omega\\)-dimensional subspace

\\[ W\subseteq\mathbb F^{1\times k} \\]

such that

\\[ \operatorname{row}H = \operatorname{row}H_A = W. \\]

This is the fundamental geometric reduction.

## **3. The linear space controlling free-row choices**

For an arbitrary row \\(r\in\mathbb F^{1\times n}\\), define

\\[ \Phi(r)=(rN,rAN). \\]

Its image is

\\[ \mathcal S = \operatorname{im}\Phi = \operatorname{row}[N\ AN] \subseteq V\oplus V, \\]

where

\\[ V=\mathbb F^{1\times k}. \\]

For a candidate \\(W\in\operatorname{Gr}(\omega,k)\\), define

\\[ \mathcal T_W = \mathcal S\cap(W\oplus W). \\]

The free rows that belong to the fibre associated with \\(W\\) are precisely the preimages of \\(\mathcal T_W\\) under \\(\Phi\\).

Write

\\[ h_i^0=(L_0)\_iN,\qquad g_i^0=(L_0)\_iAN. \\]

The three tests in the report are:

**Compatibility**

\\[ h_i^0,g_i^0\in W \qquad\forall i. \tag{3} \\]

**Rank completion**

\\[ \operatorname{span} \left( \\{h_i^0\\}\_{i=1}^{r_0} \cup\pi_1(\mathcal T_W) \right)=W, \tag{4} \\]

with enough free rows.

**Generic spectral feasibility**

The generic pencil constructed from the fixed pairs and generic elements of \\(\mathcal T_W\\) has maximal minors with greatest common divisor one.

The report proposes that feasibility is equivalent to the existence of a \\(W\\) satisfying these three conditions.&#x20;

105_active_subspace_tests.md



I agree with this formulation, subject to making the generic-pencil condition and its field convention precise.

In particular, the third test is not an independent arbitrary existential condition on free rows. Its meaning is that a nonempty open set of admissible free-row choices is spectrally feasible.

That observation is the starting point for the rest of the analysis.

# **Part II. A structural theorem that should be added**

## **4. The compatibility locus is a Grassmannian**

This is, in my opinion, the most useful immediate deduction from the report.

Define the fixed-row span

\\[ U= \operatorname{span} \\{h_1^0,\ldots,h\_{r_0}^0, g_1^0,\ldots,g\_{r_0}^0\\} \subseteq V. \\]

Let

\\[ d=\dim U. \\]

The compatibility condition says exactly that

\\[ U\subseteq W. \\]

Therefore the set of compatible \\(W\\)'s is

\\[ \mathcal X\_{\mathrm{comp}} = \\{W\in\operatorname{Gr}(\omega,k):U\subseteq W\\}. \\]

Every such \\(W\\) corresponds uniquely to an \\((\omega-d)\\)-dimensional subspace of \\(V/U\\).

Consequently,

\\[ \boxed{ \mathcal X\_{\mathrm{comp}} \cong \operatorname{Gr}(\omega-d,k-d). } \tag{5} \\]

This holds whenever

\\[ d\leq\omega\leq k. \\]

If \\(d>\omega\\), the compatibility locus is empty.

### **4.1 Consequences**

Equation (5) immediately establishes several structural facts.

**Case 1:&#x20;**\\(d=\omega\\)**.**

Then

\\[ \operatorname{Gr}(0,k-\omega) \\]

is a single point.

The active subspace is uniquely determined by the fixed rows:

\\[ W=U. \\]

This is the pinned case described in the report.

**Case 2:&#x20;**\\(d<\omega\\)**.**

The compatibility locus has positive dimension:

\\[ \dim\mathcal X\_{\mathrm{comp}} = (\omega-d)(k-\omega). \tag{6} \\]

**Case 3:&#x20;**\\(d=0\\)**.**

There are no nonzero fixed compressed rows, and the compatibility locus is the entire Grassmannian:

\\[ \mathcal X\_{\mathrm{comp}}=\operatorname{Gr}(\omega,k). \\]

### **4.2 A particularly important consequence for Q3**

The compatibility locus is irreducible over an algebraically closed field.

It is not naturally a product of independent projective lines merely because the source problem has several Boolean variables.

For example,

\\[ \operatorname{Gr}(2,3)\cong\mathbb P^2, \\]

which is irreducible.

Similarly,

\\[ \operatorname{Gr}(1,2)\cong\mathbb P^1. \\]

This gives an immediate restriction on any proposed component-based reduction.

If the spectral-feasibility locus is Zariski open in the compatibility locus, then a nonempty active set is also irreducible in the Zariski topology.

Therefore it cannot have \\(2^s\\) distinct algebraic connected components.

This does not rule out \\(2^s\\) real topological connected components. That distinction is essential and will be developed below.

I recommend adding (5) and (6) to the report as a proved structural result.

# **Part III. Q1 — Is the generic spectral test open as a function of&#x20;**\\(W\\)**?**

## **5. First distinguish two different openness questions**

There are two different spaces involved.

For a fixed \\(W\\), the admissible free-row choices form a linear space.

As \\(W\\) varies, these linear spaces themselves vary.

The first openness statement is relatively straightforward. The second is more delicate.

Let

\\[ \mathcal X=\mathcal X\_{\mathrm{comp}}. \\]

Define the incidence space

\\[ \mathcal E = \\{(W,z):W\in\mathcal X,\ z\in\mathcal T_W^m\\}. \\]

Here \\(z\\) represents the collection of \\(m\\) admissible compressed free-row pairs.

Let

\\[ \pi:\mathcal E\to\mathcal X \\]

be the projection.

The fibre is

\\[ \pi^{-1}(W)=\mathcal T_W^m. \\]

The third test asks whether the fibre contains a spectrally regular choice, equivalently whether its generic choice is spectrally regular.

The central question is whether the set

\\[ \mathcal X\_{\mathrm{reg}} = \\{W\in\mathcal X: \text{the generic admissible pencil is spectrally regular}\\} \tag{7} \\]

is open.

## **6. For a fixed&#x20;**\\(W\\)**, spectral regularity is open**

This part can be established rigorously.

Suppose \\(W\\) is fixed and choose coordinates on

\\[ \mathcal T_W^m. \\]

Let

\\[ z=(z_1,\ldots,z_D) \\]

be the corresponding affine parameters.

The pencil becomes

\\[ P_W(\lambda,z) = \lambda H_W(z)-H\_{A,W}(z). \\]

Because every row of the pencil belongs to \\(W\\),

\\[ \operatorname{rank}P_W(\lambda,z)\leq\omega. \\]

Let

\\[ m_1(\lambda,z),\ldots,m_s(\lambda,z) \\]

denote its \\(\omega\times\omega\\) minors.

The spectral condition is

\\[ \gcd\_{\mathbb C[\lambda]} (m_1(\lambda,z),\ldots,m_s(\lambda,z))=1. \tag{8} \\]

Equivalently, there is no

\\[ [\lambda_0:\lambda_1]\in\mathbb P^1(\mathbb C) \\]

at which all the homogenized maximal minors vanish.

Define the bad incidence set

\\[ \mathcal B_W = \left\\{ (z,[\lambda_0:\lambda_1]): \widetilde m_j(\lambda_0,\lambda_1,z)=0 \ \forall j \right\\}. \\]

It is algebraically closed in

\\[ \mathcal T_W^m\times\mathbb P^1. \\]

Since \\(\mathbb P^1\\) is projective, projection onto the parameter space is closed.

Thus the bad parameter set

\\[ \operatorname{Bad}\_W = \\{z:\exists\lambda,\ \operatorname{rank}P_W(\lambda,z)<\omega\\} \\]

is Zariski closed.

Therefore the spectrally regular set

\\[ \mathcal G_W = \mathcal T_W^m\setminus\operatorname{Bad}\_W \\]

is Zariski open.

Combining this with the rank-completion condition, which is also open, gives:

\\[ \boxed{ \text{For fixed }W,\text{ feasible free-row choices form a Zariski-open subset of }\mathcal T_W^m. } \tag{9} \\]

If nonempty, this set is dense because \\(\mathcal T_W^m\\) is an irreducible affine space.

This validates the fixed-fibre argument.

## **7. The difficult question: does openness survive when&#x20;**\\(W\\)**&#x20;varies?**

Here I would be more cautious than the report.

The spaces

\\[ \mathcal T_W=\mathcal S\cap(W\oplus W) \\]

need not have constant dimension as \\(W\\) varies.

Indeed, consider the linear map

\\[ \Psi_W: \mathcal S\longrightarrow (V/W)\oplus(V/W), \\]

defined by

\\[ \Psi_W(x,y)=(x+W,y+W). \\]

Then

\\[ \mathcal T_W=\ker\Psi_W. \\]

Hence

\\[ \dim\mathcal T_W = \dim\mathcal S-\operatorname{rank}\Psi_W. \tag{10} \\]

As \\(W\\) varies, the rank of this map may jump.

The condition

\\[ \operatorname{rank}\Psi_W\leq q \\]

is determinantal and therefore closed.

Thus \\(\dim\mathcal T_W\\) is upper semicontinuous, not necessarily constant.

### **7.1 Constant-rank strata**

Stratify the compatibility locus according to

\\[ \operatorname{rank}\Psi_W=q. \\]

On each locally closed constant-rank stratum \\(X_q\\), the spaces \\(\mathcal T_W\\) form a vector bundle.

Consequently,

\\[ \mathcal E|\_{X_q}\to X_q \\]

is a vector-bundle projection.

Now consider the open subset

\\[ \mathcal G\subseteq\mathcal E \\]

on which the generic pencil is spectrally regular and the rank-completion condition holds.

Since vector-bundle projections are open, the image

\\[ \pi(\mathcal G|\_{X_q}) \\]

is open in \\(X_q\\).

Therefore:

Proved on constant-rank strata

\\[ \boxed{ \mathcal X\_{\mathrm{reg}}\cap X_q \text{ is open in }X_q. } \tag{11} \\]

This is already a useful theorem.

### **7.2 Why this does not settle global openness**

The global incidence space may not be a vector bundle.

A simple general algebraic-geometric example illustrates the issue. Consider

\\[ E=\\{(t,z)\in\mathbb A^2:tz=0\\} \\]

with projection onto \\(t\\).

The fibre has dimension zero for \\(t\ne0\\), but dimension one for \\(t=0\\).

The projection is not open: the open subset

\\[ E\setminus\\{(0,0)\\} \\]

has image only \\(\\{0\\}\\).

This example is not a counterexample to the observer architecture. It demonstrates why a varying-dimensional kernel incidence cannot automatically be treated as a vector bundle.

For our problem, one must determine whether the special form

\\[ \mathcal T_W=\mathcal S\cap(W\oplus W) \\]

and the structure of the spectral test eliminate this obstruction.

I do not think the report currently establishes that.

### **7.3 My answer to Q1**

The mathematically justified conclusion is:

1. For every fixed \\(W\\), spectral feasibility is open in its admissible parameter space.
2. On every constant-rank stratum of the map \\(\Psi_W\\), the active-subspace condition is relatively open.
3. Globally, the active set is constructible, but openness has not yet been proved.
4. Closedness is also not established.
5. It is therefore premature to conclude that the global active set is either open, closed, or neither.

I would make proving or disproving global openness the first priority.

# **Part IV. Q2 — Can the component index encode a Boolean assignment?**

## **8. First distinguish three notions of connectedness**

This question is potentially very important for the NP-hardness programme, but it is also where the report needs the greatest conceptual precision.

There are three different notions of components that could be relevant:

1. Zariski connected components over an algebraically closed field;
2. connected components of the real algebraic set in the Euclidean topology;
3. connected components of the real semialgebraic active set.

These notions are not equivalent.

In particular, a nonempty Zariski-open subset of an irreducible algebraic variety is irreducible. It cannot split into several Zariski connected components.

But its real points can have multiple Euclidean connected components.

This distinction changes the answer to Q2.

## **9. Algebraic components cannot provide the proposed Boolean encoding**

Suppose that the result of Q1 is positive: the active set is Zariski open in the compatibility locus.

From (5),

\\[ \mathcal X\_{\mathrm{comp}} \cong \operatorname{Gr}(\omega-d,k-d). \\]

The Grassmannian is irreducible.

Therefore, if the active set is nonempty,

\\[ \mathcal X\_{\mathrm{act}} \subseteq\mathcal X\_{\mathrm{comp}} \\]

is a nonempty Zariski-open subset of an irreducible variety.

Hence it is irreducible.

Thus

\\[ \boxed{ \\#\\{\text{Zariski connected components of }\mathcal X\_{\mathrm{act}}\\}=1 } \\]

whenever the active set is nonempty.

Consequently, the component index cannot encode a Boolean assignment if component means algebraic connected component.

This is a strong negative result for one interpretation of Q2.

## **10. Real topological components are different**

Now consider the real setting.

A real algebraic variety can be irreducible over \\(\mathbb C\\) while its real locus has several Euclidean connected components after removing an algebraic subset.

The simplest example is

\\[ \mathbb P^1(\mathbb R). \\]

Topologically,

\\[ \mathbb P^1(\mathbb R)\cong S^1. \\]

Remove two distinct points:

\\[ X=\mathbb P^1(\mathbb R)\setminus\\{P_0,P_1\\}. \\]

Then

\\[ X \\]

has exactly two connected components.

[Real Projective Line - Circle Clipart (#5168891) - PikPng](https://images.openai.com/static-rsc-4/5ogcRKj2N4S1P3KsArnAiogf7X0BQDqyqzRcysSoMN1TMBRsIo6bqV3Gq2IN-PY4dtQUmBPHYb0aBOCkZBZnEuKxDkSXmi09dmbF1a5Np1BMOTsi1GgfXNa3kFKyTlbhxtlgCFhA56xp0Ttgh5Qx1RkxM6nhBw-Ale2FAZG1cdQ?purpose=inline)

Over \\(\mathbb C\\), however,

\\[ \mathbb P^1(\mathbb C)\setminus\\{P_0,P_1\\} \\]

is still connected and irreducible.

Thus a Zariski-open active set can have multiple real topological components.

This gives a possible route to Boolean encoding.

### **10.1 The proposed encoding mechanism**

Suppose one could construct an active set whose real points have exactly

\\[ 2^s \\]

connected components:

\\[ \mathcal X\_{\mathrm{act}}(\mathbb R) = X_1\sqcup\cdots\sqcup X\_{2^s}. \\]

Suppose further that each component has a label

\\[ \beta(X_j)\in\\{0,1\\}^s. \\]

Then the component label could represent a Boolean assignment.

For example, if the compatibility space were a product

\\[ (\mathbb P^1(\mathbb R))^s \\]

and the spectral test removed two points in each projective-line coordinate, the resulting space could be

\\[ \left( \mathbb P^1(\mathbb R)\setminus\\{P_0,P_1\\} \right)^s. \\]

It would have

\\[ 2^s \\]

connected components.

Each component would correspond to a choice of one of two arcs in each coordinate.

This is a mathematically coherent topological encoding idea.

But there are two major difficulties.

## **11. Difficulty 1: the compatibility locus is not automatically a product**

As proved in Part II, the compatibility locus is

\\[ \operatorname{Gr}(\omega-d,k-d). \\]

A product of \\(s\\) projective lines is a different variety in general.

For example,

\\[ (\mathbb P^1)^2 \\]

has dimension two, just like \\(\mathbb P^2\\), but they are not isomorphic as algebraic varieties.

Therefore one cannot simply assign one independent projective coordinate to each Boolean variable by choosing a suitable value of \\(\omega\\) and \\(k\\).

The product structure must be created by the spectral condition or by a special decomposition of the admissible-subspace geometry.

The question becomes:

> Can the spectral-feasibility locus inside a single Grassmannian have the same real topology as a product of independently split projective lines?

This is a much more precise version of Q3.

## **12. Difficulty 2: component decoding must be algorithmic**

Even if the active set has \\(2^s\\) connected components, that alone does not give a polynomial-time reduction.

One must distinguish:

- existence of \\(2^s\\) components;
- ability to identify the component containing a given \\(W\\);
- ability to associate a Boolean assignment with that component;
- ability to verify that the assignment satisfies the source instance.

For a polynomial-time reduction, the matrices must be constructible in polynomial time.

For a polynomial-time witness decoder, one additionally needs an efficient method for determining the component label.

Real algebraic geometry provides methods for computing connected components of semialgebraic sets, but their complexity can be substantial. A proof that the component count is exponential is not a proof that the components can be efficiently labeled.

The proposed decoding should therefore be given explicitly, ideally through signs of polynomial functions.

For instance, suppose the active components are distinguished by

\\[ \operatorname{sign}g_i(W)\in\\{-1,+1\\}, \qquad i=1,\ldots,s. \\]

Then one can define

\\[ \beta_i(W)= \begin{cases} 0,&g_i(W)>0,\\\ 1,&g_i(W)<0. \end{cases} \\]

This is more concrete than referring abstractly to a component index.

The key requirement is that none of the \\(g_i\\) vanish on the active set and that the sign vector be constant on each connected component.

## **13. Does fibrewise rigidity obstruct component decoding?**

No.

Suppose the decoding map depends only on \\(W\\):

\\[ \beta:\mathcal X\_{\mathrm{act}}(\mathbb R) \to\\{0,1\\}^s. \\]

For each fixed active \\(W\\), all feasible free-row witnesses belong to the same fibre \\(M_W\\).

The decoding value is then identical for every feasible witness in that fibre.

This is compatible with fibrewise rigidity because the decoding does not impose a polynomial restriction on the free rows.

In particular, if

\\[ R\in M_W \\]

is feasible, the decoder returns

\\[ \beta(W), \\]

independently of the particular choice of \\(R\\).

Thus the fibrewise density result does not prohibit this type of decoding.

### **13.1 A more important qualification: decision reductions do not require decoding**

There is an additional distinction that should be made explicit.

For an ordinary polynomial-time many-one reduction, the requirement is only

\\[ z\in\mathcal L \iff I(z)\in\mathsf{FO}. \\]

It is not necessary to decode a source solution from every feasible target witness.

Witness decoding is needed for stronger reductions involving search problems or explicit solution recovery.

Therefore, component-based Boolean decoding is a possible additional strategy, not a necessary condition for NP-hardness.

This is important because the report's earlier discussion sometimes treats the existence of a target witness and the recovery of a source assignment as though they were the same requirement.

They are not.

## **14. My answer to Q2**

I would state the conclusion as follows:

- If components mean Zariski connected components, component encoding is impossible whenever the active set is a nonempty Zariski-open subset of the compatibility Grassmannian.
- If components mean real Euclidean connected components, component encoding remains possible in principle.
- Fibrewise rigidity does not obstruct a decoder depending only on \\(W\\).
- An actual reduction still requires an explicit polynomial-time construction and a sound decoding or, for a decision reduction, a proof of feasibility equivalence.

I recommend retaining the component idea, but formulating it explicitly in real algebraic geometry.

# **Part V. Q3 — Can the active set have exactly&#x20;**\\(2^s\\)**&#x20;components?**

## **15. The first structural obstacle**

The report suggests making the compatibility locus a product of projective lines:

\\[ (\mathbb P^1)^s. \\]

As explained above, the compatibility locus generated solely by the fixed rows is instead

\\[ \operatorname{Gr}(\omega-d,k-d). \\]

Thus the product structure cannot arise from the compatibility condition alone.

Nevertheless, the active set is not determined by compatibility alone. It is further restricted by:

1. the rank-completion condition;
2. the generic spectral-feasibility condition.

These can remove algebraic subsets of the Grassmannian.

Therefore the more appropriate question is whether a Grassmannian with a suitable algebraic subset removed can acquire \\(2^s\\) real connected components.

The answer is yes in general real algebraic geometry, but it has not been established for this particular observer architecture.

## **16. An illustrative construction in real projective geometry**

Consider

\\[ X=(\mathbb P^1(\mathbb R))^s. \\]

For each coordinate \\(i\\), choose two distinct points

\\[ P_i^0,\ P_i^1\in\mathbb P^1(\mathbb R). \\]

Define

\\[ X\_{\mathrm{good}} = \prod\_{i=1}^s \left( \mathbb P^1(\mathbb R) \setminus\\{P_i^0,P_i^1\\} \right). \\]

Each factor has two connected components, so

\\[ \\#\pi_0(X\_{\mathrm{good}})=2^s. \\]

A component is indexed by a vector

\\[ \beta\in\\{0,1\\}^s. \\]

This demonstrates that an exponential number of real components can arise from removing relatively simple algebraic subsets.

But there is a crucial point: the construction uses a product of projective lines.

We need an analogous construction inside

\\[ \operatorname{Gr}(\omega-d,k-d). \\]

### **16.1 A possible Grassmannian-based strategy**

One possibility is to use a Grassmannian with a coordinate chart represented by matrices:

\\[ W=\operatorname{row}[I\_\omega\ X]. \\]

Here

\\[ X\in\mathbb R^{\omega\times(k-\omega)}. \\]

The chart is an affine space of dimension

\\[ \omega(k-\omega). \\]

If the spectral test could enforce the nonvanishing of suitable polynomials

\\[ g_1(X),\ldots,g_s(X) \\]

and the signs of these polynomials distinguished the active components, then the active set could have exponentially many real components.

For example, the equations

\\[ g_i(X)=0 \\]

could define separating hypersurfaces.

The complement

\\[ \\{X:g_1(X)\cdots g_s(X)\ne0\\} \\]

has connected components corresponding to feasible sign patterns, subject to the actual geometry of the hypersurfaces.

This is a more natural approach than trying to force a literal product of projective lines.

However, it still leaves the main problem:

**Can the generic-pencil condition generate the required hypersurfaces in Grassmannian coordinates?**

That is precisely the expressive-power question.

## **17. A useful dimension restriction**

Suppose the compatibility locus is

\\[ \operatorname{Gr}(q,\ell), \qquad q=\omega-d,\quad \ell=k-d. \\]

Its dimension is

\\[ D=q(\ell-q) = (\omega-d)(k-\omega). \\]

If one wants \\(s\\) independent continuous parameters, necessarily

\\[ D\ge s \\]

for an ordinary full-dimensional parameterization.

This is only a necessary condition, not a sufficient one.

It suggests that any construction based on \\(s\\) independent Boolean choices should first choose dimensions satisfying

\\[ (\omega-d)(k-\omega)\ge s. \\]

One should then investigate whether the spectral test can produce at least \\(s\\) independent separating conditions in a suitable chart.

## **18. A potentially stronger direction: sign-pattern complexity**

Rather than directly constructing \\(2^s\\) connected components, I suggest studying the number of realizable sign patterns of the polynomial conditions defining the generic-pencil locus.

Suppose the generic spectral condition can be represented locally by

\\[ g_1(W)\ne0,\ldots,g_t(W)\ne0. \\]

Then the real active set is a union of sign regions:

\\[ \mathcal X\_{\mathrm{act}}(\mathbb R) = \bigcup\_{\sigma\in\\{-1,+1\\}^t} \left\\{ W: \operatorname{sign}g_i(W)=\sigma_i \right\\}, \\]

possibly with additional rank conditions.

The number of nonempty sign regions is bounded by real algebraic-geometric complexity estimates in terms of:

- the dimension of the Grassmannian;
- the number of defining polynomials;
- their degrees.

This provides an intermediate quantitative question:

> Can the spectral-feasibility polynomials realize exponentially many sign patterns in the dimension of the Grassmannian?

This is easier to formulate than an exact \\(2^s\\)-component construction.

It also connects the observer problem with established questions about arrangements of algebraic hypersurfaces.

## **19. My answer to Q3**

I would not yet claim that the active set can be made to have exactly \\(2^s\\) components.

The mathematically justified position is:

1. A nonempty Zariski-open active set in an irreducible Grassmannian has one algebraic component.
2. Its real locus can nevertheless have many Euclidean connected components.
3. The compatibility locus itself is a Grassmannian, not generally a product of projective lines.
4. The spectral condition may potentially create exponential real component complexity.
5. Whether the particular pencil structure permits this remains open.

This is a genuine research direction, not a consequence of the existing gates.

# **Part VI. Q4 — Should the reduction target the top layer?**

## **20. What does the top layer mean geometrically?**

The report suggests considering

\\[ W=V=\mathbb F^{1\times k}. \\]

This corresponds to

\\[ \omega=k. \\]

Then

\\[ W=\mathbb F^{1\times k} \\]

is the unique possible row space.

Consequently,

\\[ \operatorname{Gr}(k,k) \\]

is a point.

There is no Grassmannian selection problem.

The compatibility condition becomes automatic, because every compressed row belongs to \\(V\\).

The space of admissible free-row pairs is

\\[ \mathcal T_V=\mathcal S. \\]

The rank-completion condition becomes

\\[ \operatorname{span} \left( \\{h_i^0\\}\cup\pi_1(\mathcal S) \right)=V. \\]

But the first projection of \\(\mathcal S\\) is all of \\(V\\):

\\[ \pi_1(\mathcal S) = \\{rN:r\in\mathbb F^{1\times n}\\} = V, \\]

because \\(N\\) has full column rank.

Thus rank completion is automatic as soon as there is at least one free row:

\\[ m\ge1. \\]

The entire feasibility question in this top layer reduces to the generic spectral condition on

\\[ \mathcal S. \\]

This is an important simplification.

## **21. The top layer still has nontrivial data-side structure**

Although \\(W\\) is fixed, the generic pencil need not be trivial.

Let

\\[ \mathcal S=\operatorname{row}[N\ AN]. \\]

The admissible pairs for each free row belong to \\(\mathcal S\\).

If

\\[ \dim\mathcal S=\rho, \\]

then the \\(m\\) free rows contribute \\(m\rho\\) parameters at the compressed-pair level, subject to possible redundancy in the original row representation.

The generic pencil is constructed from:

- the fixed compressed pairs;
- \\(m\\) generic pairs from \\(\mathcal S\\).

Its maximal minors may have a complicated dependence on the input matrices \\(A,C,L_0\\).

Thus even though the Grassmannian disappears, the data-side generic-pencil condition remains.

This distinction is important:

\\[ \boxed{ \text{No subspace choice does not imply no computational complexity.} } \\]

The input matrices may still encode a difficult algebraic condition in the generic pencil.

## **22. The square-pencil obstruction is decisive**

The report establishes that if

\\[ r=k=\omega, \\]

then the pencil is square and

\\[ \det(\lambda H-H_A) \\]

has degree \\(k\\) with leading coefficient

\\[ \det H\ne0. \\]

Over \\(\mathbb C\\), it must have a root.

Therefore the spectral condition fails.

This is correct.

However, it is important not to confuse the top layer with the square case.

The top layer means

\\[ \omega=k. \\]

It does not necessarily mean

\\[ r=k. \\]

If

\\[ r>k, \\]

then the pencil is rectangular, and full column rank for every \\(\lambda\\) can be possible.

For example,

\\[ H= \begin{pmatrix} 1&0\\\ 0&1\\\ 0&0 \end{pmatrix}, \qquad H_A= \begin{pmatrix} 0&0\\\ 0&0\\\ 1&1 \end{pmatrix}. \\]

Then

\\[ \lambda H-H_A = \begin{pmatrix} \lambda&0\\\ 0&\lambda\\\ -1&-1 \end{pmatrix}. \\]

At \\(\lambda=0\\), the last row is nonzero, while for \\(\lambda\ne0\\), the first two rows are linearly independent. Thus the pencil has rank two for every complex \\(\lambda\\).

This illustrates why the square-pencil obstruction does not apply to the top layer generally.

## **23. What can the witness encode if&#x20;**\\(W\\)**&#x20;is fixed?**

There are two distinct possibilities.

### **Possibility A: the free-row witness has no source-assignment role**

The reduction may encode the source problem entirely into the instance data.

The target instance is feasible precisely when a generic pencil associated with \\(\mathcal S\\) satisfies the required spectral property.

In this case, \\(R\\) is simply a witness that realizes a generic admissible choice. It does not need to encode a Boolean assignment.

This is entirely legitimate for a many-one decision reduction.

### **Possibility B: the free rows encode a source assignment**

This is much more difficult.

Fibrewise rigidity says that the feasible free-row set is dense in the admissible fibre whenever it is nonempty.

Therefore it cannot enforce polynomial equations among the free-row coordinates beyond the identities already imposed by the linear fibre structure.

If one tries to define Boolean variables as polynomial functions of \\(R\\), the construction cannot force those functions to take prescribed discrete values throughout the feasible fibre unless the corresponding identities already hold throughout the entire fibre.

Thus the usual scalar-witness encoding strategy is severely restricted.

## **24. My recommendation concerning Q4**

I would investigate the top layer separately as an algorithmic and complexity-theoretic branch.

Its advantages are:

- no Grassmannian search;
- automatic compatibility;
- automatic rank completion with at least one free row;
- a generic-pencil condition depending only on \\(\mathcal S\\) and the fixed pairs.

Its disadvantage is that it removes the most obvious source of existential geometric freedom.

The key question becomes:

\\[ \boxed{ \text{What coefficient conditions characterize generic spectral regularity of } \mathcal S? } \\]

If this condition has enough expressive power, the top layer may be sufficient for hardness.

If it admits a polynomial-time characterization, it may provide a useful tractable special case.

I would not make the top layer the only target of the reduction programme, but I would definitely study it as a separate branch.

# **Part VII. Q5 — Which computation is decisive for isolated multi-active sets?**

## **25. My recommendation: exact symbolic elimination, not random sampling**

The report asks for one decisive computation, particularly for

\\[ k=2 \\]

and

\\[ \operatorname{Gr}(2,3). \\]

I would prioritize a symbolic computation that determines the active-subspace locus exactly.

Random sampling is not sufficient for this purpose.

A finite random search can establish that certain sampled points are not active, but it cannot establish:

- that the active set is empty;
- that the active set contains isolated points;
- that two different active points belong to different components;
- that a positive-dimensional active set does not exist.

The right approach is to parameterize \\(W\\), compute \\(\mathcal T_W\\) exactly, construct the generic pencil over the rational function field of its parameters, and eliminate the spectral variable.

There are two especially useful low-dimensional cases.

## **26. Case I:&#x20;**\\(k=2\\)**,&#x20;**\\(\omega=1\\)

Here

\\[ \operatorname{Gr}(1,2)\cong\mathbb P^1. \\]

Write a candidate row space as

\\[ W\_{[s:t]} = \operatorname{span}\\{(s,t)\\}. \\]

Its annihilator is generated by

\\[ q=(-t,s). \\]

A vector

\\[ x=(x_1,x_2) \\]

belongs to \\(W\_{[s:t]}\\) precisely when

\\[ -tx_1+sx_2=0. \\]

Therefore the fixed-row compatibility conditions are

\\[ -t(h_i^0)\_1+s(h_i^0)\_2=0, \\]

and

\\[ -t(g_i^0)\_1+s(g_i^0)\_2=0. \\]

### **26.1 Compatibility can be completely classified**

Let

\\[ U=\operatorname{span}\\{h_i^0,g_i^0\\}. \\]

There are only three possibilities.

- If \\(\dim U=0\\), every \\(W\in\mathbb P^1\\) is compatible.
- If \\(\dim U=1\\), there is exactly one compatible \\(W\\).
- If \\(\dim U=2\\), there is no compatible \\(W\\).

Thus the unpinned case is particularly simple: it is the entire projective line.

This makes \\(k=2,\omega=1\\) an excellent first test of Q1.

### **26.2 Explicit parameterization of&#x20;**\\(\mathcal T_W\\)

Choose the chart \\(s\ne0\\), and normalize

\\[ W_z=\operatorname{span}\\{(1,z)\\}, \qquad z=t/s. \\]

For a pair

\\[ (x,y)\in\mathcal S, \\]

membership in \\(W_z\oplus W_z\\) is equivalent to

\\[ x_2-zx_1=0, \qquad y_2-zy_1=0. \\]

Hence

\\[ \mathcal T_z = \ker \left( \begin{bmatrix} -z&1&0&0\\\ 0&0&-z&1 \end{bmatrix} \bigg|\_{\mathcal S} \right). \tag{12} \\]

This is an exact linear-algebraic description.

If

\\[ B \\]

is a matrix whose columns form a basis of \\(\mathcal S\\), then a basis of \\(\mathcal T_z\\) can be computed as the kernel of a matrix whose entries are polynomial in \\(z\\).

The dimension changes only at zeros of certain minors of this matrix.

Therefore the projective line has a finite algebraic stratification into constant-rank regions and exceptional points.

This is computationally manageable.

### **26.3 The generic spectral test becomes especially simple**

Because \\(W_z\\) has dimension one, every admissible compressed row can be written as

\\[ h_j=\alpha_j(1,z), \qquad g_j=\beta_j(1,z). \\]

The pencil becomes

\\[ P(\lambda) = \begin{pmatrix} \lambda\alpha_1-\beta_1\\\ \vdots\\\ \lambda\alpha_r-\beta_r \end{pmatrix} (1,z). \\]

The rank is one if and only if the scalar polynomials

\\[ \lambda\alpha_j-\beta_j \\]

do not vanish simultaneously.

Consequently,

\\[ \boxed{ \text{Spectral regularity} \iff \gcd_j(\lambda\alpha_j-\beta_j)=1. } \tag{13} \\]

This is much simpler than a general matrix-pencil calculation.

In particular:

- one nonzero constant polynomial immediately guarantees regularity;
- two nonzero linear polynomials with distinct roots guarantee regularity;
- if all nonconstant polynomials have the same root and there is no nonzero constant polynomial, regularity fails.

This provides an explicit low-dimensional classification.

The generic spectral condition can therefore be expressed through the linear geometry of the admissible coefficient pairs

\\[ (\alpha,\beta)\in\mathbb F^2. \\]

I would exploit this before moving to \\(k=3\\).

## **27. Case II:&#x20;**\\(k=3\\)**,&#x20;**\\(\omega=2\\)

Now

\\[ \operatorname{Gr}(2,3)\cong\mathbb P^2. \\]

Every two-dimensional row space can be written as

\\[ W_q=\ker q^{\mathsf T}, \qquad q=(q_1,q_2,q_3)\ne0, \\]

where \\(q\\) is considered projectively.

Thus the parameter space is

\\[ [q_1:q_2:q_3]\in\mathbb P^2. \\]

### **27.1 Compatibility**

A fixed pair

\\[ (h_i^0,g_i^0) \\]

belongs to \\(W_q\oplus W_q\\) if and only if

\\[ q^{\mathsf T}h_i^0=0, \qquad q^{\mathsf T}g_i^0=0. \\]

Again, let

\\[ U=\operatorname{span}\\{h_i^0,g_i^0\\}. \\]

The compatible locus is:

| \\(d=\dim U\\) | Compatible locus  |
| -------------- | ----------------- |
| 0              | \\(\mathbb P^2\\) |
| 1              | \\(\mathbb P^1\\) |
| 2              | One point         |
| 3              | Empty             |

This classification is exact.

It also provides an immediate diagnostic for the report's failed \\(\operatorname{Gr}(2,3)\\) probes.

If the fixed rows span a two-dimensional space, only one \\(W\\) is possible. If they span a line, only a projective line needs to be investigated. If they span zero, the entire projective plane must be investigated.

### **27.2 Constructing the admissible pair space**

Write

\\[ \mathcal S=\operatorname{row}[N\ AN]. \\]

A pair

\\[ (x,y)\in\mathcal S \\]

belongs to \\(\mathcal T\_{W_q}\\) if and only if

\\[ q^{\mathsf T}x=0,\qquad q^{\mathsf T}y=0. \\]

Therefore

\\[ \mathcal T\_{W_q} = \ker\left( \begin{bmatrix} q^{\mathsf T}&0\\\ 0&q^{\mathsf T} \end{bmatrix} \bigg|\_{\mathcal S} \right). \tag{14} \\]

Choose a basis matrix \\(B\\) for \\(\mathcal S\\). Then the restricted matrix is

\\[ M(q)= \begin{bmatrix} q^{\mathsf T}&0\\\ 0&q^{\mathsf T} \end{bmatrix}B. \\]

Its entries are linear in \\(q_1,q_2,q_3\\).

Thus the exceptional locus where

\\[ \dim\mathcal T\_{W_q} \\]

jumps is determined by determinantal equations in projective coordinates.

This is the first object I would compute symbolically.

### **27.3 Construct the generic pencil**

On each constant-rank chart, choose a rational basis

\\[ Z(q) \\]

of \\(\ker M(q)\\).

Introduce independent parameters

\\[ z_1,\ldots,z_D \\]

for the admissible free-row choices.

The resulting pencil is

\\[ P(\lambda,q,z) = \lambda H(q,z)-H_A(q,z). \\]

Since

\\[ \omega=2, \\]

its maximal minors are the \\(2\times2\\) minors:

\\[ m_1(\lambda,q,z),\ldots,m_s(\lambda,q,z). \\]

The generic spectral condition is

\\[ \boxed{ \gcd\_{\overline{\mathbb F(z)}[\lambda]} \bigl(m_1,\ldots,m_s\bigr)=1. } \tag{15} \\]

This must be checked over the rational function field in the free-row parameters, not merely at a few numerical values.

### **27.4 Eliminate the spectral variable**

Because each maximal minor has degree at most two in \\(\lambda\\), the generic coprimality condition can be analyzed using polynomial remainder sequences or subresultant matrices.

For a collection of polynomials, one can use a generic linear combination:

\\[ f(\lambda)=\sum_j a_jm_j(\lambda), \qquad g(\lambda)=\sum_j b_jm_j(\lambda), \\]

with auxiliary indeterminates \\(a_j,b_j\\).

Over an infinite field, generic choices give

\\[ \gcd(f,g)=\gcd(m_1,\ldots,m_s). \\]

Thus generic coprimality of all maximal minors can be tested by a resultant:

\\[ \operatorname{Res}\_\lambda(f,g)\ne0, \\]

provided the generic combinations are handled over the appropriate function field and the degree drops are treated correctly.

This reduces the spectral condition to nonvanishing of polynomial expressions in

\\[ q_1,q_2,q_3 \\]

and the relevant generic parameters.

The remaining task is to eliminate the generic parameters in a way that preserves the distinction between generic feasibility and mere existence of a special parameter choice.

This distinction is essential.

# **Part VIII. The single computation I would perform first**

## **28. Compute the exact active locus in&#x20;**\\(\mathbb P^1\\)**&#x20;before&#x20;**\\(\mathbb P^2\\)

Although the report emphasizes both \\(k=2\\) and \\(\operatorname{Gr}(2,3)\\), I would begin with

\\[ k=2,\qquad\omega=1. \\]

The reason is that the spectral test becomes the gcd of scalar linear polynomials, as in (13).

A complete symbolic classification is much more realistic here.

I would implement the following procedure.

**Proposed symbolic experiment:&#x20;**\\(k=2,\omega=1\\)

1. **Compute the fixed-row span**

   \\[ U=\operatorname{span}\\{h_i^0,g_i^0\\}. \\]

   Determine whether the compatible locus is empty, a point, or all of \\(\mathbb P^1\\).
2. **Parameterize the projective line**

   Use \\(W_z=\operatorname{span}(1,z)\\), together with the chart at infinity.
3. **Compute the exact kernel**

   Construct \\(\mathcal T_z\\) using (12), and determine all exceptional values of \\(z\\) at which its dimension changes.
4. **Construct the generic scalar pencil**

   Express all admissible rows as \\((\alpha_j,\beta_j)\\) in a basis of \\(\mathcal T_z\\).
5. **Compute the generic gcd**

   Determine exactly when

   \\[ \gcd_j(\lambda\alpha_j-\beta_j)=1. \\]
6. **Eliminate the generic parameters**

   Obtain polynomial equalities and inequations in \\(z\\) describing the active locus.
7. **Classify its real topology**

   Determine whether the active set is empty, finite, or contains intervals, and count its connected components.

This experiment would answer several questions simultaneously:

- Does global openness hold in the simplest nontrivial case?
- Can isolated active subspaces occur?
- Can there be multiple active points?
- Can the active set have multiple real connected components?
- What algebraic features of \\(\mathcal S\\) control these possibilities?

## **29. A useful theorem to target from this computation**

I would formulate the following as the next intermediate theorem.

**Theorem (projective-line active-set classification).**

Let

\\[ k=2,\qquad\omega=1, \\]

and suppose the fixed-row compatibility locus is the entire projective line.

Then the active-subspace set is determined by the generic coprimality condition

\\[ \gcd_j(\lambda\alpha_j(z)-\beta_j(z))=1, \\]

where the pairs \\((\alpha_j(z),\beta_j(z))\\) are obtained from the linear family

\\[ \mathcal T_z=\mathcal S\cap(W_z\oplus W_z). \\]

On each constant-rank chart, the active set is Zariski open.

The remaining question is whether the exceptional rank-jump points can introduce additional isolated active points or other behavior not predicted by the open loci on the constant-rank strata.

A complete classification of those exceptional points would settle the first nontrivial instance of Q1.

I would regard this as a strong mathematical result even if it ultimately proves that isolated multi-active sets do not exist in this case.

# **Part IX. An important correction to the proposed three-test criterion**

## **30. The rank-completion and spectral conditions must be combined carefully**

The report treats rank completion and generic spectral feasibility as separate tests.

This is reasonable, but the exact equivalence deserves a formal statement.

Fix \\(W\\), and let

\\[ \mathcal P_W=\mathcal T_W^m \\]

be the affine parameter space of \\(m\\) free-row compressed pairs.

Let

\\[ \mathcal U_W^{\mathrm{rank}} \subseteq\mathcal P_W \\]

be the set on which \\(H\\) has rank \\(\omega\\).

This is Zariski open.

Let

\\[ \mathcal U_W^{\mathrm{spec}} \subseteq\mathcal P_W \\]

be the set on which the pencil has rank \\(\omega\\) for all complex \\(\lambda\\).

This is also Zariski open.

The actual feasible set in the fibre is

\\[ \mathcal U_W^{\mathrm{rank}} \cap \mathcal U_W^{\mathrm{spec}}. \\]

Since \\(\mathcal P_W\\) is irreducible, if both open sets are nonempty, their intersection is nonempty.

Therefore:

\\[ \boxed{ \begin{aligned} &\exists z\in\mathcal P_W: \operatorname{rank}H(z)=\omega \text{ and } P_W(\lambda,z)\text{ is regular for all }\lambda\\\ &\iff \mathcal U_W^{\mathrm{rank}}\ne\varnothing \text{ and } \mathcal U_W^{\mathrm{spec}}\ne\varnothing. \end{aligned} } \tag{16} \\]

This is a useful formal justification for separating the two conditions.

However, for the report's third test, I would recommend a small refinement:

The generic-pencil calculation should be performed on the entire linear space \\(\mathcal T_W^m\\), and the rank-completion test should be checked independently.

There is no need to impose rank completion before computing the generic spectral gcd, provided the equivalence in (16) is used.

This makes the symbolic implementation simpler.

## **31. A field qualification**

The report uses

\\[ R\in\mathbb F^{m\times n} \\]

while the spectral parameter ranges over \\(\mathbb C\\).

For a real observer problem, the correct interpretation is

\\[ R\in\mathbb R^{m\times n}, \qquad \lambda\in\mathbb C. \\]

The algebraic openness arguments should then be understood over the complexification of the real parameter space, with real points considered for actual witnesses.

If the admissible parameter space is a real affine linear space, a nonempty Zariski-open subset defined over \\(\mathbb R\\) has real points and is Euclidean dense in that affine space.

This helps transfer the generic argument to real witnesses.

Nevertheless, the distinction between:

- complex feasibility;
- real feasibility;
- rational feasibility

must be maintained in any final complexity theorem.

In particular, the existence of a complex active subspace does not automatically imply the existence of a real active subspace.

# **Part X. Recommended revisions to Report 105**

## **32. What should be added**

I would revise the report by adding four results or clarifications.

| Addition      | Mathematical content                                            | Importance                             |
| ------------- | --------------------------------------------------------------- | -------------------------------------- |
| Proposition 1 | Compatibility locus is \\(\operatorname{Gr}(\omega-d,k-d)\\)    | Establishes its global geometry        |
| Proposition 2 | Spectral regularity is open on each fixed fibre                 | Formalizes the generic-pencil argument |
| Proposition 3 | Active locus is open on constant-rank strata                    | Gives a partial answer to Q1           |
| Proposition 4 | Distinguish algebraic components from real connected components | Makes Q2 and Q3 mathematically precise |

## **33. What should be corrected**

I would make the following changes.

**First:** The statement that the active set is a union of finitely many connected components should specify the topology. In the Zariski topology, this is a very different assertion from the real Euclidean topology.

**Second:** The proposed product-of-projective-lines construction should be presented as a possible topology of the real active locus, not as an automatic structure of the compatibility locus.

**Third:** The top-layer discussion should explicitly distinguish

\\[ \omega=k \\]

from

\\[ r=k. \\]

Only the latter, together with full square rank, produces the square-pencil obstruction.

**Fourth:** The statement that the active set is relatively open should remain conditional until the dimension-jump issue for \\(\mathcal T_W\\) is resolved.

**Fifth:** The report should distinguish decision reductions from witness-decoding reductions. Component decoding is an interesting additional idea, but it is not required for ordinary NP-hardness reductions.

# **Part XI. A revised research programme**

## **34. The next four theorems**

I would organize the next stage around the following results.

**Theorem A: Compatibility geometry**

Ready to prove

\\[ \mathcal X\_{\mathrm{comp}} \cong\operatorname{Gr}(\omega-d,k-d). \\]

This is a direct consequence of the fixed-row span.

**Theorem B: Stratified openness**

Provable framework

On every constant-rank stratum of \\(\Psi_W\\), the active-subspace set is relatively open.

**Theorem C: Global openness**

Open

Determine whether the special incidence geometry of \\(\mathcal S\cap(W\oplus W)\\) guarantees global openness or admits counterexamples.

**Theorem D: Component complexity**

Open

Determine whether the real active locus can have exponentially many connected components, and whether these components can encode Boolean assignments.

The logical order matters. The component-complexity question should not be attacked before the openness question is settled.

## **35. A possible algorithmic implementation**

For the symbolic experiments, I recommend using exact rational arithmetic and polynomial computation rather than floating-point numerical rank tests.

A suitable computational workflow is:

1. Construct \\(N\\) exactly from the rational matrix \\([C;CA]\\).
2. Compute a rational basis of\
   \\[\
   \mathcal S=\operatorname{row}[N\ AN].\
   \\]
3. Compute the fixed-row span \\(U\\).
4. Determine the compatibility Grassmannian.
5. Introduce Grassmannian coordinates in suitable affine charts.
6. Construct the matrix defining \\(\mathcal T_W\\).
7. Stratify by its determinantal rank conditions.
8. Compute a rational basis of \\(\mathcal T_W\\) on each stratum.
9. Construct the generic pencil.
10. Compute its maximal minors and generic gcd.
11. Eliminate the free-row parameters.
12. Determine the real connected components of the resulting semialgebraic locus.

For exact symbolic work, the most relevant methods are:

- rational Gaussian elimination;
- determinantal ideals;
- Gröbner bases;
- subresultant sequences;
- resultants;
- real quantifier elimination;
- semialgebraic connected-component computation.

One important implementation rule: do not evaluate the generic pencil at random free-row choices and interpret successful or unsuccessful samples as a classification. Genericity is an algebraic statement and should be tested over the function field.

# **Part XII. Final evaluation**

## **36. Answers to the five questions**

**Q1. What is the type of test (iii) as a function of&#x20;**\\(W\\)**?**

For fixed \\(W\\), it is a Zariski-open condition on the admissible free-row parameter space.

As \\(W\\) varies, it is relatively open on constant-rank strata of the incidence map

\\[ \Psi_W:\mathcal S\to(V/W)\oplus(V/W). \\]

Global openness is not yet established. The rank-jump loci must be analyzed.

**Q2. Can the component index encode a Boolean assignment?**

For Zariski connected components, no, provided the active set is a nonempty Zariski-open subset of the compatibility Grassmannian.

For real Euclidean connected components, potentially yes. A component-based decoder depending only on \\(W\\) is compatible with fibrewise rigidity.

However, the component labels must be efficiently computable if one wants a constructive search reduction.

**Q3. Can the active set have exactly&#x20;**\\(2^s\\)**&#x20;components?**

This is possible in principle for real semialgebraic sets, but not yet established for this architecture.

The compatibility locus is a single Grassmannian. The challenge is to determine whether the spectral condition can generate enough separating algebraic hypersurfaces to create exponentially many real components.

**Q4. Should the reduction target the top layer?**

The top layer is worth investigating separately.

There,

\\[ W=V,\qquad \mathcal T_W=\mathcal S, \\]

and rank completion is automatic with at least one free row.

The problem reduces to generic spectral regularity of the pencil constructed from \\(\mathcal S\\) and the fixed pairs.

This may be sufficient for a data-side hardness reduction, but it does not provide a Boolean witness encoding.

**Q5. Which computation is decisive?**

Start with

\\[ k=2,\qquad\omega=1. \\]

Compute the exact projective-line active locus using

\\[ \gcd_j(\lambda\alpha_j(z)-\beta_j(z))=1. \\]

Then move to

\\[ k=3,\qquad\omega=2, \\]

using hyperplane coordinates \\(q\in\mathbb P^2\\) and exact elimination of the generic-pencil parameters.

This is the most efficient progression.

## **37. Final recommendation**

Recommended next direction

I would make **the global geometry of the generic spectral-feasibility locus** the central problem of the next report.

The decisive chain of reasoning is:

\\[ \boxed{ \begin{gathered} \text{Fixed-row span }U\\\ \Downarrow\\\ \mathcal X\_{\mathrm{comp}} =\operatorname{Gr}(\omega-d,k-d)\\\ \Downarrow\\\ \mathcal T_W=\mathcal S\cap(W\oplus W)\\\ \Downarrow\\\ \text{Generic pencil and maximal-minor gcd}\\\ \Downarrow\\\ \mathcal X\_{\mathrm{act}}\\\ \Downarrow\\\ \text{Algebraic and real-topological complexity}. \end{gathered} } \\]

There are two particularly valuable possible outcomes.

**Outcome A: Global openness.**

If global openness can be proved, the active set is either empty or a dense open subset of the irreducible compatibility Grassmannian. This would rule out isolated multi-active sets in every positive-dimensional compatibility locus and eliminate algebraic component encoding.

The real topology could still be complicated, but the possibilities would be much more constrained.

**Outcome B: Failure of global openness.**

If one constructs an explicit observer instance in which the active set contains isolated points or different-dimensional pieces, this would reveal an important mechanism arising from rank jumps in \\(\mathcal T_W\\).

Such an example could be the foundation of a discrete encoding construction.

I would regard either outcome as a significant result.

**My strongest recommendation is therefore not to start with another Booleanity gadget or an immediate NP-hardness reduction. First settle the global openness question, beginning with the exact&#x20;**\\(k=2,\omega=1\\)**&#x20;classification.** That result will determine whether the component-based reduction strategy has a realistic mathematical foundation or whether the project should concentrate on the top-layer generic-pencil problem instead.