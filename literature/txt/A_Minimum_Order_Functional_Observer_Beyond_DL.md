
===== page 1 =====
1
A Minimum-Order Functional Observer Beyond
the Darouach and Luenberger Constructions
T yrone Fernando
Abstract— This paper develops a general minimum-order
functional observer framework that contains the classical
Darouach functional observer and the reduced-order Luen-
berger observer as special cases. The required functional
dimension is determined from the triple(A,C,L)through
a set of functional observability indices. The minimum
dimension permitted by the algebraic observer-existence
condition is characterized, and the complete family of
augmentations attaining this dimension is determined.
Necessary-and-sufficient spectral feasibility conditions are
then established for this dimension to be the minimum
achievable observer order. The resulting existence condi-
tions reduce exactly to the Darouach conditions when no
augmentation is required and to the classical observability
condition in the reduced-order Luenberger case. More gen-
erally, the framework admits minimum-order functional ob-
servers of intermediate order, which may exist even when
neither classical observer is available.
Index Terms— Functional observers, Functional observ-
ability indices, minimum-order observer, Luenberger ob-
server, Darouach observer.
I. INTRODUCTION
Functional observers arise when only prescribed linear func-
tions of the state, rather than the entire state vector, need to be
estimated. Consider the continuous-time linear time-invariant
system
˙x(t) =Ax(t) +Bu(t), y(t) =Cx(t), z(t) =Lx(t),(1)
wherex(t)∈R n is the state,u(t)∈R m is the input,y(t)∈
Rp is the measured output, andz(t)∈R r is the functional
to be estimated, withA∈R n×n,B∈R n×m,C∈R p×n,
andL∈R r×n. Whenr≪n, reconstructing the complete
state solely to recoverzmay introduce unnecessary observer
dynamics, motivating the search for the minimum observer
order required to estimateLx(t).
The reduced-order Luenberger observer provides a
minimum-order structure for reconstructing state directions
not directly available from the measured output. Luenberger
also introduced functional observers for estimating prescribed
linear functions without reconstructing the entire state [1],
although general existence conditions were not established.
This initiated extensive research on single- and multi-
functional observer design; see [2]- [5] and the references
T . Fernando is with the Department of Electrical, Electronic
and Computer Engineering, University of Western Australia (UWA),
35 Stirling Highway , Crawley , WA 6009, Australia. (email: ty-
rone.fernando@uwa.edu.au)
therein. Darouach [6] later established necessary-and-
sufficient conditions for the existence and design of an
order-rfunctional observer, whereris the number of
independent functional directions to be estimated. More
recently, functional-observer theory has been extended to
large-scale and interconnected systems [7]- [9], networked
systems [10]- [13], sampled-data systems [14] and nonlinear
systems [15]- [16]. The Darouach functional observer and the
reduced-order Luenberger observer represent two important
classical cases of the minimum-order problem considered
here.
These cases do not exhaust the possible functional-observer
structures. The prescribed functional matrixLmay fail the
Darouach observer-existence conditions, while the system may
be unobservable and hence admit no reduced-order Luenberger
observer, even though the triple(A, C, L)is functional ob-
servable. Failure of an order-rDarouach observer does not
imply that a minimum-order functional observer does not
exist, nor that alln−punmeasured state directions must be
reconstructed; the minimum observer order may lie strictly
betweenrandn−p. Thus, the minimum order is not restricted
to either the number of prescribed functionals or the number of
unmeasured state directions, but is determined more generally
by the functional observability structure of(A, C, L), subject
to spectral feasibility.
This paper develops a general minimum-order functional
observer framework containing the Darouach and reduced-
order Luenberger observers as special cases while admitting
this intermediate regime. The prescribed functional matrix is
augmented as
L=
L
R

,
where the required number of additional functional directions
is determined from(A, C, L)through functional observability
indices and their choice is made from the complete family of
admissible augmentations.
The observer-existence conditions are separated into an
algebraic condition(A)and a spectral condition(S). The
minimum functional dimension satisfying condition(A)is
q0 =
rX
j=1
ηj, r≤q 0 ≤n−p,
whereη 1, . . . , ηr are the functional observability indices as-
sociated with the rows ofL. Since condition(A)is necessary
for observer existence, no functional observer can have order
smaller thanq 0.
arXiv:2609.33615v1  [eess.SY]  27 Sep 2026

===== page 2 =====
2
An augmentation attainingq 0 need not be unique. Hence,
failure of condition(S)for one minimum condition-(A)
augmentation does not preclude another augmentation of the
same dimension from satisfying both conditions. The complete
family of minimum condition-(A)augmentations is therefore
characterized, together with necessary-and-sufficient condi-
tions for the existence of a member satisfying condition(S).
Consequently,
νmin =q 0
if and only if at least one member of this family satisfies
condition(S).
The classical cases follow directly. When the Darouach
observer-existence conditions hold, no augmentation is re-
quired,η j = 1forj= 1, . . . , r, and
νmin =q 0 =r,
with the general existence conditions reducing exactly to the
necessary-and-sufficient Darouach conditions. At the other
specialization, when the prescribed functional directions rep-
resent all state directions not directly available from the
measured output,
νmin =q 0 =n−p,
and the general existence condition reduces to the classical
observability condition for the reduced-order Luenberger ob-
server.
The principal extension is the intermediate regime
r < q0 < n−p.
Here an order-rDarouach observer does not exist, while
reconstruction of alln−punmeasured state directions is
unnecessary. If spectral feasibility holds atq 0, thenν min =q 0,
yielding a minimum-order functional observer that may exist
even when the system is unobservable and neither classical
construction is available.
The main contributions are:
1) The minimum functional dimension permitted by condi-
tion(A)is characterized by the functional observability
indices asq 0 = Prj=1 ηj,withr≤q 0 ≤n−p.
2) The complete family of augmentations attainingq 0 and
satisfying condition(A)is characterized, and necessary-
and-sufficient conditions are established forν min =q 0.
3) The Darouach and reduced-order Luenberger observer-
existence conditions are recovered as special cases,
while intermediate-order minimum functional observers
are admitted when neither classical construction is ap-
plicable.
The paper concludes with an example in which the
Darouach conditions fail and the system is unobservable,
yet an intermediate minimum-order functional observer ex-
ists. The example also shows why the complete minimum
condition-(A)family must be considered: one minimum aug-
mentation fails condition(S), whereas another of the same
dimension satisfies it.
II. PRELIMINARIES ANDPROBLEMFORMULATION
Consider the system and prescribed functional in (1), with
inputu(t)and measured outputy(t)available. Without loss
of generality,CandLare assumed to have full row rank:
dependent measurements provide no additional information,
while dependent prescribed functionals can be recovered from
estimates of a maximal independent subset. We further assume
rank

L
C

=r+p,
since any component ofLinrow(C)is directly available from
the measured output and requires no observer dynamics.
Throughout, the triple(A, C, L)is assumed functional ob-
servable, so thatz(t) =Lx(t)is reconstructible from the
available input and output. The objective is to determine a
minimum-order functional observer for estimatingzand to
establish necessary-and-sufficient conditions for its existence.
A. Functional Observability
Functional observability admits two equivalent characteri-
zations.
Definition 1 (Functional Observability: Reconstruction Form):
As defined in [17],(A, C, L)is functionally observable if
there exists a finiteT >0such thatz(0) =Lx(0)can be
uniquely determined from the outputy(t)and known input
u(t)over0≤t≤T.
An equivalent augmentation-based characterization is as
follows.
Definition 2 (Functional Observability: Augmentation Form):
As defined in [18],(A, C, L)is functionally observable if
there exists a finite-dimensional augmentationR∈R qR×n
such thatL=
L
R

satisfies the algebraic condition
rank


LA
L
CA
C

 = rank


L
CA
C

 ,(A)
and the spectral condition
rank


λL − LA
CA
C

 = rank


L
CA
C

 ,∀λ∈C.(S)
Remark 1:Condition(S), as stated for allλ∈
C, corresponds to arbitrary observer-pole assignment. If
only asymptotic convergence is required, it suffices that
rank


λL − LA
CA
C

 = rank


L
CA
C

 ,ℜ(λ)≥0,so that
the observer poles can be assigned to the open left-half plane.
As established in [17], [19], Definitions 1 and 2 are equiv-
alent and yield
row(OL)⊆row(O C),O C =


