function c367_layer_one_equation()
% c367 — Does "layer omega = 1 is nonempty" encode an EQUATION in x?
%
% Two anchored 303C blocks with parameters t1 = x and t2 = 1-x.
%   H column i   = (1; u_i)          (anchor)
%   H_A column i = t_i (0; v_i)
% Layer omega = 1 requires rank H = 1 and rank P(lam) = 1 for all lam.
%   -- rank H = 1  => the two H columns are proportional => u_1 = u_2 = u.
%   -- lam = 0     => [-t1 w1 | -t2 w2] must have rank 1 => w1, w2 parallel (if both nonzero).
%   -- lam ~= 0    => the two columns must stay proportional; comparing the first coordinates
%                     forces the proportionality coefficient to be 1, hence t1 = t2, i.e. x = 1/2.
% So layer 1 should be nonempty IFF x = 1/2: an EQUALITY (a closed condition), not an open one.
%
% This script scans x and asks whether layer omega = 1 is feasible (exact gcd test at omega = 1).

  xs = [-1, 0, 1/4, 1/2, 3/4, 1, 2];
  for x = xs
    [C, A, L0] = two_blocks(x, 1-x);
    ok = search_layer_one(C, A, L0, 2, 500);
    fprintf('  x = %-6s : layer(omega=1) feasible = %d   (equation predicts %d)\n', ...
            rat2str(x), ok, (x == 1/2));
  end
end

function s = rat2str(x)
  [n, d] = rat(x);
  if d == 1, s = sprintf('%d', n); else, s = sprintf('%d/%d', n, d); end
end

function [C, A, L0] = two_blocks(t1, t2)
  n = 6; C = zeros(2, n); A = zeros(n); L0 = zeros(1, n);
  % block 1: coordinates 1..3, parameter t1
  C(1,3) = 1; A(2,1) = t1; A(3,2) = 1; L0(1,1) = 1;
  % block 2: coordinates 4..6, parameter t2
  C(2,6) = 1; A(5,4) = t2; A(6,5) = 1; L0(1,4) = 1;
end

function ok = search_layer_one(C, A, L0, mrows, budget)
  N = null(sym([C; C*A]));
  if isempty(N), ok = 0; return; end
  N = double(N);
  H0 = L0*N; HA0 = L0*A*N;
  rng(367);
  ok = 0;
  for t = 1:budget
    R = randi([-2 2], mrows, size(A,1));
    H = round([H0; R*N]); HA = round([HA0; R*A*N]);
    if rank(H) ~= 1, continue; end                 % we ask for THIS layer only
    if rank([H; HA]) ~= 1, continue; end           % (5a)
    if layer_good(H, HA, 1)
      ok = 1; return;
    end
  end
end

function good = layer_good(H, HA, w)
  persistent lam
  if isempty(lam), lam = sym('lam'); end
  P = lam*sym(H) - sym(HA);
  [nr, nc] = size(P);
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
