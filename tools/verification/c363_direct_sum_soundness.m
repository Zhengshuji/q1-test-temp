function c363_direct_sum_soundness()
% c363 — Is the direct-sum AND-composition SOUND?
%
% Danger (297-type): if a block's free data can be set to zero, that block is "switched off"
% and the sum reduces to the remaining blocks.  Then the sum is feasible whenever the OTHER
% blocks are, even if the switched-off block's condition fails  =>  the AND is unsound.
%
% Test: 2-block direct sum, (x1,x2) = (0,1).  Block 1 has x1 = 0, so A_1 N_1 = 0 and the pair
% is (h1, 0) with h1 = (free row) * N_1.  Choose the free row so that its block-1 component is
% orthogonal to N_1  =>  h1 = 0, g1 = 0, block 1 is switched off.
% Then check (5a),(5b) for the sum.

  syms lam
  [C, A, L0] = direct_sum([0 1]);
  W = [C; C*A];
  N = null(sym(W));
  N = double(N);
  H0 = double(L0*N); HA0 = double(L0*A*N);
  n = size(A,1);
  fprintf('k = %d, H0 = %s\n', size(N,2), mat2str(round(H0)));

  % Block 1 spans coordinates 1..3, block 2 spans 4..6.  N_1 = first 3 rows of N.
  N1 = N(1:3, :);
  fprintf('N_1 =\n%s\n', mat2str(round(N1)));

  % Find a block-1 component orthogonal to N_1 (so that h1 = 0).
  % We take the free row's block-1 part = a vector z with N1'*z = 0.
  Z = null(sym(N1'));            % basis of the orthogonal complement of N_1's columns
  Z = double(Z);
  fprintf('dim of {z : N1'' z = 0} = %d\n', size(Z,2));

  rng(363);
  found = 0;
  for trial = 1:50
    if isempty(Z), z1 = zeros(3,1); else, z1 = Z * randi([-2 2], size(Z,2), 1); end
    r2 = randi([-2 2], 1, 3);                    % block-2 part
    R = [z1' r2];
    H = round([H0; R*N]); HA = round([HA0; R*A*N]);
    w = rank(H);
    if w == 0, continue; end
    if rank([H; HA]) ~= w, continue; end          % (5a)
    if symbolic_good(H, HA, w)
      fprintf('  SOUNDNESS VIOLATION: R = %s, omega = %d\n', mat2str(R), w);
      fprintf('     H  = %s\n', mat2str(H));
      fprintf('     HA = %s\n', mat2str(HA));
      found = 1;
      break;
    end
  end
  if ~found
    fprintf('  no violation found in 50 tries (block 1 could not be fully switched off?)\n');
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
