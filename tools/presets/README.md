# 学术写作预设（DSH agent preset）

`academic-writing/` 是一个 `@deepseek-ai/dsh-agent-preset` bundle，把本项目的论文写作经验写成一份
persona 章程，供新的写作会话直接选用。

## 它是什么

| | |
|---|---|
| 预设 id | `academic-writing`（显示名 "Academic writing"，roster 顺序 5） |
| 声明行 | `preset-academic-writing` → `@deepseek-ai/dsh-agent-preset` |
| persona | 5.2k 字符，`complete: true`（整段替换默认人格） |
| 工具 | fs（read/write/edit）、fs-search、pwsh/bash（按平台）、jobs、skill、todo、ask-user、web、present、office；子代理组（subagent / subagent_fork / workflow）；compaction 组 |
| 刻意不加 | schedule、goal、plan-mode、plugin-manager/market 工具（写作会话用不到） |

## 章程覆盖的八类经验

1. **诚实性**：不把猜想当定理；不编造引用/编号/页数；区分"改数学结论"与"改文风"。
2. **结构**：一篇一个研究问题；按问题边界拆分；6–8 节；单子节的节是缺陷；贡献表写成"成果→位置"；
   roadmap 只点名 3–6 个关键引理。
3. **证明**：不重推已证引理（要**点明代换**）；不复述已在生效的定义；长证明先给策略句；
   核对被引引理的前提是否在此处成立；检查结论是否真的覆盖所有分支与退化情形；删掉证明末尾的复述。
4. **记号与公式**：一符一义并显式审计重载；未定义即用是缺陷；只给被引用的公式编号
   （中间步骤用 `equation*`，引理里的关键公式可保留编号）；固定等式一侧的符号约定。
5. **算法与复杂度**：算法要定义输入、点名被判定的对象、标注唯一的非初等步骤（是什么问题、什么模型、
   什么代价）；退化分支写成算法内部的条件判断；每条界都要说明是位复杂度还是算术复杂度；参数只声称
   "与 X 无关的不变量"。
6. **更正与局限**：纠正已发表值时只陈述数值矛盾与见证，不推断成因；保留"未声明/开放/纸面级"一节。
7. **工作方法**：每次编译查五项（error、undefined ref、undefined cite、overfull、multiply-defined）；
   在 scratch 目录两遍编译再回拷；大规模审计用**并行只读**评审 + **单人串行**改写。
8. **交付**：不擅自删除；被取代的版本归档而非丢弃；构建产物与源同步。

## 安装位置与更新

- 本目录就是 bundle 源：`package.json` + `cordis.patch.yml`。**改完重新安装**才会生效：
  `plugin_manager` → `install_bundle`，target 指向本目录的绝对路径。
- 已写入 profile：`~/.dsh/profiles/desktop/package.json` 的 `dsh.profile.bundles` 末尾。
- 已有会话保持启动时的预设；**新会话**才能在预设选择器里选到它。

## 注意

- `!!js` 表达式只用于 `disabled`（按平台二选一的 shell 工具），与官方 `standard` 预设的写法一致。
- 若某次改动的插件名不在已安装的包里，声明行会在 roster 上标记诊断而无法组合会话；改名前先对照
  `references/packages.md` 的包清单。
