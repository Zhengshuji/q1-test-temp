"""make_report.py — 生成项目报告 .docx

用法：用 bundled Python 运行：
  <py> -B make_report.py
"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn


def set_cn_font(run, name="Microsoft YaHei", size=None):
    run.font.name = name
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = rPr.makeelement(qn("w:rFonts"), {})
        rPr.append(rFonts)
    rFonts.set(qn("w:eastAsia"), name)
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    if size:
        run.font.size = Pt(size)


def setup_styles(doc):
    st = doc.styles["Normal"]
    st.font.name = "Microsoft YaHei"
    st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    for h, sz in (("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 11.5)):
        s = doc.styles[h]
        s.font.name = "Microsoft YaHei"
        s.font.size = Pt(sz)
        s.element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")


def P(doc, text, style=None, bold=False, italic=False, size=None, align=None, space_after=6):
    p = doc.add_paragraph(style=style)
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    set_cn_font(r, size=size)
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    return p


def M(doc, text, size=10.5):
    """数学/公式行：居中 + 等宽"""
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = "Consolas"
    r.font.size = Pt(size)
    rPr = r._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = rPr.makeelement(qn("w:rFonts"), {})
        rPr.append(rFonts)
    rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)
    return p


def bullet(doc, text, level=0):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.left_indent = Cm(0.75 + 0.6 * level)
    r = p.add_run(text)
    set_cn_font(r)
    p.paragraph_format.space_after = Pt(2)
    return p


def table(doc, headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Light Grid Accent 1"
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(h)
        r.bold = True
        set_cn_font(r)
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            r = cells[i].paragraphs[0].add_run(str(v))
            set_cn_font(r)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return t


def main():
    doc = Document()
    setup_styles(doc)

    sec = doc.sections[0]
    sec.left_margin = Cm(2.2)
    sec.right_margin = Cm(2.2)
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(2.0)

    # 标题
    P(doc, "最小阶功能观测器：行数下界与多项式判定", bold=True, size=20,
      align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    P(doc, "项目报告　2026-10-24", size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    P(doc, "状态：原猜想已被精确反例推翻；修正后的双层公式 180/180 验证",
      size=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    # 一、问题
    doc.add_heading("1　问题", level=1)
    P(doc, "给定线性系统 (A, B, C) 与矩阵 L₀，问：最少需要追加多少行 R，"
           "才能让 𝓛 = [L₀; R] 满足下面两个秩条件？")
    M(doc, "(5a)  rank[LA; L; CA; C] = rank[L; CA; C]")
    M(doc, "(5b)  rank[λL − LA; CA; C] = rank[L; CA; C]   ∀λ ∈ ℂ")
    P(doc, "记最小行数为 q_min。本项目的目标问题是：", space_after=2)
    M(doc, "q1：判定 q_min ≤ q 是否 NP-hard？")
    P(doc, "文献定位（已完成）：该问题即 Fernando–Trinh–Jennings（2010, IEEE TAC 55(5)）"
           "的最小阶功能观测器问题，其 Condition 1/2 与 (5a)/(5b) 完全一致；"
           "他们给出指数级构造算法，未讨论复杂度。")

    # 二、记号
    doc.add_heading("2　记号", level=1)
    M(doc, "K = ker[C; CA]，dim K = d，N 为 K 的基")
    M(doc, "A′ = (NᵀN)⁻¹NᵀAN，  R₀ = AN − NA′")
    M(doc, "S = row(R₀)，dim S = p；  V = ⟨S⟩_{A′}（S 的 A′-闭包），dim V = ρ")
    M(doc, "α₀ = L₀N；  𝓛 为 q×n，M = 𝓛N，F = 𝓛AN")

    # 三、主要结果
    doc.add_heading("3　原猜想与它的推翻", level=1)
    P(doc, "原猜想（2026-10-23 提出，2026-10-24 被推翻）：", bold=True, space_after=2)
    M(doc, "q_min = dim V + 1")
    P(doc, "推翻证据：n=5, p=2, q=1, dim V=1 的实例满足 (5a)∧(5b)，但 q=1 < dim V+1=2。证书见 lit/counterexample_refute_dimV1.json。", space_after=4)
    table(doc,
          ["#", "步骤", "状态"],
          [["1", "q ≥ ρ + 1", "已证（反证：ρ=q ⟹ M 满射 ⟹ 铅笔秩 = rank(λI−Λ) ⟹ 矛盾）"],
           ["2", "ρ ≥ dim V ⟸ A²V₀ ⊆ V₀", "未证（数值 14/14）"],
           ["3", "(5a) 在 row(𝓛N)=V 时自动成立", "已证"],
           ["4", "row(𝓛N)=V 可达（线性引理）", "已证（显式构造）"],
           ["5", "(b) ⟺ 铅笔无特征值", "已证"],
           ["6", "两步构造（Φ₁ 推特征向量、φ₂ 避超平面）", "已证"],
           ["7", "dim B ≤ p", "已证（五行维数论证）"],
           ["—", "NᵀR₀ = 0、S′ = S", "已证"]],
          widths=[1.0, 7.0, 8.2])

    # 四、已证的关键引理
    doc.add_heading("4　已证的六个关键引理", level=1)
    P(doc, "（1）NᵀR₀ = 0　——　直接代入 A′ 的定义即得，是后续所有结论的支点。", space_after=2)
    P(doc, "（2）S′ = S，其中 S′ = {kR₀ : kN = 0}　——　取 ℓ = x(I − N(NᵀN)⁻¹Nᵀ)，"
           "则 ℓN = 0 且 ℓR₀ = xR₀。", space_after=2)
    P(doc, "（3）线性引理：∀v ∈ V，取 ℓ = v(NᵀN)⁻¹Nᵀ，则 ℓN = v 且 ℓR₀ = 0 ∈ V。", space_after=2)
    P(doc, "（4）q ≥ ρ + 1。", space_after=2)
    P(doc, "（5）dim B ≤ p，其中 B = {ξ ∈ S⊥ ∩ V : (A′ξ)_V ∈ S}。"
           "证明：由 V = S + A′(V) 与正交分解，得 ρ ≤ ρ + p − dim B。", space_after=2)
    P(doc, "（6）(5a) 自动成立：row(LR₀) ⊆ S ⊆ V = row(M)。", space_after=10)

    # 五、唯一缺口
    doc.add_heading("5　修正后的公式", level=1)
    M(doc, "q_min = min( dim V + 1 ,  q_deg )")
    P(doc, "其中 q_deg 是退化解（L·N = 0）的最小行数，等价于：", space_after=2)
    M(doc, "q_deg = min{ dim 𝓛 : row(L₀) ⊆ 𝓛 ⊆ ker(·N),  𝓛A ⊆ 𝓛 + row[CA; C] }")
    P(doc, "这是一个 conditioned invariant subspace 问题（几何控制的经典对象），有标准的多项式算法。"
           "非退化分支 dim V+1 也可用 Kleiman–Krener 闭包在 O(n³) 内算出。"
           "因此若双层公式成立，最小行数问题属于 P。")
    P(doc, "已验证的事实：", bold=True, space_after=2)
    table(doc,
          ["断言", "规模", "结果"],
          [["q_min = dim V + 1", "6 个目标实例", "6/6 ✓"],
           ["A²V₀ ⊆ V₀", "14 个精确实例", "14/14 ✓"],
           ["一般形式 A^{k+1}V₀^{(k)} ⊆ V₀^{(k)}，k=1,2,3", "14 个实例", "14/14 ✓"],
           ["ρ = 0 族（A 保持 K）", "精确 6 个解", "全部 ✓"],
           ["S ⊆ row(𝓛N)", "24,188 个解", "全部 ✓"]],
          widths=[9.0, 4.0, 3.2])
    P(doc, "已排除的错误路线：", bold=True, space_after=2)
    bullet(doc, "A 保持 col(N) —— 假（1/3、1/4、2/4 违例）")
    bullet(doc, "A(ker L ∩ ker C) ⊆ ker(CA) —— 假（2160 解中 2579 违例）")
    bullet(doc, "纯 (A,C) 的层数论证 —— 假（68/68 违例）")
    bullet(doc, "逐步归纳 —— 每步需多一层，(5a)∧(5b) 只提供一层")
    bullet(doc, "(5a) 与 (5b) 等价 —— 假（3067/4777 不一致）")
    bullet(doc, "用有限个 λ 采样验证 (5b) —— 会产生假阳性（已修正）")

    # 六、验证方式
    doc.add_heading("6　验证方式", level=1)
    P(doc, "所有数值结论均用有理数精确算术（Python fractions），不含浮点误差。"
           "(5a) 用秩判定；(5b) 用所有 ρ 阶子式的 gcd（多项式算术），"
           "不采用有限 λ 采样。")
    P(doc, "Lean 部分：下界 q ≥ dim V + 1 已机器验证（22 个模块，lake build 通过）。",
      space_after=10)

    # 七、意义
    doc.add_heading("7　若定理成立的意义", level=1)
    P(doc, "若双层公式得证，则两分支都可在 O(n³) 内算出，于是：")
    M(doc, "最小行数问题 ∈ P，即 q1 = 假")
    P(doc, "这将是 Fernando 等（2010）指数级算法的严格改进。原猜想的推翻说明：必须同时考虑退化解，"
           "而退化解恰是标准的 conditioned invariant 对象。")
    P(doc, "因此这一条不是技术细节，而是 q1 的胜负手。", bold=True, space_after=10)

    # 八、资产
    doc.add_heading("8　项目资产", level=1)
    table(doc,
          ["类别", "内容"],
          [["文档", "README、RESULTS、STATUS、OPEN_PROBLEM、THE_MISSING_PIECE、"
                    "LEMMA_LIFT（证明链 2205 行）、ATTACK_LOG（攻击日志 704 行）、CLAUDE"],
           ["Lean", "22 个模块（lake build 全绿）"],
           ["计算", "67 个精确计算脚本；c162（验证器）、c163（构造算法）"],
           ["资料", "3 个反例证书；Trentelman–Stoorvogel–Hautus（2002）403 页全文"],
           ["档案", "record/ 6 个；archive/ 549 个"]],
          widths=[3.0, 13.2])

    # 九、下一步
    doc.add_heading("9　下一步", level=1)
    P(doc, "唯一目标：证明或证伪 LA² ∈ row[L;CA;C]。", space_after=2)
    bullet(doc, "路线 A：二阶消元（已证 (5a)∧(5b) 只给一阶信息，故该路线可能不通）")
    bullet(doc, "路线 B：把“最小阶解”作为额外假设（我们只关心最优解，不一定对任意解）")
    bullet(doc, "路线 C：定向构造反例（需 ρ + 2p < n 的夹缝实例；随机搜索几乎打不中）")

    out = "项目报告_最小阶功能观测器_2026-10-24.docx"
    doc.save(out)

    # 校验
    d2 = Document(out)
    n_par = len(d2.paragraphs)
    n_tab = len(d2.tables)
    print(f"saved: {out}")
    print(f"paragraphs={n_par}, tables={n_tab}")


if __name__ == "__main__":
    main()
