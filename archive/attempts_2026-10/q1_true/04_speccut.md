# 路线 4：谱切割 / 块结构

## 目标
利用 $A$ 的谱（对角、块结构）把"选哪些行"变成"选哪些特征空间/块"，从而编码组合选择。

## 设想与理由
若 $A$ 有多个互异的块，$(5a)$ 的解在块上可以独立选择；直觉上"选块"像集合覆盖。

## 做法
`archive/old_scripts/q1_true_routes/` 的 `c184_spec_cut.py`、`c185_directed_speccut.py`、`c185b.py`、`c186_speccut.py`、`c187_span4.py`：
在 $\mathbb F_3$ 上枚举**全部**子空间，比较 $q_{\text{coord}}$ 与"按块的组合下界"。

## 进展
- $\mathbb F_3$ 上确实出现"需要组合选择"的实例；
- 换到 $\mathbb F_5,\mathbb F_7$ 后，同批实例的"结构"消失 —— 典型小域**伪影**（秩退化）。

## 最终结论
**死**。观测到的"组合结构"不是规律，是 $\mathbb F_p$ 上的偶然退化。

## 放弃原因
无法构造**在 $\mathbb Q$ 上**也成立的"块选择"实例；$\mathbb F_p$ 证据无法提升。

## 残留价值
- 教训进 [CLAUDE.md](../../../CLAUDE.md) 纪律 5/7。
- $\mathbb F_3$ 全子空间枚举工具（`c184`）。

## 相关文件
- `archive/old_scripts/q1_true_routes/`（c184–c187 五个脚本）
- [01_matroid_tap.md](01_matroid_tap.md)