C
CA
...
CA n−1

 ,O L =


L
LA
...
LAn−1

 .

===== page 3 =====
T . FERNANDO: 3
Equivalently,
rank
OC
OL

= rank(OC),(2)
whererow(M)denotes the row space of a matrixM. For
L=I n, this reduces torank(O C) =n, recovering classical
state observability. Also, condition(A)is equivalently
row(LA)⊆row(L, C, CA).
Since the observer order equals the number of independent
functional directions represented byL, the minimum-order
problem is
νmin := minL rankL,row(L)⊆row(L),
subject to conditions (A) and (S). The analysis proceeds in
three stages:
I determine the smallest functional dimension permitted
by(A)and construct an augmentation attaining it;
II characterize all minimum-dimensional augmentations
satisfying(A);
III test(S)over this complete family.
This separation is necessary because the minimum dimension
imposed by(A)is unique, whereas the augmentation attaining
it need not be.
III. ORDEREDFUNCTIONAL-OBSERVABILITY
CONSTRUCTION
The functional-observability condition [20],
row(OL)⊆row(O C)
establishes that the functional information generated by the
rows ofLis contained in the information generated by the
measured output. For observer construction, however, it is
necessary to identify how this information is generated and
which additional functional directions may be used to form
an augmented functional matrix satisfying conditions (A) and
(S).
To this end, we introduce an ordered rank-retention con-
struction based jointly on the rows ofCandLand their
successiveA-iterates. The construction produces a finite set
of independent directions from which the functional augmen-
tations considered later will be formed.
A. Global examination order and rank-retention rule
Write
C= (C 1;. . .;Cp), L= (L 1;. . .;Lr),
and define thep+rgenerating rowsby
g1, . . . , gp+r :=C 1, . . . , Cp, L1, . . . , Lr.(3)
For each generatorg i, consider theA-generated sequence
gi, g iA, g iA2, . . . .
The rows
giAq, i= 1, . . . , p+r, q= 0,1,2, . . . ,
are referred to as thecandidate rows.
The candidate rows are examined in the followingglobal
order: by increasing powers ofAand, within each power, in
the fixed generator order (3):
g1, . . . , gp+r;g 1A, . . . , gp+rA;g 1A2, . . . , gp+rA2;· · ·.
(4)
Theglobal rank-retention procedureis defined as follows.
Letv k denote thek th candidate row in this global order, and
letM k−1 denote the matrix of rows retained after examining
the firstk−1candidate rows, withM 0 empty. The candidate
vk is retained, that is, appended as a new row ofM k−1, if
and only if it increases the rank:
vk is retained⇐ ⇒rank
Mk−1
vk

>rank(M k−1).
Equivalently,
Mk =



 
Mk−1
vk
!
,ifv k is retained,
Mk−1,otherwise.
ThusM k contains exactly the candidate rows retained after
the firstkexaminations. Since a candidate row is retained only
when it increases the rank, the rows of everyM k are linearly
independent.
Although the candidate sequence in the global order (4)
is written indefinitely, only finitely many powers need to be
examined for each generatorg i. By the Cayley–Hamilton
theorem,
An ∈span{I, A, . . . , An−1},
and hence, for every generatorg i,
giAn ∈span{g i, giA, . . . , giAn−1}.
Therefore everyA-generated sequence encounters a dependent
row no later than powern. By Cayley–Hamilton, only powers
up toA n−1 need be considered. Moreover, by the standard
observability-index construction, dependence persists along
eachA-generated sequence: ifg iAq fails to increase the rank
when examined, then so doesg iAq+ℓ for everyℓ≥1.
Lemma 1 (Persistence of dependence):In the global rank-
selection procedure (4), ifg iAq is dependent on the previously
retained rows when it is examined, then every subsequent row
giAq+ℓ, ℓ≥1,is also dependent on the previously retained
rows when it is examined.
Proof:For each stepkin the global order, letS k :=
row(Mk)denote the row space retained after the firstk
examinations. Since retained rows are only added and never
removed,S 0 ⊆S 1 ⊆S 2 ⊆ · · ·.
We will use the following observation: every candidate row
already examined belongs to each subsequent retained-row
space. Indeed, ifv j is retained, thenv j ∈S j; if it is not
retained, thenv j ∈S j−1. Since the spacesS k are nested, in
either case
vj ∈S k, k≥j.
We first show that dependence ofg iAq implies dependence of
the next rowg iAq+1.

===== page 4 =====
4
Supposeg iAq is examined at stepkand is dependent. Then
giAq ∈S k−1.
Hence it can be written as a linear combination of rows
retained before stepk:
giAq = X
ν
ανgjν Asν .
Because each row on the right was examined beforeg iAq,
the global order implies that, for everyν, eithers ν < q,or
sν =qandj ν < i.Multiplying the dependence relation
byAgives
giAq+1 = X
ν
ανgjν Asν +1.
Now letk ′ > kbe the step at whichg iAq+1 is examined. We
claim that every row on the right-hand side has already been
examined before stepk ′. Indeed, ifs ν < q, then
sν + 1≤q < q+ 1,
sog jν Asν +1 occurs in an earlier power block thang iAq+1. If
sν =q, thenj ν < i, sog jν Aq+1 occurs earlier thang iAq+1
within the same power-(q+ 1)block.
Thus every row on the right-hand side has been examined
beforeg iAq+1. By the observation above, each such row
therefore belongs toS k′−1. Consequently,
giAq+1 ∈S k′−1.
Henceg iAq+1 is dependent on the rows retained before its
own examination.
The same argument can now be applied again tog iAq+1,
then tog iAq+2, and so on. Therefore, for everyℓ≥1,
giAq+ℓ
is dependent on the previously retained rows when it is
examined.
Consequently, once the first dependent row in anA-
generated sequence is encountered, no higher power from that
sequence can contribute a new independent direction. The
sequence may therefore be terminated at that point. Since each
generator encounters a dependent row no later than powern,
the ordered rank-retention procedure terminates after finitely
many examinations.
LetMdenote the final matrix formed by the rows retained
by this procedure, listed in the order in which they are retained.
Thus,Mcontains exactly the independent candidate rows
selected by the ordered rank-retention rule. By construction,
its rows are linearly independent, and therefore
rank(M) =number of rows ofM ≤n.
B. Functional-observability indices
The functional-observability indices are read directly from
the retained matrixM. Since
rank
C
L

=p+r,
all generating rowsg 1, . . . , gp+r are retained. Hence, for each
generatorg i, define
αi = 1+max

k≥0 :g iAk is a row ofM 	 , i= 1, . . . , p+r.
Thus the highest retained power associated withg i is
giAαi−1,
whereas
giAαi
is the first dependent row of the correspondingA-generated
sequence. By Lemma 1, all subsequent powers generated by
gi are also dependent.
The integers
α1, . . . , αp+r
are called theordered functional-observability indices.
No regrouping of the rows ofMis required to determine
these indices. For each generator,α i is obtained by identifying
its highest retained power inMand adding one. The rows
themselves remain in the global order induced by (4).
For subsequent use, denote the functional-observability in-
dices associated specifically with the rows ofLby
ηj :=α p+j, j= 1, . . . , r.
Thusη j is the functional-observability index associated with
the generator
gp+j =L j.
C. First-dependence relations
For eachi= 1, . . . , p+r, the functional-observability index
αi identifies the first dependent row of the generatorg i, namely
giAαi .
LetM −i denote the matrix formed by all rows retained strictly
beforeg iAαi is reached in the prescribed global order. By the
rank-retention rule,
giAαi ∈row(M −i ).
Since the rows ofM −i are linearly independent, there exists
a unique coefficient row vectorϕ i such that
giAαi =ϕ iM−i , i= 1, . . . , p+r.(5)
The predecessor matrixM −i may contain retained rows gen-
erated by bothCandL. Every row ofM −i has the form
gjAq
for somej= 1, . . . , p+rand some nonnegative integerq.
The prescribed global examination order implies that such
a row can precedeg iAαi only if
q < αi,
or if
q=α i andj < i.
Thus, at powers strictly belowα i, retained rows from any
generator may occur inM −i , whereas at the terminal power

