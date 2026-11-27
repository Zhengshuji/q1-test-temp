# paper_drafts —— 交给论文侧的 Markdown 稿

> 本目录放**已成形、准备交给论文侧转 LaTeX** 的稿子。与 `paper/` 的区别：
> `paper/` 只放冻结的 `.tex` 源（§5.6 的唯一事实来源）；本目录放**尚未冻结**的 Markdown 稿与其规格。

## 文件

| 文件 | 内容 | 状态 |
|---|---|---|
| [paper_IV_c2.md](paper_IV_c2.md) | $c=2$ 的论文稿：**Image-Space Reduction and Polynomial-Time Feasibility for Functional Observers with a Two-Dimensional Compressed Kernel**。8 节 + 附录 A（高度链）+ 附录 B（转换须知）；17 个编号环境 | **草稿完成**，交论文侧转 LaTeX |

## 交接要点（给论文侧）

1. **范围标签必须保留**：所有结构陈述都是 **S**（$K_0$-split）；唯一的 **U** 陈述是定理 4。
   专家明确要求每条定理带 S/U 标签。
2. **不得加强的三处**（附录 B 详列）：定理 9 只是单谱分类（注 6 是不能删的免责）；
   定理 12/15 依赖单谱与 $c=2$（注 7 给两条边界与 $n^{O(cn+c^2)}$）；两个预设行条件都不可省（注 3）。
3. **环境编号**：17 项按类型混合顺序编号（命题 1–3、定理 4–9、引理 10、推论 11、定理 12、引理 13–14、
   定理 15–16、命题 17）；若改成分类计数器，必须同步改 IV–VII 的交叉引用。
4. **附录 B 不要印进论文**（里面有机检片段与内部状态）；附录 A 可以印。

## 相关卷宗

- 论文所依据的结果：[attempts/393](../augmentation_family/attempts/393_c2_fibre_and_base.md)（纤维与底）、
  [406](../augmentation_family/attempts/406_eliminate_W.md)（像约化）、[411](../augmentation_family/attempts/411_expert109_audit.md)（可实现性与约化判据）、
  [412](../augmentation_family/attempts/412_rowspace_identity_proof.md)（行空间恒等式一般证明）、
  [413](../augmentation_family/attempts/413_exact_arithmetic_c2.md)（精确算术）、
  [414](../augmentation_family/attempts/414_expert110_audit.md)（二值化与冻结清单）、
  [397](../augmentation_family/attempts/397_layer_nomonotone.md)（不单调反例）
- 测试集规格：[attempts/415](../augmentation_family/attempts/415_test_suite_spec.md)
