function c366_or_not_gates()
% c366 — OR and NOT gates in the "variables in (A,C,L0)" architecture.
%
% Duality observed:
%   * ANCHORED block (fixed row L0_i = [1 0 0] != 0):
%       H column i = (1; u_i)   -> the anchor cannot be cancelled
%       => the block cannot be switched off  => AND-style composition,
%          and the gate reads  "x ~= 0"  (303C).
%   * UNANCHORED block (L0_i = 0):
%       H column i = (u_i)      -> the free data may set it to zero
%       => the block CAN be switched off    => OR-style composition,
%          and the gate reads  "x = 0".
%
% Tests:
%   (1) single unanchored block, x = 0 : feasible?   x = 1 : infeasible?
%   (2) two unanchored blocks, (x1,x2) in {0,1}^2 : feasible iff (x1==0 or x2==0)?

  codes = [0 0; 0 1; 1 0; 1 1];
  fprintf('=== (2) two UNANCHORED blocks: expect feasible iff some x_i == 0 ===\n');
  for r = 1:4
    x = codes(r,:);
    [C, A] = direct_sum_unanchored(x);
    [ok, tried, wit] = search_feasible(C, A, 2, 400);
    fprintf('  x=(%d,%d): feasible=%d (expected %d), tested %d\n', ...
            x(1), x(2), ok, any(x==0), tried);
    if ok, fprintf('     witness R = %s\n', mat2str(wit)); end
  end

  fprintf('=== (1) single UNANCHORED block ===\n');
  for x = [0 1]
    [C, A] = direct_sum_unanchored(x);
    [ok, tried, ~] = search_feasible(C, A, 1, 400);
    fprintf('  x=%d: feasible=%d (expected %d), tested %d\n', x, ok, (x==0), tried);
  end
end

function [C, A] = direct_sum_unanchored(x)
  k = numel(x); n = 3*k;
  C = zeros(k, n); A = zeros(n);
  for i = 1:k
    C(i, 3*(i-1)+3) = 1;
    A(3*(i-1)+2, 3*(i-1)+1) = x(i);
    A(3*(i-1)+3, 3*(i-1)+2) = 1;
  end
end

function [ok, tried, found] = search_feasible(C, A, mrows, budget)
  N = null(sym([C; C*A]));
  if isempty(N), ok = 0; tried = 0; found = []; return; end
  N = double(N);
  H0 = zeros(mrows, size(N,2)); HA0 = zeros(mrows, size(N,2));  % L0 = 0
  rng(366);
  ok = 0; tried = 0; found = [];
  for t = 1:budget
    R = randi([-2 2], mrows, size(A,1));
    H = round(H0 + R*N); HA = round(HA0 + R*A*N);
    w = rank(H);
    if rank([H; HA]) ~= w, continue; end        % (5a)  (w may be 0: trivial feasible point)
    if w == 0
      ok = 1; found = R; return;                % H = 0, H_A = 0 -> both conditions trivially hold
    end
    tried = tried + 1;
    if numeric_good(H, HA, w) && symbolic_good(H, HA, w)
      ok = 1; found = R; return;
    end
  end
end

function good = numeric_good(H, HA, w)
  lamv = [0, 1, -1, 2, 3] + 0.1234567;
  good = true;
  for i = 1:numel(lamv)
    if rank(lamv(i)*H - HA) ~= w, good = false; return; end
  end
end

function good = symbolic_good(H, HA, w)
  persistent lam
  if isempty(lam), lam = sym('lam'); end
  P = lam*sym(H) - sym(HA);
  [nr, nc] = size(P);
  if w > min(nr, nc), good = false; return; end
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
  if isempty(g), tf = false; return; end
  p = sym2poly(g);
  tf = (numel(p) == 1) && (p(1) ~= 0);
end