===== page 5 =====
T . FERNANDO: 5
αi, only retained rows associated with the preceding generators
g1, . . . , gi−1 can occur.
Equation (5) therefore expresses each first dependent row
directly in terms of the rows actually retained before it, while
preserving the ordering induced by the global rank-retention
procedure.
The collection of these dependence relations preserves the
jointC- andL-generated structure of the ordered construction.
This structure will now be used to construct augmented
functional matrices satisfying condition (A).
IV. CONSTRUCTION OFADMISSIBLEFUNCTIONAL
AUGMENTATIONS
The ordered rank-retention construction provides a finite
set of independent directions generated jointly by the rows
ofCandLand their successiveA-iterates. We now use the
associated first-dependence relations to construct augmented
functional matrices
L=
L
R

that satisfy the observer-existence conditions (A) and (S).
Condition (A) requires algebraic closure underA, modulo
the measured directions supplied byCandCA, whereas
condition (S) imposes the corresponding spectral rank require-
ment. We first construct an augmentation satisfying (A).
A. Augmentation required by condition (A)
Condition(A)is
rank


LA
L
CA
C

 = rank


L
CA
C

 .
Equivalently,
row(LA)⊆row


L
CA
C

 .
Thus condition(A)requires theA-image of every row of
Lto belong to the row space generated byL,C, andCA.
For the unaugmented choiceL=L, condition(A)holds if
and only if
row(LA)⊆row


L
CA
C

 .
If this inclusion fails, additional functional directions are
required. The first-dependence relations obtained in Section III
provide the information needed to construct these directions.
B. Construction of the augmentation for condition (A)
For the functional generatorg p+j =L j, j∈ {1, . . . , r}, let
ηj =α p+j.
Then
Lj, LjA, . . . , LjAηj −1
are retained, whereasL jAηj is the first dependent row. Hence,
by (5),
LjAηj =ϕ p+jM−p+j, j= 1, . . . , r.(6)
We refer to (6) as thefirst-dependence relationassociated with
Lj.
PartitionM −p+j according to the powers ofAin its retained
rows:
M−p+j =


G(0)p+jA0
G(1)p+jA1
...
G(ηj )p+j Aηj

 .
HereG (q)p+j consists of those generatorsg i,i= 1, . . . , p+r,
for which the candidate rowg iAq was retained beforeL jAηj
(i.e.,g p+jAηj ) was examined. If no such candidate row exists
for a givenq, thenG (q)p+j is empty.
Partition the coefficient rowϕ p+j conformably as
ϕp+j =

ϕ(0)p+j ϕ(1)p+j · · ·ϕ(ηj )p+j

.
With this partition, the first-dependence relation (6) becomes
LjAηj −
ηjX
q=0
ϕ(q)p+jG(q)p+jAq =0.(7)
IfG (q)p+j is empty for someq, the corresponding term in (7)
is omitted. Writing (7) explicitly in descending powers ofA
gives
LjAηj −ϕ (ηj )p+j G(ηj )p+j Aηj −ϕ (ηj −1)p+j G(ηj −1)p+j Aηj −1 − · · ·
−ϕ(2)p+jG(2)p+jA2 −ϕ (1)p+jG(1)p+jA−ϕ (0)p+jG(0)p+j =0.
The first augmented functional row,ℓ j,ηj −1, is constructed
from the terms on the left-hand side of (7) corresponding to
q= 2, . . . , ηj. Specifically, omit the terms corresponding to
q= 0,1and decrease each remaining power ofAby one.
This gives
ℓj,ηj −1=LjAηj −1 −ϕ (ηj )p+j G(ηj )p+j Aηj −1 −ϕ (ηj −1)p+j G(ηj −1)p+j Aηj −2
− · · · −ϕ(3)p+jG(3)p+jA2 −ϕ (2)p+jG(2)p+jA.
The remaining augmented functional rows are obtained succes-
sively from the preceding row. To obtain the next row, decrease
each positive power ofAby one and discard the last term.
Thus
ℓj,ηj −2=LjAηj −2 −ϕ (ηj )p+j G(ηj )p+j Aηj −2 −ϕ (ηj −1)p+j G(ηj −1)p+j Aηj −3
− · · · −ϕ(4)p+jG(4)p+jA2 −ϕ (3)p+jG(3)p+jA.
Continuing in this way gives
ℓj,2 =L jA2 −ϕ (ηj )p+j G(ηj )p+j A2 −ϕ (ηj −1)p+j G(ηj −1)p+j A,
ℓj,1 =L jA−ϕ (ηj )p+j G(ηj )p+j A,
and finally
ℓj,0 =L j.

===== page 6 =====
6
This construction can be written compactly as
ℓj,t =L jAt −
ηjX
q=ηj −t+1
ϕ(q)p+jG(q)p+jAq−ηj +t,(8)
fort= 1, . . . , ηj −1, with
ℓj,0 =L j.
These functional rows satisfy a first-order recursion. Fort=
0, . . . , ηj −2,
ℓj,tA=ℓ j,t+1 +ϕ (ηj −t)p+j G(ηj −t)p+j A.(9)
For the terminal row, first suppose thatη j >1. Setting
t=η j −1in (8), multiplying byA, and using (7) gives
ℓj,ηj −1A=ϕ (0)p+jG(0)p+j +ϕ (1)p+jG(1)p+jA.(10)
Whenη j = 1, no augmented row is required andℓ j,0 =L j.
In this case, (10) follows directly from (7). Hence (10) holds
for everyη j ≥1.
For each functional generatorL j, define the corresponding
augmentation block by
Rj =


ℓj,ηj −1
...
ℓj,1

 , j= 1, . . . , r.
ThusR j contains theη j −1additional functional rows
constructed from the retainedA-generated sequence ofL j.
Ifη j = 1, no additional row is required andR j is empty.
Stacking these augmentation blocks gives
R=


R1
...
Rr

 .(11)
The augmented functional matrix is therefore
L=
L
R

.(12)
Thus the ordered rank-retention procedure provides the
augmentation matrixRexplicitly. The following result proves
that the resulting augmented functional matrixLsatisfies
condition(A), while the subsequent result proves that the
number of additional rows inRis minimum.
C. Verification of condition (A)
The preceding construction converts each higher-order first-
dependence relation into a sequence of first-order relations.
The following result establishes that the resulting augmented
functional matrix satisfies condition(A).
Theorem 1:LetLbe the augmented functional matrix
constructed in (12), withRdefined by (11). Then
row(LA)⊆row


L
CA
C

 .
HenceLsatisfies condition (A).
Proof:DefineS= row


L
CA
C

 .We prove the result
in two steps:row(LA)⊆S,row(RA)⊆S.
Step 1: Show thatrow(LA)⊆S.
For eachj∈ {1, . . . , r}, by definition of the predecessor
matrixM −p+j, every retained row in the power-η j block
G(ηj )p+j Aηj
was retained beforeL jAηj was examined. At the fixed power
ηj, candidates are examined in the order
C1, . . . , Cp, L1, . . . , Lr.
Therefore,G (ηj )p+j can contain only output generatorsC i and
preceding functional generatorsL 1, . . . , Lj−1. Hence
row

G(ηj )p+j

⊆row


C
L1
...
Lj−1

 ,
and therefore
row

G(ηj )p+j A ⊆row


CA
L1A
...
Lj−1A

 .(13)
Whenj= 1, the functional block


L1A
...
Lj−1A


is absent from the right-hand side of (13).
We now prove by induction onjthat
LjA∈S, j= 1, . . . , r.
Base case:j= 1.
Whenj= 1, there are no preceding functional generators,
so (13) reduces to
row

G(η1)p+1 A ⊆row(CA)⊆S.
Hence
ϕ(η1)p+1G(η1)p+1 A∈S.(14)
Ifη 1 >1, thenℓ 1,0 =L 1, and (9) witht= 0gives
L1A=ℓ 1,1 +ϕ (η1)p+1G(η1)p+1 A.
The first term belongs toSbecauseℓ 1,1 is a row ofL, while
the second term belongs toSby (14). Therefore,
L1A∈S.
Ifη 1 = 1, thenL 1 =ℓ 1,0 is already the terminal row, and
(10) gives
L1A=ϕ (0)p+1G(0)p+1 +ϕ (1)p+1G(1)p+1A.

===== page 7 =====
T . FERNANDO: 7
Since every row ofG (0)p+1 is an original generatorC i orL i,
row

