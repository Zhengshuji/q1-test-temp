function c370_booleanity_gate()
% c370 — Booleanity from the layer structure: one anchored column + two UNanchored columns.
%
% Observation from c369: with exactly ONE anchored column the rank-zero escape is impossible,
% and the unanchored columns can be forced to vanish.  By the kernel lemma (ker H = ker H_A)
% a vanishing column of H forces the corresponding column of H_A to vanish, which is an
% EQUATION in the block parameter.
%
% Construction: columns 1 (anchored, parameter 1), 2 (unanchored, parameter t), 3 (unanchored,
% parameter t-1).   Then:
%   layer 1 (rank 1): every column proportional to the anchor => columns 2,3 vanish
%                     => t = 0 AND t-1 = 0 : impossible.
%   layer 2 (rank 2): exactly one of columns 2,3 vanishes
%                     => t = 0 OR t = 1.
% So "some layer is feasible" should be exactly  t in {0,1}:  BOOLEANITY.
%
% This script scans t and reports whether SOME layer is feasible.

  ts = [-1, -1/2, 0, 1/4, 1/2, 3/4, 1, 3/2, 2];
  fprintf('%8s | %s\n', 't', 'feasible (any layer)   [predicted: t in {0,1}]');
  for t = ts
    [C, A, L0] = build(t);
    ok = any_layer_feasible(C, A, L0, 3, 800);
    pred = (t == 0) || (t == 1);
    fprintf('%8s | %d   (predicted %d)\n', rat2str(t), ok, pred);
  end
end

function s = rat2str(x)
  [n, d] = rat(x);
  if d == 1, s = sprintf('%d', n); else, s = sprintf('%d/%d', n, d); end
end

function [C, A, L0] = build(t)
  n = 9; C = zeros(3, n); A = zeros(n); L0 = zeros(1, n);
  % column block 1: anchored, parameter 1
  C(1,3) = 1; A(2,1) = 1; A(3,2) = 1; L0(1,1) = 1;
  % column block 2: unanchored, parameter t
  C(2,6) = 1; A(5,4) = t; A(6,5) = 1;
  % column block 3: unanchored, parameter t-1
  C(3,9) = 1; A(8,7) = t-1; A(9,8) = 1;
end

function ok = any_layer_feasible(C, A, L0, mrows, budget)
  N = null(sym([C; C*A]));
  if isempty(N), ok = 0; return; end
  N = double(N);
  H0 = L0*N; HA0 = L0*A*N;
  rng(370);
  ok = 0;
  for t = 1:budget
    R = randi([-2 2], mrows, size(A,1));
    H = round([H0; R*N]); HA = round([HA0; R*A*N]);
    w = rank(H);
    if w == 0, continue; end                    % rank-zero escape would be vacuous: excluded by design
    if rank([H; HA]) ~= w, continue; end        % (5a)
    if layer_good(H, HA, w)
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
