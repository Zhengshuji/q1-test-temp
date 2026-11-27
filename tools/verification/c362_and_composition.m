function c362_and_composition()
% c362 — AND-composition test for the q1 architecture (variables in A, R is the witness).
%
% Block i: C_i = [0 0 1], A_i(x) = [[0 0 0]; [x 0 0]; [0 1 0]], L0_i = [1 0 0]
%   (the "input-nonzero" gate: block i is feasible iff x_i ~= 0).
% Direct sum: C stacked block-diagonally (NOT concatenated), A block diagonal, L0 concatenated.
%
% Feasibility = exists free rows R with
%   (5a) rank[H; HA] = rank H,  and
%   (5b) gcd of the maximal minors of lam*H - HA is a nonzero constant.
%
% Findings (see attempts/362):
%   * C must be stacked block-diagonally; concatenating the 1x3 blocks into ONE row
%     couples K_0 (dim jumps, H0 couples) and every case becomes infeasible.
%   * m (number of free rows) does NOT need to equal the number of blocks: with m = 2
%     the 3-block case is still feasible, at a LOWER layer omega (omega = 2 instead of 3).
%     An earlier "m >= blocks" guess came from too sparse a search and is retracted.
%
% Usage:  matlab -batch "c362_and_composition"

  syms lam
  fprintf('=== 2 blocks (m = 2 free rows) ===\n');
  run_cases([0 0; 0 1; 1 0; 1 1], lam);

  fprintf('=== 3 blocks (m = 3 free rows) ===\n');
  run_cases([1 1 1; 1 1 0; 0 0 1], lam);

  fprintf('=== control: 3 blocks, m = 2 free rows (feasible, at a lower layer) ===\n');
  run_cases([1 1 1], lam, 2);
end

function run_cases(cases, lam, m_override)
  for i = 1:size(cases,1)
    x = cases(i,:);
    [C, A, L0] = direct_sum(x);
    if nargin < 3, mrows = numel(x); else, mrows = m_override; end
    [ok, tried, found] = search_feasible(C, A, L0, mrows, lam, 400);
    fprintf('  x = %s : feasible = %d (expected %d), layer points tested %d\n', ...
            mat2str(x), ok, all(x ~= 0) && (nargin < 3 || all(x ~= 0)), tried);
    if ok, fprintf('     witness R = %s\n', mat2str(found)); end
  end
end

function [C, A, L0] = direct_sum(x)
  k = numel(x); n = 3*k;
  C = zeros(k, n); A = zeros(n); L0 = zeros(1, n);
  for i = 1:k
    C(i, 3*(i-1)+3) = 1;
    A(3*(i-1)+2, 3*(i-1)+1) = x(i);
    A(3*(i-1)+3, 3*(i-1)+2) = 1;
    L0(1, 3*(i-1)+1) = 1;
  end
end

function [ok, tried, found] = search_feasible(C, A, L0, mrows, lam, budget)
  N = null(sym([C; C*A]));                  % exact null basis
  if isempty(N), ok = 0; tried = 0; found = []; return; end
  N = double(N);
  H0 = L0*N; HA0 = L0*A*N;
  rng(362);
  ok = 0; tried = 0; found = [];
  for t = 1:budget
    R = randi([-2 2], mrows, size(A,1));
    H = round([H0; R*N]); HA = round([HA0; R*A*N]);
    w = rank(H);
    if w == 0, continue; end
    if rank([H; HA]) ~= w, continue; end     % (5a)
    tried = tried + 1;
    if numeric_good(H, HA, w) && symbolic_good(H, HA, w)
      ok = 1; found = R; return;
    end
  end
end

function good = numeric_good(H, HA, w)
  lamv = [0, 1, -1, 2, 3] + 0.1234567;       % off-integer samples (cheap necessary test)
  good = true;
  for i = 1:numel(lamv)
    if rank(lamv(i)*H - HA) < w, good = false; return; end
  end
end

function good = symbolic_good(H, HA, w)
  % NOTE: (5b) requires rank P(lam) = w for ALL lam.  That is TWO conditions:
  %   (i)  rank P(lam) <= w identically  <=>  all (w+1)-minors vanish identically;
  %   (ii) rank P(lam) >= w for every lam  <=>  the w-minors have no common root.
  % Forgetting (i) is a real bug: a 3x2 pencil with w = 1 can have rank 2 everywhere.
  persistent lam
  if isempty(lam), lam = sym('lam'); end
  P = lam*sym(H) - sym(HA);
  [nr, nc] = size(P);
  if w > min(nr, nc), good = false; return; end
  % (i) all (w+1)-minors must vanish identically
  if w+1 <= min(nr, nc)
    rs1 = nchoosek(1:nr, w+1); cs1 = nchoosek(1:nc, w+1);
    for i = 1:size(rs1,1)
      for j = 1:size(cs1,1)
        if expand(det(P(rs1(i,:), cs1(j,:)))) ~= 0, good = false; return; end
      end
    end
  end
  rs = nchoosek(1:nr, w); cs = nchoosek(1:nc, w);
  g = sym(0); first = true;
  for i = 1:size(rs,1)
    for j = 1:size(cs,1)
      d = expand(det(P(rs(i,:), cs(j,:))));
      if d ~= 0
        if first, g = d; first = false; else, g = gcd(g, d); end
        if is_constant_nonzero(g), good = true; return; end
      end
    end
  end
  good = ~isempty(g) && is_constant_nonzero(g);
end

function tf = is_constant_nonzero(g)
  p = sym2poly(g);
  tf = (numel(p) == 1) && (p(1) ~= 0);
end