G(0)p+1

⊆row(C, L)⊆row(C,L)⊆S,
we have
ϕ(0)p+1G(0)p+1 ∈row(C, L)⊆S.
Moreover, sinceη 1 = 1, (14) gives
ϕ(1)p+1G(1)p+1A∈S.
Thus
L1A∈S.
This proves the base case.
Induction step.
Letj∈ {2, . . . , r}and assume that
L1A, . . . , Lj−1A∈S.
Then, sincerow(CA)⊆S, (13) implies
ϕ(ηj )p+j G(ηj )p+j A∈S.(15)
Ifη j >1, thenℓ j,0 =L j, and (9) witht= 0gives
LjA=ℓ j,1 +ϕ (ηj )p+j G(ηj )p+j A.
The first term belongs toSbecauseℓ j,1 is a row ofL, while
the second term belongs toSby (15). Hence
LjA∈S.
Ifη j = 1, thenL j =ℓ j,0 is already the terminal row, and
(10) gives
LjA=ϕ (0)p+jG(0)p+j +ϕ (1)p+jG(1)p+jA.
Since every row ofG (0)p+j is an original generatorC i orL i,
row

G(0)p+j

⊆row(C, L)⊆row(C,L)⊆S,
the first term satisfies
ϕ(0)p+jG(0)p+j ∈row(C, L)⊆S.
The second term
ϕ(1)p+jG(1)p+jA
belongs toSby (15), since in this caseη j = 1. Therefore,
LjA∈S.
Thus the induction step is proved. Hence, by induction,
LjA∈Sfor allj= 1, . . . , r,
and therefore
row(LA)⊆S.(16)
Step 2: Show thatrow(RA)⊆S.
Consider first a nonterminal augmented rowℓ j,t, where1≤
t≤η j −2, whenever this index set is nonempty. By (9),
ℓj,tA=ℓ j,t+1 +ϕ (ηj −t)p+j G(ηj −t)p+j A.
The first term belongs toSbecauseℓ j,t+1 is a row ofL.
Every row ofG (ηj −t)p+j is an original generatorC i orL i.
Hence
row

G(ηj −t)p+j A ⊆row(CA, LA).
Therefore,
ϕ(ηj −t)p+j G(ηj −t)p+j A∈row(CA, LA)⊆S,
where the last inclusion follows from the definition ofSand
(16). Thus
ℓj,tA∈S.
It remains to consider the terminal augmented rowℓ j,ηj −1
whenη j >1. By (10),
ℓj,ηj −1A=ϕ (0)p+jG(0)p+j +ϕ (1)p+jG(1)p+jA.
Since every row ofG (0)p+j andG (1)p+j is an original generatorC i
orL i,
row

G(0)p+j

⊆row(C, L),row

G(1)p+jA ⊆row(CA, LA).
Consequently,
ϕ(0)p+jG(0)p+j ∈row(C, L)⊆S,
and
ϕ(1)p+jG(1)p+jA∈row(CA, LA)⊆S,
where the latter inclusion follows from the definition ofS
and (16). Therefore,
ℓj,ηj −1A∈S.
Thus every augmented row inRhas itsA-image inS, and
hence
row(RA)⊆S.
Finally, since
L=

L
R

,
we obtain
row(LA) = row
LA
RA

⊆S= row


L
CA
C

 .
Therefore, condition (A) holds.
Theorem 1 establishes that the constructed augmented func-
tional matrixLsatisfies condition(A). The next result shows
that its augmentation dimension is minimum. Although this
minimum dimension is fixed, the corresponding augmentation
need not be unique: other augmented functional matrices may
also satisfy condition(A)with the same minimum augmenta-
tion dimension.
This nonuniqueness becomes important when condition(S)
is considered. A particular minimum augmentation satisfying
condition(A)may fail condition(S), while another mini-
mum augmentation of the same dimension may satisfy it.
It is therefore necessary to characterize the complete family
of minimum augmentations satisfying condition(A)before
testing condition(S).

===== page 8 =====
8
D. Minimum augmentation for condition (A)
The augmentation construction of Section IV-B provides an
augmented functional matrix satisfying condition (A). We now
show that its augmentation dimension is minimum.
Theorem 2 (Minimum augmentation for condition (A)):
Letη j,j= 1, . . . , r, denote the functional-observability
indices associated with the prescribed functional rowsL j.
Then the minimum number of additional functional rows
required to satisfy condition (A) is
(q0 −r) =
rX
j=1
(ηj −1).
Equivalently, the minimum dimension of an augmented func-
tional matrix satisfying condition (A) is
q0 =
rX
j=1
ηj.
Proof:We prove the result by establishing matching
upper and lower bounds.
Upper bound.For each prescribed functional rowL j, the
construction in Subsection IV-B introducesη j −1additional
rows. Hence the total number of augmented rows is
rX
j=1
(ηj −1).
By Theorem 1, the resulting augmented functional matrix
satisfies condition (A). Therefore,
(q0 −r)≤
rX
j=1
(ηj −1).(17)
Lower bound.Let
eL=
L
eR

, eR∈R eq×n,
be any augmentation satisfying condition (A). We show that
eq≥
rX
j=1
(ηj −1).
Condition (A) implies that, for suitable matricesT,G 0, and
G1,
eLA=T eL+G 0C+G 1CA.
Define
L= eL −G1C.
Then
LA=T L+GC, G:=T G 1 +G 0,
and
row

L
C

= row
 eL
C

.
Since the rows ofLare contained in eL, there exist matrices
PandEsuch that
L=P L+EC.
Repeatedly using LA=T L+GCtherefore gives, for every
k≥0,
LjAk =w j,kL+h j,k,(18)
where
row(hj,k)⊆row


C
CA
...
CA k

 .
Now consider the functional candidate rows retained by the
global rank-selection procedure:
LjAk, j= 1, . . . , r,0≤k < η j.
We claim that the corresponding coefficient rowsw j,k are
linearly independent.
Suppose otherwise, and letw j,k be the first such coefficient
row, in the global examination order, that is a linear combi-
nation of preceding coefficient rows. Then there exist scalars
γi,q such that
wj,k =
X
(i,q)≺(j,k)
γi,qwi,q,
where(i, q)≺(j, k)means that the functional candidateL iAq
is examined beforeL jAk in the global order. Substituting this
relation into (18) and using
wi,qL=L iAq −h i,q
for the preceding functional candidates gives
LjAk = X
(i,q)≺(j,k)
γi,qwi,qL+h j,k
=
X
(i,q)≺(j,k)
γi,qLiAq +h j,k − X
(i,q)≺(j,k)
γi,qhi,q.
Every functional candidateL iAq appearing on the right-
hand side has been examined beforeL jAk. Moreover, since
q≤k, all output-generated rows occurring inh i,q andh j,k
have also been examined beforeL jAk. Every previously
examined row belongs to the span of the rows retained up
to that point, whether it was itself retained or rejected. Hence
LjAk belongs to the span of the rows retained before it is
examined.
LetM − denote the matrix of rows retained immediately
beforeL jAk is examined. Then
rank
 M−
LjAk

= rank(M−).
By the rank-retention rule,L jAk would therefore not be
retained. This contradictsk < ηj, since, by definition ofη j,
Lj, LjA, . . . , LjAηj −1
are all retained. Therefore the coefficient rows
wj,k, j= 1, . . . , r,0≤k < η j,
are linearly independent. There are
rX
j=1
ηj

===== page 9 =====
T . FERNANDO: 9
such rows. Since Lhasr+eqrows, eachw j,k belongs to
R1×(r+eq). Hence rX
j=1
ηj ≤r+eq,
and therefore
eq≥
rX
j=1
(ηj −1).(19)
Since eLwas arbitrary, this lower bound holds for every
augmentation satisfying condition (A). Combining (17) and
(19) gives
(q0 −r) =
rX
j=1
(ηj −1).
Consequently,
q0 =
rX
j=1
ηj.
Remark 2 (Nonuniqueness of the minimum augmentation):
Theorem 2 determines uniquely the minimum augmentation
dimension
(q0 −r) =
rX
j=1
(ηj −1),
but it does not imply uniqueness of the corresponding mini-
mum augmentation subspace.
In general, distinct augmented functional spaces of the
same minimum dimension may satisfy condition (A). The
ordered rank-retention construction selects a particular min-
imum augmentation determined by the prescribed generator
and examination orders. Thus the minimum dimension is
unique, whereas the minimizing augmentation need not be.
V. COMPLETEFAMILY OFMINIMUMCONDITION-(A)
AUGMENTATIONS
Section IV constructs one minimum augmentation satisfying
condition(A)and establishes that the minimum functional
dimension is
q0 =
rX
j=1
ηj.
The minimum augmentation, however, need not be unique.
We now characterize all minimum augmentations satisfying
condition(A).
Let
L=
L
R

