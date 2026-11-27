import runpy, sys, io
# 复用 build_T_normalized 的函数：直接 exec 并截取
src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\build_T_normalized.py", encoding="utf-8").read()
# 在末尾追加诊断
src += '''

print()
print("=== 诊断 ===")
print("  R  =", [str(x) for x in R[0]])
print("  RNC =", [str(x) for x in RNC[0]])
MC = mm(inv(mm(transpose(NC), NC)), transpose(NC))
print("  MC =", [[str(x) for x in row] for row in MC])
print("  RNC*MC =", [str(x) for x in mm(RNC, MC)[0]])
print("  R_2 := RNC*MC 的 condA =", condA(A, C, toF(L0) + mm(RNC, MC)))
XJ = mm(WJ, Tinv)
print("  XJ[r:] =", [[str(x) for x in row] for row in XJ[r:]])
R2b = mm(XJ[r:], MC)
print("  XJ[r:]*MC =", [str(x) for x in R2b[0]])
print("  R2b 的 condA =", condA(A, C, toF(L0) + R2b))
print("  (RNC*MC) 与 R2b 相同?", mm(RNC,MC) == R2b)
'''
exec(compile(src, "build_T_normalized.py", "exec"))
