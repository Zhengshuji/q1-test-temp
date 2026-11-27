"""精确定位三篇 PDF 的假设，并核对含义"""
import re

paths = {
    "P1": r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\_extract\p1.txt",
    "P2": r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\_extract\p2.txt",
    "P3": r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\_extract\p3.txt",
}

KEY = [
    "full row rank",
    "We further assume",
    "is assumed functional ob",
    "Throughout",
    "redundant measured outputs",
    "redundant functional rows",
    "assumed without loss",
    "It is assumed",
    "no stable uncontrollable",
    "are removed so that",
    "is required to be recoverable",
    "row(L) \u2286 row",
]

for tag, p in paths.items():
    print("=" * 78)
    print(f"  {tag}")
    print("=" * 78)
    lines = open(p, encoding="utf-8").read().split("\n")
    shown = set()
    for i, ln in enumerate(lines):
        for k in KEY:
            if k.lower() in ln.lower():
                lo = max(0, i - 2)
                hi = min(len(lines), i + 4)
                block = "\n".join(f"      {j+1:4d}| {lines[j].strip()[:120]}"
                                  for j in range(lo, hi))
                if block[:80] in shown:
                    break
                shown.add(block[:80])
                print(f"\n  --- 命中 '{k}' @ line {i+1} ---")
                print(block)
                break
    print()