be an augmentation of the prescribed functional matrixL.
Since the measured quantityCxis already available, com-
ponents belonging torow(C)do not contribute additional
functional directions.
Let
dC :=n−p,
and choose
NC ∈R n×dC
whose columns form a basis ofkerC. Then
CN C = 0,rank(N C) =d C.
Choose also a left inverse
MC ∈R dC ×n
such that
MCNC =I dC .
Multiplication byN C factors out precisely the measured
directions, since
vNC = 0⇐ ⇒v∈row(C).
Consequently,
rank
C
L

−p= rank(LN C).
Thusrank(LN C)is the number of independent functional
directions represented byLmodulo the measured row space
row(C).
By the standing assumption
rank

C
L

=p+r,
we have
rank(LNC) =r.
Since a minimum augmentation has functional dimension
q0 =
rX
j=1
ηj,
it requires
k:= (q 0 −r) =
rX
j=1
(ηj −1)
additional independent directions beyond those represented by
L. Accordingly, we seek minimum augmentations satisfying
rank(LNC) =r+k=q 0.
Since such anLhas exactlyr+krows, this also implies
rank(L) =r+k=q 0.
We first describe all possible choices of thesekadditional
directions and then impose condition(A).
A. Parameterization of the additional directions
Since
rank(LNC) =r,
there exists a nonsingular matrix
T∈R dC ×dC
such that
LNCT=
 Ir 0 .
Thus, in the coordinates defined byT, the prescribed func-
tional directions occupy the firstrcoordinates.
Set
s:=d C −r=n−p−r.

===== page 10 =====
10
A minimum augmentation must addkindependent directions
to therprescribed directions. By subtracting suitable linear
combinations of the prescribed rows from the additional rows,
every minimum candidate row space can be represented in the
transformed coordinates as

Ir 0
0Y

, Y∈R k×s,rank(Y) =k.
Let
J⊆ {1, . . . , s},|J|=k,
denote a set ofkpivot-column indices. Fork= 0, takeJ=∅
and no parameterΘis required. For eachk >0and suchJ,
choose a permutation matrixΠ J such that, in
YJ (Θ) =
 Ik Θ ΠTJ ,
the columns originating fromI k occupy the positions indexed
byJ, while
Θ∈R k×(s−k)
contains the remaining free columns. Since the columns in-
dexed byJare the columns ofI k, they are linearly indepen-
dent, and therefore
rankY J (Θ) =k
for everyΘ.
Conversely, let
Y∈R k×s,rank(Y) =k.
ThenYcontainsklinearly independent columns. LetJdenote
their indices. A nonsingular row transformation can normalize
these columns toI k, while the remainings−kcolumns form
a matrixΘ∈R k×(s−k). Hence
row(Y) = row
 
YJ (Θ)

for someJandΘ. Consequently, asJranges over allk-
element subsets of{1, . . . , s}andΘranges overR k×(s−k),
the matricesY J (Θ)represent allk-dimensional row spaces in
Rs.
For each pair(J,Θ), define
WJ (Θ) :=
Ir 0
0Y J (Θ)

.
Since
rankY J (Θ) =k,
it follows that
rankW J (Θ) =r+k=q 0.
Thus everyW J (Θ)has the required minimum functional
dimension. It remains only to determine which members of
this family satisfy condition(A).
B. Imposing condition(A)
The preceding parameterization describes all minimum-
dimensional candidates containing the prescribed functional
directions. We now restrict this family to those candidates that
satisfy condition(A). To do so, we first express condition(A)
entirely in the reduced coordinates introduced above.
Lemma 2 (Reduced form of condition(A)):Let
¯A=M CANC, B A =CAN C.
Then condition(A),
row(LA)⊆row


L
CA
C

 ,
is equivalent to
row
 
(LNC) ¯A ⊆row LNCBA  .
Proof:To verify the claim, note first that for any row
vectorv,
v−(vN C)MC
annihilatesN C, since
 
v−(vN C)MC

NC =vN C −vN CMCNC = 0.
Since the columns ofN C spankerC, a row vectorvsatisfies
vNC = 0if and only ifv∈row(C), and it follows that
v−(vN C)MC ∈row(C).
Hence there exists a row vectorγ∈R 1×p such that
v−(vN C)MC =γC,
or equivalently,
v= (vN C)MC +γC.
Applying this rowwise toLgives
L= (LN C)MC + ΓC
for some matrixΓ. Hence
LA= (LN C)MCA+ ΓCA.
Multiplying byN C on the right yields
LANC = (LNC)MCANC + ΓCANC,
and therefore
LANC = (LNC) ¯A+ ΓB A.
Now suppose condition(A)holds, that is,
row(LA)⊆row


L
CA
C

 .
Multiplying byN C gives
row(LANC)⊆row
LNC
BA

,
sinceCN C = 0. Using
LANC = (LNC) ¯A+ ΓB A,

===== page 11 =====
T . FERNANDO: 11
we obtain
row((LNC) ¯A)⊆row
LNC
BA

.
Conversely, suppose
row((LNC) ¯A)⊆row
LNC
BA

.
Then, by the identity above,
row(LANC)⊆row
LNC
BA

.
Hence there exist matricesFandGsuch that
LANC =FLN C +GB A.
Equivalently,
(LA−FL −GCA)N C = 0.
Therefore
row(LA−FL −GCA)⊆row(C),
and thus
row(LA)⊆row


L
CA
C

 .
This is precisely condition(A).
As established above, condition(A)in the reduced coordi-
nates is equivalent to
row(LNC ¯A)⊆row
LNC
BA

.
The matricesW J (Θ)are expressed in the transformed coor-
dinates defined byT. Therefore the same coordinate transfor-
mation must be applied to ¯AandB A. Define
¯AT :=T −1 ¯AT, B A,T :=B AT.
Condition(A)for the candidateW J (Θ)is then
row
 
WJ (Θ) ¯AT  ⊆row WJ (Θ)BA,T  .
This inclusion holds if and only if adding the rows of
WJ (Θ) ¯AT does not increase the rank. Hence condition(A)
is equivalent to
rank


WJ (Θ)
BA,T
WJ (Θ) ¯AT

 = rank
WJ (Θ)
BA,T

.(20)
For each pivot setJ, define
Ω⋆A,J :=
(
Θ∈R k×(s−k) :
rank


WJ (Θ)
BA,T
WJ (Θ) ¯AT

 = rank

WJ (Θ)
BA,T
 )
.
ThusΩ ⋆A,J contains exactly those values ofΘfor which the
corresponding minimum candidate satisfies condition(A).
C. Completeness of the parameterization
We now show that the preceding construction produces
every minimum candidate satisfying condition(A).
Theorem 3:For every
J⊆ {1, . . . , s},|J|=k,
and every
Θ∈Ω ⋆A,J ,
the matrixW J (Θ)is a reduced augmentation of minimum
functional dimension satisfying condition(A).
Conversely, every reduced augmentation of minimum func-
tional dimension satisfying condition(A)is row-equivalent to
WJ (Θ)for at least one pair
(J,Θ),|J|=k,Θ∈Ω ⋆A,J .
Consequently,

WJ (Θ) :J⊆ {1, . . . , s},|J|=k,Θ∈Ω⋆A,J 	
represents, up to row equivalence, the complete family of
reduced augmentations of minimum functional dimension sat-
isfying condition(A).
Proof:First, fix any
J⊆ {1, . . . , s},|J|=k,
and any
Θ∈Ω ⋆A,J .
By construction,
rank
 
YJ (Θ)

=k.
Therefore,
rank
 
WJ (Θ)

