"""坐标级重建 P3 第 2 页 (5a)(5b) 的行块结构"""
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

print("total words:", len(words))
xs = sorted(w[0] for w in words)
print("x range:", min(xs), max(xs))

# 打印页面右侧栏（公式区）所有 word，按 y 再按 x 排序
sel = [w for w in words if w[0] > 290]
sel.sort(key=lambda w: (round(w[1], 1), w[0]))
print(f"\n右侧栏词数: {len(sel)}\n")
for w in sel:
    print(f"  x={w[0]:7.1f}..{w[2]:7.1f}  y={w[1]:7.1f}..{w[3]:7.1f}   {w[4]!r}")
