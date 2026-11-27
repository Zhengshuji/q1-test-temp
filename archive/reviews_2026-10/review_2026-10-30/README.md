# 接手者复核（2026-10-30）

> 这不是项目原有内容。是 2026-10-30 接手本项目的**第二个 AI 会话**在"先读档案、再动手"阶段
> 写下的独立核对脚本，配套文档是 [archive/handovers/HANDOVER2_2026-10-30.md](../../archive/handovers/HANDOVER2_2026-10-30.md)。

## 文件

| 文件 | 作用 |
|---|---|
| `verify_handover2_checks.py` | 三件事：(A) 反例实例不变量；(B)(C) §82 证书脚本的 `% 1` bug（lift 清零 ⟹ V 秩 1 ⟹ 28 子式平凡为零）；(D) λ=0 的一行证明（200/200 随机格子） |

## 跑法

```bash
python workspace/review_2026-10-30/verify_handover2_checks.py
```

全部 `fractions.Fraction` 精确算术，无第三方依赖，约 2 秒。

## 结论（与 HANDOVER2 一致）

1. §82 反例实例的不变量：`rank(A)=2`、`j=3`、`d=3`、`dim B=1`、`μ=1` ✓（这些是对的）。
2. `proof/layer_program/verify_counterexample_certificate.py` 第 61 行的 `% 1` 把 `lift(e_i)` 打成了零向量，
   于是脚本里的 "V" 秩为 1，28 个 6 阶子式**平凡地**为零 —— "0/28" 是 bug 的产物，不是证书。
3. 修掉 `% 1` 后同一个 V 在 λ=1 处的铅笔秩 = 6 ⟹ 至少一个子式非零 ⟹ "全部子式恒为零"**不成立**。
4. **但结论仍然对**，且有一行证明：`rank(A)=2` ⟹ `dim π(C^n A)=1 ≤ ρ−1` ⟹
   λ=0 处 `rank[-LA;CA;C] ≤ j+1 = 4 < 6 = rank[L;CA;C]` ⟹ (5b) 对所有 L 失败 ⟹ 层不可行。
   （200 个随机 (3,1) 格子全部满足该不等式。）
