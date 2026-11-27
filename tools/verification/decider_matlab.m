% decider_matlab.m -- c=1 layer decider (MATLAB symbolic, YES side only)
%
% Pipeline: load A, C -> symbolic -> K0 = null([C; C*A]) -> compression M
%   -> eigenvalues -> for each eigenvalue, eigenvector v -> in the fibre take rational x-samples
%   -> gcd of the omega-minors of lambda*H - H_A -> if gcd = 1, FEASIBLE.

clc;
data = readmatrix('i4246.csv');
n = 8;
p = 2;
A = sym(data(1:n, 1:n));
C = sym(data(n+1:n+p, 1:n));

S = [C; C*A];
fprintf('rank[C;CA] = %d\n', rank(S));
N = null(S);
k = size(N,2);
om = k - 1;
fprintf('k = %d, omega = %d, n-2-p = %d\n', k, om, n-2-p);

G = N.'*N;
M = simplify(G \ (N.'*A*N));

cp = simplify(charpoly(M, 'x'));
fprintf('charpoly = %s\n', char(cp));

ev = eig(M);
fprintf('num eigenvalues: %d\n', numel(ev));

lam = sym('lam');
found = false;
for ii = 1:numel(ev)
    mu = simplify(ev(ii));
    K = null(M - mu*eye(k));
    if size(K,2) == 0
        continue;
    end
    v = simplify(N*K(:,1));
    if rank([v A*v]) ~= 2
        fprintf('  mu: eigen direction of A, skip\n');
        continue;
    end
    fv = v.'*N;
    K0v = null(fv);
    if size(K0v,2) ~= om
        fprintf('  mu: dim(K0 cap vperp) = %d ~= omega, skip\n', size(K0v,2));
        continue;
    end
    W0 = N*K0v;
    Q = null([v A*v].');
    sel = [];
    cur = W0;
    for jj = 1:size(Q,2)
        x = Q(:,jj);
        if rank([cur x]) > size(cur,2)
            cur = [cur x];
            sel = [sel x];
        end
        if size(sel,2) == 3
            break;
        end
    end
    if isempty(sel)
        continue;
    end
    for t = 1:3
        cc = [mod(3*t,5)-2; mod(5*t,7)-3; mod(7*t,11)-5];
        x = sel*cc(1:size(sel,2));
        L = [W0.'; x.'];
        H = simplify(L*N);
        if rank(H) ~= om
            continue;
        end
        HA = simplify(L*A*N);
        if ~all(all(simplify(HA*null(H)) == 0))
            continue;
        end
        P = lam*H - HA;
        polys = sym([]);
        for r = nchoosek(1:size(P,1), om).'
            for c = nchoosek(1:size(P,2), om).'
                d = det(P(r,c));
                if ~all(all(simplify(d) == 0))
                    polys(end+1) = d;
                end
            end
        end
        if isempty(polys)
            continue;
        end
        g = polys(1);
        for q = 2:numel(polys)
            g = gcd(g, polys(q));
        end
        g = simplify(g);
        if all(all(simplify(g - 1) == 0))
            fprintf('  ** FEASIBLE **  x-coeffs = %s\n', mat2str(cc(1:size(sel,2)).'));
            found = true;
            break;
        end
    end
    if found
        break;
    end
end
if ~found
    fprintf('  no good point found (this is not an infeasibility proof)\n');
end
