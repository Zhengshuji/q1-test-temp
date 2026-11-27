function c371_offset_anchor_equation()
% c371 — Offsetting the anchor to the SECOND entry of L0 turns "column vanishes" into an EQUATION.
%
% Block structure (per block, coordinates 3i-2 .. 3i):
%   C_i = [0 0 1],  A_i(t) = [[0 0 0]; [t 0 0]; [0 1 0]]
%   => K0_i = span{e_{3i-2}} =: N_i,   A_i N_i = t e_{3i-1}.
%   With L0_i = [a b c] the contributions are
%        H's column i   = (a; u_i),      H_A's column i = t (b; w_i).
%
% c369 used a = 1 (anchored) for block 1 and a = b = 0 for block 2, so the H_A column of
% block 2 could vanish by choosing w_2 = 0 WITHOUT t_2 = 0: no equation.  (The c369 "layer 1
% <=> t2 = 0" reading was a sampling artefact: it needed u_2 = w_2 = 0 simultaneously.)
%
% Fix: give block 2 a NONZERO second entry, L0_2 = [0 1 0].  Then
%        H's column 2 = (0; u_2)      (still vanishes when u_2 = 0)
%        H_A's column 2 = t_2 (1; w_2)  vanishes  <=>  t_2 = 0.
% At layer 1 the kernel lemma forces H_A's column 2 to vanish => t_2 = 0.   EQUATION.
%
% This script tests layer 1 and layer 2 feasibility versus t.

  ts = [-1, 0, 1/4, 1, 2];
  fprintf('%8s | %8s %8s   (prediction: layer1 <=> t == 0 ; layer2 <=> t ~= 0?)\n', 't', 'layer1', 'layer2');
  for t = ts
    [C, A, L0] = build(t);
    ok1 = search_layer(C, A, L0, 1, 2, 3000);
    ok2 = search_layer(C, A, L0, 2, 2, 3000);
    fprintf('%8s | %8d %8d\n', rat2str(t), ok1, ok2);
  end
end

function s = rat2str(x)
  [n, d] = rat(x);
  if d == 1, s = sprintf('%d', n); else, s = sprintf('%d/%d', n, d); end
end

function [C, A, L0] = build(t)
  n = 6; C = zeros(2, n); A = zeros(n); L0 = zeros(1, n);
  % block 1: anchored in the FIRST entry, parameter t1 = 1
  C(1,3) = 1; A(2,1) = 1; A(3,2) = 1; L0(1,1) = 1;
  % block 2: anchored in the SECOND entry, parameter t
  C(2,6) = 1; A(5,4) = t; A(6,5) = 1; L0(1,5) = 1;
end

function ok = search_layer(C, A, L0, w_target, mrows, budget)
  N = null(sym([C; C*A]));
  if isempty(N), ok = 0; return; end
  N = double(N);
  H0 = L0*N; HA0 = L0*A*N;
  rng(371);
  ok = 0;
  for t = 1:budget
    R = randi([-2 2], mrows, size(A,1));
    H = round([H0; R*N]); HA = round([HA0; R*A*N]);
    if rank(H) ~= w_target, continue; end
    if rank([H; HA]) ~= w_target, continue; end
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
