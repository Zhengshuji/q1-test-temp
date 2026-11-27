function c365_three_block_patterns()
% c365 — 3-block direct sum: test ALL 8 patterns of (x1,x2,x3) with the CORRECTED criterion.
%
% Block i: C_i = [0 0 1], A_i(x) = [[0 0 0]; [x 0 0]; [0 1 0]], L0_i = [1 0 0].
%   =>  H column i      = (1; u_i)        (anchor: first coordinate 1)
%       H_A column i    = x_i * (0; v_i)  (first coordinate 0)
%   =>  if some x_i = 0, that H_A column vanishes while the H column stays anchored.
%
% Corrected criterion for (5b)  rank P(lam) = omega for all lam:
%   (i)  all (omega+1)-minors of P vanish identically;
%   (ii) the omega-minors have no common root.
%
% Expected (AND semantics): feasible  <=>  all x_i ~= 0, i.e. only (1,1,1).

  codes = dec2bin(0:7) - '0';      % 8 rows, 3 columns
  for r = 1:8
    x = codes(r,:);
    [C, A, L0] = direct_sum(x);
    [ok, tried, wit] = search_feasible(C, A, L0, 2, 300);
    [ok3, tried3, ~] = search_feasible(C, A, L0, 3, 300);
    fprintf('  x=(%d,%d,%d): m=2 -> feasible=%d (tested %3d) | m=3 -> feasible=%d (tested %3d) | expected %d\n', ...
            x(1), x(2), x(3), ok, tried, ok3, tried3, all(x~=0));
    if ok || ok3
      fprintf('     witness (m=2): %s\n', mat2str(wit));
    end
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

function [ok, tried, found] = search_feasible(C, A, L0, mrows, budget)
  N = null(sym([C; C*A]));
  if isempty(N), ok = 0; tried = 0; found = []; return; end
  N = double(N);
  H0 = L0*N; HA0 = L0*A*N;
  rng(365);
  ok = 0; tried = 0; found = [];
  for t = 1:budget
    R = randi([-2 2], mrows, size(A,1));
    H = round([H0; R*N]); HA = round([HA0; R*A*N]);
    w = rank(H);
    if w == 0, continue; end
    if rank([H; HA]) ~= w, continue; end        % (5a)
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
  if w+1 <= min(nr, nc)                       % (i) rank <= w identically
    rs1 = nchoosek(1:nr, w+1); cs1 = nchoosek(1:nc, w+1);
    for i = 1:size(rs1,1)
      for j = 1:size(cs1,1)
        if expand(det(P(rs1(i,:), cs1(j,:)))) ~= 0, good = false; return; end
      end
    end
  end
  rs = nchoosek(1:nr, w); cs = nchoosek(1:nc, w);   % (ii) no common root
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
