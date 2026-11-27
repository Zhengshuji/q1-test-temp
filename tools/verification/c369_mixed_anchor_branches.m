function c369_mixed_anchor_branches()
% c369 — Two-alternative block WITHOUT a rank-zero escape: mix one anchored column
%        with one (or more) unanchored columns.
%
% Motivation (expert 100, task 4): a two-branch block with no rank-zero witness.
%   * EVERY column anchored  => the kernel lemma forces t_i ~= 0 in EVERY layer
%     (H's column is anchored non-zero, so (H_A)'s column cannot vanish), so the
%     layer index produces no branch distinction.
%   * NO column anchored      => R = 0 gives H = H_A = 0, omega = 0, both conditions
%     hold trivially: the rank-zero escape.
%   * ONE column anchored     => omega >= 1 (no rank-zero escape) while the other
%     columns may vanish => LOW LAYERS CAN GIVE CLOSED CONDITIONS.
%
% Claim to test: block 1 anchored with parameter t1, block 2 UNANCHORED with t2.
%   H column 1 = (1;u1),  H_A column 1 = t1(0;v1)
%   H column 2 = (0;u2),  H_A column 2 = t2(0;v2)     (no anchor in block 2)
% Predictions:
%   layer omega = 1  <=>  t2 = 0      (CLOSED condition!)
%   layer omega = 2  <=>  t1 t2 ~= 0  (open)

  fprintf('layer structure for the mixed-anchor block\n');
  fprintf('%8s %8s | %12s %12s\n', 't1', 't2', 'layer1', 'layer2');
  for t1 = [0 1 2]
    for t2 = [0 1 2]
      [C, A, L0] = mixed(t1, t2);
      ok1 = search_layer(C, A, L0, 1, 2, 600);
      ok2 = search_layer(C, A, L0, 2, 2, 600);
      fprintf('%8d %8d | %12d %12d\n', t1, t2, ok1, ok2);
    end
  end
  fprintf('\nPredicted: layer1 <=> t2==0 ; layer2 <=> t1~=0 && t2~=0\n');
end

function [C, A, L0] = mixed(t1, t2)
  n = 6; C = zeros(2, n); A = zeros(n); L0 = zeros(1, n);
  % block 1 (coordinates 1..3): ANCHORED
  C(1,3) = 1; A(2,1) = t1; A(3,2) = 1; L0(1,1) = 1;
  % block 2 (coordinates 4..6): UNANCHORED (L0 has no entry here)
  C(2,6) = 1; A(5,4) = t2; A(6,5) = 1;
end

function ok = search_layer(C, A, L0, w_target, mrows, budget)
  N = null(sym([C; C*A]));
  if isempty(N), ok = 0; return; end
  N = double(N);
  H0 = L0*N; HA0 = L0*A*N;
  rng(369);
  ok = 0;
  for t = 1:budget
    R = randi([-2 2], mrows, size(A,1));
    H = round([H0; R*N]); HA = round([HA0; R*A*N]);
    if rank(H) ~= w_target, continue; end
    if rank([H; HA]) ~= w_target, continue; end     % (5a)
    if layer_good(H, HA, w_target)
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
