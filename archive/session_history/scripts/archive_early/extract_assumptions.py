"""系统提取三篇 PDF 的假设/前提语句"""
import re

files = {
    "P1": r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\_extract\p1.txt",
    "P2": r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\_extract\p2.txt",
    "P3": r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\_extract\p3.txt",
}

PATTERNS = [
    r"assum", r"Assum", r"without loss", r"WLOG", r"w\.l\.o\.g",
    r"we further", r"throughout", r"Throughout",
    r"full row rank", r"full column rank",
    r"functional(ly)? observable", r"functional observability",
    r"detectab", r"uncontrollable", r"minimal realization",
    r"we consider", r"we require", r"we restrict",
    r"Let .* satisfy", r"suppose", r"Suppose",
    r"rank\(", r"rank\s",
    r"is assumed", r"are assumed",
    r"for simplicity", r"henceforth", r"in the sequel",
]

for tag, path in files.items():
    print("=" * 78)
    print(f"  {tag}  ({path.split(chr(92))[-1]})")
    print("=" * 78)
    try:
        lines = open(path, encoding="utf-8").read().split("\n")
    except Exception as e:
        print("  read error:", e)
        continue
    hits = []
    for i, ln in enumerate(lines):
        for p in PATTERNS:
            if re.search(p, ln):
                hits.append((i + 1, ln.strip()))
                break
    # 去重、去掉明显是参考文献的行
    seen = set()
    for ln_no, txt in hits:
        if not txt or len(txt) < 12:
            continue
        if re.match(r"^\[\d+\]", txt):
            continue
        key = txt[:70]
        if key in seen:
            continue
        seen.add(key)
        print(f"  [{ln_no:4d}] {txt[:150]}")
    print()