=r+k=q 0.
HenceW J (Θ)is a reduced augmentation of minimum func-
tional dimension. Moreover, since
Θ∈Ω ⋆A,J ,
the defining rank condition forΩ ⋆A,J gives
rank


WJ (Θ)
BA,T
WJ (Θ) ¯AT

 = rank
WJ (Θ)
BA,T

.
ThusW J (Θ)satisfies condition(A). Consequently, every
matrix in the stated family is a reduced augmentation of
minimum functional dimension satisfying condition(A).
Conversely, consider any reduced augmentation of mini-
mum functional dimension satisfying condition(A). After
multiplication byN C and application of the coordinate trans-
formationT, its reduced rows have rank
q0 =r+k
and contain the prescribed rows
 Ir 0 .By elementary row
operations, its reduced row space can therefore be represented
in the form Ir 0
0Y

,
whereY∈R k×s,rank(Y) =k.

===== page 12 =====
12
SinceYhas rankk, it contains at least one set ofklinearly
independent columns. Let
J⊆ {1, . . . , s},|J|=k,
denote the indices of any such set. Using the columns indexed
byJas pivot columns, the row space ofYadmits a chart
representation of the form
row(Y) = row
 
YJ (Θ)

for someΘ∈R k×(s−k).It follows that the original reduced
augmentation is row-equivalent toW J (Θ).
Since the original augmentation satisfies condition(A), and
condition(A)depends only on the corresponding reduced row
space, its representativeW J (Θ)also satisfies the transformed
rank condition
rank


WJ (Θ)
BA,T
WJ (Θ) ¯AT

 = rank
WJ (Θ)
BA,T

.
Therefore, by the definition ofΩ ⋆A,J,Θ∈Ω ⋆A,J .
Thus every reduced augmentation of minimum functional
dimension satisfying condition(A)is represented, up to row
equivalence, by at least one matrixW J (Θ)with
J⊆ {1, . . . , s},|J|=k,Θ∈Ω ⋆A,J .
Together with the first part of the proof, this shows that

WJ (Θ) :J⊆ {1, . . . , s},|J|=k,Θ∈Ω⋆A,J 	
represents, up to row equivalence, the complete family of
reduced augmentations of minimum functional dimension sat-
isfying condition(A).
D. Recovery of the augmentation matrix
The matricesW J (Θ)are expressed in transformed reduced
coordinates. We now recover the corresponding augmentation
L=
L
R

in the original state coordinates.
For each admissible pair(J,Θ), returning to the original
reduced coordinates gives
WJ (Θ)T −1 =
 LNC
XJ (Θ)

,
which defines
XJ (Θ)∈R k×dC .
Thus the firstrrows areLN C, whileX J (Θ)contains the
kadditional reduced directions. Recovering the augmentation
therefore amounts to solving
RNC =X J (Θ).(21)
SinceN C has full column rank, this equation is solvable
for everyX J (Θ). Indeed, for any left inverseM C satisfying
MCNC =I dC , a particular solution is
RJ (Θ) =X J (Θ)MC.
since
RJ (Θ)NC =X J (Θ)MCNC =X J (Θ).
Hence
LJ (Θ) =
 L
XJ (Θ)MC

has precisely the reduced rows represented byW J (Θ).
The solution of (21) is not unique. SinceCN C = 0, for any
K∈R k×p,the matrix
R=X J (Θ)MC +KC
satisfies
RNC =X J (Θ)MCNC +KCN C =X J (Θ).
Thus adding rows from the measured row space does not
change the reduced augmentation.
Conversely, letRbe any solution of (21). Then
 
R−X J (Θ)MC

NC = 0.
Since the columns ofN C form a basis forkerCandChas
full row rank,
{v∈R 1×n :vN C = 0}= row(C).
Therefore
R−X J (Θ)MC =KC
for someK∈R k×p. Consequently, all matrix representatives
associated with an admissible pair(J,Θ)are exactly
R=X J (Θ)MC +KC, K∈R k×p.
Hence the complete family of minimum augmented functional
matrices satisfying condition(A)is represented by
L=
 L
XJ (Θ)MC +KC

,(22)
where
J⊆ {1, . . . , s},|J|=k,Θ∈Ω ⋆A,J , K∈R k×p.
Remark 3:The minimum condition-(A)family is
nonempty. Indeed, the chain construction of Section IV
explicitly produces a minimum augmentation satisfying
condition(A). Since the parameterization above is complete,
there exist at least one pivot setJ ⋆ and one parameter value
Θ⋆ ∈Ω ⋆A,J ⋆ .
VI. SPECTRALFEASIBILITY AT THEMINIMUM
CONDITION-(A)ORDER
The preceding development characterizes the complete
family of minimum augmentations satisfying condition(A).
Therefore, the search for a minimum functional observer can
be restricted to matrices of the form (22). It remains to
determine which members of this family also satisfy condition
(S). We now derive a reduced spectral test for this purpose.
Set
dCA :=n−rank

C
CA

,

===== page 13 =====
T . FERNANDO: 13
and choose
NCA ∈R n×dCA ,imN CA = ker
 C
CA

.
Thus
CN CA = 0, CAN CA = 0.
For any minimum condition-(A)augmentationL, define
H:=LN CA, F:=LAN CA, P L(λ) :=λH−F.
The following rank identity removes the directions already
contained inrow(C, CA).
Lemma 3 (Rank reduction):For any matrixMwithn
columns,
rank


M
C
CA

 = rank
 C
CA

+ rank(M NCA).(23)
Proof:Since the columns ofN CA form a basis of
ker
 C
CA

,
a row vectorvsatisfies
vNCA = 0
if and only if
v∈row
 C
CA

.
Hence multiplication byN CA removes precisely the row
directions already contained in
row
 C
CA

.
Therefore the number of independent directions contributed
byMbeyond this row space isrank(M N CA), which gives
(23).
Theorem 4 (Reduced form of condition(S)):LetLbe a
minimum augmentation satisfying condition(A). Then con-
dition(S)is equivalent to
rankP L(λ) = rankH,∀λ∈C.(24)
Proof:Applying Lemma 3 with
M=λL − LA
gives
rank


λL − LA
CA
C

 = rank
 C
CA

+ rank
 
(λL − LA)NCA

.
By definition,
(λL − LA)NCA =λH−F=P L(λ).
Hence
rank


λL − LA
CA
C

 = rank
 C
CA

+ rankP L(λ).
Applying the same lemma withM=Lgives
rank


L
CA
C

 = rank

C
CA

+ rankH.
Therefore condition(S)is equivalent to
rankP L(λ) = rankH,∀λ∈C.
Condition(A)provides an additional useful structure. Since
row(LA)⊆row


L
CA
C

 ,
there exist matricesT L,G 0, andG 1 such that
LA=T LL+G 0C+G 1CA.
Multiplying byN CA and using
CN CA = 0, CAN CA = 0,
gives
F=T LH.
Consequently,
PL(λ) = (λI−T L)H.
If
h:= rank(H),
thenrankP L(λ)≤hfor everyλ. Moreover,λI−T L is
nonsingular for all but finitely manyλ, for which
rankP L(λ) =h.
Thus condition(S)requires
rankP L(λ) =h,∀λ∈C.
A. Finite algebraic spectral test
The reduced spectral condition (24) can be tested alge-
braically for each member of the minimum condition-(A)
family.
Let
h:= rankH.
Ifh= 0, thenH= 0. Since condition(A)gives
F=T LH,
it follows thatF= 0. Hence
PL(λ) = 0,∀λ∈C,
and therefore
rankP L(λ) = 0 = rankH,∀λ∈C.
Thus condition(S)is automatically satisfied.
Suppose now thath >0, and let
∆1(λ), . . . ,∆Nh (λ)
denote allh×hminors ofP L(λ), whereN h denotes the
number of such minors. Since
PL(λ) = (λI−T L)H,
we have
rankP L(λ) =h

===== page 14 =====
14
wheneverλI−T L is nonsingular. Condition(S)therefore
holds if and only ifrankP L(λ) =h,∀λ∈C.Equiva-
lently, the maximal minors
∆1(λ), . . . ,∆Nh (λ)
have no common zero inC. Since these are univariate
polynomials, this is equivalent to requiring that they have no
nonconstant common polynomial factor, or equivalently,
gcd
λ
 
∆1(λ), . . . ,∆Nh (λ)

