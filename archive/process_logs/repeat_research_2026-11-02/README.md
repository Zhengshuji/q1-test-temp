# process —— 流程与事故复盘

> 本目录放**流程层面**的记录：重复研究复盘、协议修订的背景材料、以及其他"为什么这样做"的说明。
> 结论性的规范在 [CLAUDE.md](../../CLAUDE.md)，现状在 [STATUS.md](../../STATUS.md)。

## 文件

| 文件 | 内容 |
|---|---|
| [repeat_research_postmortem_2026-11-02.md](repeat_research_postmortem_2026-11-02.md) | **重复研究事故复盘**：本会话实际发生的 7 处重复（含证据）、根因（读档协议漏 `proof/`、`proof/README` 目录表不全、`STATUS` 只留近几轮、无命题级索引、按自造记号检索）、以及已落地的防复发措施（`claims.tsv` + 第 22 条 + `proof/README` 补全）|
| [5b_map.md](../inventory/5b_map.md) | $(5b)$ 工作的总图（配套 `claims.tsv` 索引）|

## 新会话开工清单（与 CLAUDE.md §7 第 17、22 条一致）

```bash
python tools/hygiene/claim_index.py --grep "<命题形状词>"   # 先按形状检索
python tools/hygiene/claim_index.py --check                  # 索引是否最新
```

然后读 `proof/README.md` 的命题关系表与命中的 `proof/*/README.md`。
