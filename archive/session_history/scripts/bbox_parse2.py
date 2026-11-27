"""精确重建 (5a)(5b) 的行块：按行聚类，输出每行的 x 位置与文本"""
import html
import re

p = r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\_extract\bbox2.html"
h = open(p, encoding="utf-8").read()
words = []
for m in re.finditer(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', h
):
    x0, y0, x1, y1 = (float(m.group(i)) for i in range(1, 5))
    words.append((x0, y0, x1, y1, html.unescape(m.group(5))))

# 找 "Condition 1" / "Condition 2" 的 y 位置
for w in words:
    if w[4] in ("Condition", "1", "2") and w[0] > 290:
        pass
conds = [w for w in words if w[4] == "Condition"]
print("Condition 出现位置:")
for c in sorted(conds, key=lambda w: w[1]):
    print(f"   x={c[0]:.1f} y={c[1]:.1f}")

# 取 y 在两个 Condition 之间的所有词
ys = sorted(c[1] for c in conds)
print("\n条件公式区 (y 从", ys[0] - 5, "到", ys[-1] + 40, "):\n")

sel = [w for w in words if w[0] > 290 and ys[0] - 8 <= w[1] <= ys[-1] + 45]
# 按 y 聚类成行（容差 4）
sel.sort(key=lambda w: w[1])
rows, cur, lasty = [], [], None
for w in sel:
    if lasty is None or abs(w[1] - lasty) <= 4.0:
        cur.append(w)
    else:
        rows.append(cur)
        cur = [w]
    lasty = w[1]
if cur:
    rows.append(cur)

for i, r in enumerate(rows):
    r.sort(key=lambda w: w[0])
    txt = " ".join(w[4] for w in r)
    ymin = min(w[1] for w in r)
    xs = f"{r[0][0]:.0f}..{r[-1][2]:.0f}"
    print(f"  行{i:02d}  y≈{ymin:6.1f}  x={xs:>12s}   {txt!r}")

# 额外：打印每个词的精确 x，便于判断矩阵块列位置
print("\n\n=== 公式区每个词的精确位置（按 y 再按 x）===")
for w in sorted(sel, key=lambda w: (round(w[1], 1), w[0])):
    print(f"  y={w[1]:6.1f}  x={w[0]:6.1f}..{w[2]:6.1f}   {w[4]!r}")