= 1,(25)
wheregcd λ denotes the greatest common divisor with respect
to the variableλ, normalized up to multiplication by a nonzero
constant.
Combining this algebraic test with the complete param-
eterization of the minimum condition-(A)family gives the
following existence criterion.
Theorem 5 (Existence at the minimum condition-(A)order):
Let
q0 =
rX
j=1
ηj, k= (q 0 −r) =
rX
j=1
(ηj −1), s=n−p−r.
A functional observer of orderq 0 exists with arbitrary
observer-pole assignment if and only if
J⊆ {1, . . . , s},|J|=k,Θ∈Ω ⋆A,J ,
and
K∈R k×p
such that
L=

L
XJ (Θ)MC +KC

satisfies
rankP L(λ) = rankH,∀λ∈C.
Ifh:= rankH= 0, this condition is satisfied automatically.
Ifh >0, it is equivalent to
gcd
λ
 
∆1(λ), . . . ,∆Nh (λ)

= 1,
where∆ 1(λ), . . . ,∆Nh (λ)are theh×hminors ofP L(λ).
Proof:The preceding section characterizes all minimum
augmentations satisfying condition(A)by the parameters
(J,Θ, K)appearing above. Therefore every augmentation of
functional dimensionq 0 satisfying condition(A)is represented
by at least one such choice of(J,Θ, K).
By Theorem 4, a member of this family also satisfies
condition(S)if and only if
rankP L(λ) = rankH,∀λ∈C.
Hence a functional observer of orderq 0 exists if and only if
at least one choice of(J,Θ, K)satisfies this condition.
Ifh= 0, the condition holds automatically, as shown above.
Ifh >0, the preceding maximal-minor argument shows that
it is equivalent to (25).
Remark 4:Theorem 5 is stated for arbitrary observer-
pole assignment. If only asymptotic convergence is required,
the same result holds with the spectral test restricted to
rankP L(λ) = rankH,∀λ∈Cwithℜ(λ)≥0.Thus an
asymptotic functional observer of orderq 0 exists if and only
if at least one member of the minimum condition-(A)family
satisfies this restricted spectral condition.
B. Recovery of the Darouach and Luenberger
Conditions
Theorem 5 recovers the Darouach functional-observer con-
ditions whenLrequires no augmentation and the Luenberger
observability condition whenLspans all state directions not
directly available from the measured output.
Corollary 1 (Recovery of Darouach observer conditions):
Ifq 0 =r, thenk= 0and Theorem 5 reduces to
rank


LA
L
CA
C

 = rank


L
CA
C

 ,andrank


λL−LA
CA
C

 =
rank


L
CA
C

 ,∀λ∈C,which are precisely the Darouach
observer-existence conditions.
Corollary 2 (Recovery of Luenberger observer condition):
LetC∈R p×n have full row rank andL∈R (n−p)×n satisfy
rank

C
L

=n.(26)
Thenη j = 1,j= 1, . . . , n−p, andq0 =n−p. Moreover,
Theorem 5 reduces to
rank

λIn −A
C

=n,∀λ∈C,(27)
the PBH observability condition for(A, C).
Proof:SinceC, Ltogether spanR 1×n, condition(A)
is automatic, givingη j = 1andq 0 =n−p; condition(S)
reduces torank

L(λIn −A);CA;C

=nfor allλ. We show
this equalsrank(λI n −A;C).
LetΦ :=
C
L
−1
= (Φ 1 Φ2), partitioned conformably
withC, L, so thatCΦ 1 =I p,CΦ 2 =0,LΦ 1 =0,LΦ 2 =
In−p. Right-multiplying byΦpreserves rank and gives both
matrices the common form
X Y
Ip 0

, with
Y=Y 1 := (λIn −A)Φ 2 for(λI n −A;C),
Y=Y 2 :=
λIn−p −LAΦ 2
CAΦ 2

for
 
(λIn −A);CA;C)

.
Since
In −X
0I p
 X Y
Ip 0

=
 0Y
Ip 0

has rankp+
rank(Y)for anyY, settingY=Y 1 givesrank(λI n −A;C) =
p+ rank(Y 1), and settingY=Y 2 givesrank

L(λIn −
A);CA;C

=p+ rank(Y 2).
It remains to showrank(Y 1) = rank(Y 2)for ev-
eryλ. Left-multiplyingY 1 by the nonsingular
C
L

gives
 −CAΦ 2
λIn−p −LAΦ 2

, which isY 2 with its two row blocks
swapped and the first negated. Since row-block swaps and

===== page 15 =====
T . FERNANDO: 15
sign changes do not affect rank,rank
 C
L

Y1

= rank(Y2);
and since
C
L

is nonsingular,rank
 C
L

Y1

= rank(Y 1).
Hencerank(Y 1) = rank(Y2), the two original ranks coincide
for everyλ, and (27) follows.
Remark 5 (Constructive decision procedure):The preced-
ing results yield a finite procedure. First, apply the global
rank-retention rule to determineq 0 = Prj=1 ηj.Construct
the complete minimum condition-(A)family and recover the
corresponding augmented functional matrices as in Sections V-
C and V-D. For each admissible representative, form
H=L J (Θ)NCA, F=L J (Θ)ANCA,
and test
rank(λH−F) = rankH,∀λ∈C.
An observer of orderq 0 exists if and only if this test holds for
at least one admissible pair(J,Θ). Once such an augmentation
is found, the observer parameters can be constructed using the
procedure in [6], with the functional matrixLtherein replaced
byL J (Θ).
VII. EXAMPLE
Consider the system (1) withn= 8,p=r= 2, and
A=


−14 3−4 5−1−1 1 0
−3 5 3−2−6 0 8 0
22−17 1−9 8 3−11 0
9−11−2−6 7 1−5 0
21−2 12−14−6 3 2 0
0 1−1 0 0−5 3 0
10−9 1−3 5 1−10 0
0 0 0 0 0 0 0−1

 ,
B=
 e1 e2 +e 8 ,
C=

2−3 0 0 2 0−4 0
−1−10−3 2 5 0−10 0

,
L=

−2 3 1 0−2 0 1 0
−7 8 3 0−6 0 2 0

,
wheree i is thei-th standard basis vector ofR 8. The eighth
state is decoupled from, and unobserved by, the remaining
seven, so that(A, C)is unobservable while the first seven
rows and columns reproduce the finite-dimensional subsystem
examined below.
The functional observability indices are(η 1, η2) = (3,1),
and hence
q0 =η 1 +η 2 = 4.
The conditions for the existence of an order-rfunctional
observer in [6] are not satisfied, and(A, C)is unobservable,
withn 0 = rankO C = 7< n= 8.Thus,
r= 2< q 0 = 4< n0 −p= 5< n−p= 6,
so the minimum dimension permitted by condition(A)is
strictly between the functional dimensionrand the functional-
observability endpointn 0 −p, which itself lies strictly below
the (here inapplicable) reduced-order Luenberger dimension
n−p.
A family of minimum condition-(A)augmentations is
La,b =


−2 3 1 0−2 0 1 0
−7 8 3 0−6 0 2 0
−4a−1 6a+ 2 2a0−4a−1−a2a+ 2 0
2−4b6b+ 1 2b−1−4b−b2b+ 3 0

 ,
a, b∈R,
withrank(L a,b) = 4.Every member satisfies condition(A).
For this family, the maximal minors of the reduced spectral
pencil, up to a common nonzero factor, are
λ+5,−(λ+5) 2,(λ+5) 3−a(λ+5)−b,−  a(λ+5)+b .
Consequently,
La,b satisfies(S)⇐ ⇒b̸= 0.
In particular, the chain augmentationL 0,0 satisfies condi-
tion(A)but fails condition(S)atλ=−5, whereasL 0,1
satisfies both conditions. Therefore, by Theorem 5,
νmin =q 0 = 4.
Thus, spectral failure of one minimum condition-(A)augmen-
tation does not preclude another augmentation of the same
dimension from yielding a minimum-order observer.
It is also instructive to compare this result with the con-
structive procedure of Darouach and Fernando [21]. Forq=
4, the corresponding case isk= 1andµ=r= 2.
For the present example, condition (43) of [21] fails for
every choice ofN, so that procedure proceeds to the next
admissible order. This can be certified directly: the vector
w= (2,0,−6,−3,−6,0,−2,0) T satisfies


