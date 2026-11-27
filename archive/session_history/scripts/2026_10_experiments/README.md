# history/scripts/2026_10_experiments — 实验脚本归档（258 个）

> **这些脚本是"过程"，不是"结论"。**
> 它们记录每条路线怎么试、怎么失败；结论请看 [`../../../RESULTS.md`](../../../RESULTS.md)
> 与 [`../../../OPEN_PROBLEM.md`](../../../OPEN_PROBLEM.md)，过程叙述见 [`../../52_session_conclusion.md`](../../52_session_conclusion.md)。
>
> 归档时间：2026-10-20（工作区整理）。原位置：`scripts/core/`。

---

## 为什么归档到这里

`scripts/core/` 的既定规则是"**只留结论仍有效的脚本**"。多轮会话后该目录膨胀到 298 个脚本，
其中大部分是**一次性探针 / 被后续更正推翻的实验 / 同一实验的多个版本**。
本次按规则把它们移出，保留 41 个（库 + 复现装置 + 结论依据）。

## 这些脚本**不能直接运行**（重要）

它们用 `__file__` 相对定位库文件：

```python
_HERE = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(_HERE, "exact_count_thm7.py"))   # ← 找同目录的库
```

移出 `scripts/core/` 后这一步会失败。**要跑某个脚本，请复制回 `scripts/core/` 再运行**：

```bash
cp history/scripts/2026_10_experiments/c105_verdier_defects.py scripts/core/
python scripts/core/c105_verdier_defects.py
```

## 按家族分类（共 258 个）

| 家族 | 数量 | 内容 | 相关文档 |
|---|---|---|---|
| `c1`–`c136` | 147 | 逐轮实验：判据试错、反例搜索、结构统计 | `history/52`（§7.x 逐条对应） |
| `b1_*`、`b2_*`、`b3_*` | 32 | 支 B 的维数/解数/Gröbner 实验 | `history/28`–`30` |
| `probe_*` | 24 | 定向探针（(A)⟹分解、YES 搜寻、机制定位） | `history/27`、`43` |
| `dir1_*`、`dir2_*` | 10 | 归约（D1）与多项式算法（D2）的尝试 | `history/36` |
| `mainline_*` | 10 | 主线统一、频率量化、见证搜索 | `history/31`–`34` |
| `gen_*` | 5 | 各类实例生成器（含失败的 v1–v4） | `CLAUDE.md` §9 |
| `batch_*` | 4 | 批量验证 c6′（结果后被证伪） | `history/47`–`48` |
| `bridge_*` | 4 | (A)⟹分解 的数值桥接 | `history/43`–`44` |
| `diag_*`、`certify_*` | 4 | 缺陷定位（含库 `solve` 残差 bug 的证书） | `history/27` |
| `caseII_*`、`mechanism_*` | 3 | 情形 II 的平行机制探针 | `CLAUDE.md` §2 |
| `D6_*` | 3 | $q_0$ 下界的模论尝试 | `history/41` |
| `P_*` | 3 | 归约前提（满射性/表达力/可逆性） | `history/35` |
| `routeC_*` | 3 | 路 C（绕开类型障碍） | `history/40` |
| `check_*`、`calibrate_*`、`decide_*` | 3 | 早期校准与判定 | `CLAUDE.md` §2 |
| `verify_*`（早期） | 3 | 已被独立实现取代的验证器 | `history/27` |

> 完整文件名清单（含字节数与修改日期）见 [`FILES.md`](FILES.md)。

## 恢复某个脚本前先看这里

| 想做的事 | 建议 |
|---|---|
| 复现某条**仍然有效**的结论 | 不要用这里；用 `scripts/core/` 里的对应脚本（见其 README 表格） |
| 查"某条错误结论当初怎么来的" | 按 `history/52` 的编号找到对应 `c<N>_*.py` |
| 重跑一个历史实验 | 复制回 `scripts/core/`（库在同一目录） |

## 已知坑（沿用）

- 这些脚本**没有**统一入口，且互相 `exec` 复制过代码；同名逻辑在不同版本里可能不一致。
- 其中少数是**故意保留的反面教材**（如 `b2_mechanism.py` 手写 $W$ 行长度不足、
  `b2_criterion.py` 用错判据、`probe_B_final.py` 未排除零扰动）—— 见 `history/29`、`28`。