C
CA
CA 2

 w= 0,

L
LA

w= 0,
yetLA 2w= (1,1) T ̸= 0; since any row ofLA 2 −N
 L
LA

lying inrow


C
CA
CA 2

 would have to annihilatew, noNcan
satisfy condition (43). The minimum-order characterization
developed here complements that construction by showing,
through the complete family of minimum condition-(A)aug-
mentations, that a spectrally feasible fourth-order realization
nevertheless exists.
To construct such a realization, we apply the functional-
observer design procedure of Darouach [6] toL=L 0,1, with
the functional matrixLtherein replaced byL. Choosing the
eigenvalues ofNasσ(N) ={−2,−3,−4,−6},yields
˙w(t) =


−5 11 1 0
0 0 1 0
0−5−5 1
1−6 0−5

 w(t) +


−50−1
−20−1
31 0
19 0

 y(t)
+


20−30
3−7
−12 7
−14 25

 u(t),

===== page 16 =====
16
with
\Lx(t) =w(t) +


−11 0
−5 0
5−1
6 0

 y(t).
SinceNis Hurwitz, \Lx(t)− → Lx(t).Moreover, since the
first two rows ofLcoincide withL, the desired functional
estimate is
ˆz(t) =
 I2 0 \Lx(t) =w1(t)w2(t) + −11 0−5 0  y(t).
Neither the Darouach nor the Luenberger observer exists here,
yet the minimum-orderq 0 observer proposed in this paper
does, as constructed explicitly above.
VIII. CONCLUSION
This paper has developed a general minimum-order func-
tional observer framework that contains the classical Darouach
functional observer and the reduced-order Luenberger observer
as special cases. The minimum functional dimension per-
mitted by the algebraic condition(A)was characterized by
the functional observability indices, and the complete family
of augmentations attaining this dimension was determined.
Necessary-and-sufficient spectral feasibility conditions were
then established for determining whether the minimum ob-
server order isν min =q 0 = Prj=1 ηj; considering the
complete family is essential, since one minimum condition-
(A)augmentation may fail condition(S)while another aug-
mentation of the same dimension satisfies it.
The general result recovers the Darouach observer and its
necessary-and-sufficient existence conditions whenq 0 =r,
and the reduced-order Luenberger observer and its classical
observability condition whenq 0 =n−p. More generally, when
r < q0 < n−pand spectral feasibility holds, the framework
yields a minimum-order functional observer of intermediate
order that may exist even when neither classical observer is
available.
REFERENCES
[1] D. G. Luenberger, “Observers for multivariable systems,”IEEE Trans.
Autom. Control, vol. AC-11, no. 2, pp. 190–197, Apr. 1966.
[2] T. E. Fortmann and D. Williamson, “Design of a low order observer for
linear feedback control laws,”IEEE Trans. Autom. Control, vol. AC-17,
no. 3, pp. 301–308, Jun. 1972.
[3] P. Murdoch, “Observer design of a linear functional of the state vector,”
IEEE Trans. Autom. Control, vol. AC-18, no. 3, pp. 308–310, Jun. 1973.
[4] K. Furuta and S. Kawaji, “Linear functional observer with possible
minimal dimension,”IEEE Trans. Autom. Control, vol. AC-22, no. 6,
pp. 977–980, Dec. 1977.
[5] H. Trinh, T. D. Tran, and S. Nahavandi, “Design of scalar functional
observers of order less thanν−1,”International Journal of Control,
vol. 79, no. 12, pp. 1654–1659, 2006.
[6] M. Darouach, “Existence and design of functional observers”,IEEE
Trans. Autom. Contr., 45(5), pp. 940-943, 2000.
[7] K. Kumar, A. Prakash, S. K. Parida, S. Ghosh, and C. Kumar, “A
novel multi-functional observer based distributed W ADC for large power
system using modified decoupled control approach,”IEEE Transactions
on Power Systems, vol. 39, no. 5, pp. 6662–6674, doi: 10.1109/TP-
WRS.2024.3351369, 2024.
[8] H. H. Alhelou, M. E. H. Golshan, and N. D. Hatziargyriou, “A
decentralized functional observer based optimal LFC considering un-
known inputs, uncertainties, and cyber-attacks,”IEEE Transactions
on Power Systems, vol. 34, no. 6, pp. 4408–4417, doi: 10.1109/TP-
WRS.2019.2916558, 2019.
[9] D. C. Huong and H. Trinh, “Dynamic event-triggered distributed interval
functional observers for interconnected systems,”Asian Journal of
Control, vol. 25, pp. 2194–2203, doi: https://doi.org/10.1002/asjc.2890,
2023.
[10] Y . Zhang, R. Cheng, and Y . Xia, “On the structural output controllability
and functional observability of undirected networks,”Automatica, vol.
173, Art. no. 112063, 2025.
[11] Y . Zhang, R. Cheng, and Y . Xia, “Observability blocking for functional
privacy of linear dynamic networks,” inProc. 62nd IEEE Conf. on
Decision and Control (CDC), 2023, pp. 7469 7474.
[12] A. N. Montanari, C. Duan, L. A. Aguirre, and A. E. Motter, “Functional
observability and target state estimation in large-scale networks,”Pro-
ceedings of the National Academy of Sciences of the United States of
America, vol. 119, no. 1, e2113750119, Jan. 2022.
[13] A. N. Montanari, C. Duan, A. E. Motter, “Duality between controllability
and observability for target control and estimation in networks”,IEEE
Trans. Autom. Control, 2025, doi: 10.1109/TAC.2025.3552001.
[14] I. Krauss, V . G. Lopez, and M. A. M ¨uller, “On Sample-Based Functional
Observability of Linear Systems,”IEEE Control Systems Letters, pp. 1-
1, doi: http://dx.doi.org/10.1109/LCSYS.2025.3582512, 2025.
[15] S. Muntwiler, J. K ¨ohler, and M. N. Zeilinger, “Nonlinear functional
estimation: Functional detectability and full information estimation,”
Automatica, vol. 171, 2025, Art. no. 111945.
[16] C. Kravaris and S. Venkateswaran, “Functional observers with linear
error dynamics for nonlinear systems,”Systems & Control Letters,
vol. 157, p. 105021, 2021.
[17] T. Fernando, H. Trinh, L. Jennings, “Functional Observability,”Pro-
ceedings of the 2010 Fifth International Conference on Information
and Automation for Sustainability (ICIAfS), Colombo, Sri Lanka, 2010,
pp. 421-423, doi: 10.1109/ICIAFS.2010.5715662.
[18] T. Fernando, H. Trinh, L. Jennings, “Functional observability and the
design of minimum order linear functional observers”,IEEE Trans.
Autom. Contr., 55 (5), pp. 1268-1273, 2010.
[19] T. Fernando, “Unified Eigenvalue–Eigenspace Criteria for Functional
Properties of Linear Systems and a Generalized Separation Principle,”
https://arxiv.org/abs/2602.14909v2, 2026.
[20] L. Jennings, T. Fernando, H. Trinh, “Existence conditions for functional
observability from an eigenspace perspective”,IEEE Trans. Autom.
Contr., 56 (12), pp. 2957-2961, 2011.
[21] M. Darouach and T. Fernando, “On functional observability and func-
tional observer design”,Automatica, vol. 173, 2025, Art. no. 112115.
BIOGRAPHY
Tyrone Fernandoreceived his B.E.
(Hons.) and Ph.D. degrees in Electrical
Engineering from the University of Mel-
bourne, Victoria, Australia, in 1990 and
1996, respectively. In 1996, he joined
the Department of Electrical, Electronic
and Computer Engineering, University of
Western Australia (UW A), Crawley, W A,
Australia, where he currently holds the
position of Professor of Electrical Engi-
neering. He previously served as Associate Head and Deputy
Head of the department from 2008 to 2010.
Prof. Fernando is currently the Head of the Power and
Clean Energy Research Group at UW A. He has provided
professional consultancy to Western Power on the integration
and management of distributed energy resources in the electric
grid. In recognition of his professional contributions, he was
named the Outstanding W A IEEE PES/PELS Engineer in
2018. His research interests include theoretical control, ob-
server design, and power system stability and control. He has
received multiple teaching awards from UW A in recognition
of his contributions to control systems and power systems
education.