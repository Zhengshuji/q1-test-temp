# sympy 可用：§8.1 的精确消元终于跑起来了（附可靠性条件）

## 目标

用**外部 CAS**（sympy）替代自实现 Buchberger，完成 §8.1 要求的"图卡上精确判定 $\\exists\\theta:(5a)$"。

## 设想与理由

此前纯 Python Buchberger 在 $(5a)$ 的 $(h_0+1)$ 次子式系统上规模爆炸（[attempts/39](39_elimination_attempt.md)）。
用户提示 conda 环境可能有 sympy；检查结果：

```
python → C:\ProgramData\anaconda3-updata\python.exe (3.12.7)
import sympy → 1.13.2   ✓
conda envs: base, comfyui, python312, python312_ai, python312_deeplearning,
            python312_pachong, python312_sim
```

即 **base 环境自带 sympy 1.13.2**（项目此前"纯 Python 无第三方依赖"的约定因此可以放宽，
只要把 CAS 的使用**隔离在单独模块**并标注）。

## 做法

[exact_elimination.py](../../../../tools/verification/exact_elimination.py)：

1. 符号化图卡：$\\mathcal Z=K\\cdot W(\\theta)$，$\\mathcal Z^{\\perp}=K^{\\perp}\\oplus K\\cdot M(\\theta)$（$M$ 为 $W$ 的零化子）；
2. $M_{\\rm res}=[(\\mathcal Z^{\\perp})A^{\\mathsf T}\\ |\\ \\mathcal Z^{\\perp}\\ |\\ W]$、$B=[\\mathcal Z^{\\perp}|W]$；
   采样确定 $h_0=\\operatorname{rank}B$ 的可能取值；
3. **按 $h_0$ 分层**：在该层上 $(5a)\\iff\\operatorname{rank}M_{\\rm res}=\\operatorname{rank}B=h_0$，
   于是取所有 $(h_0+1)$-子式为零，并用 **Rabinowitsch 技巧**（引入 $z$、方程 $zf-1=0$）编码
   "某个 $h_0$-子式 $f\\ne0$"；
4. 每层算 Gröbner（lex/grevlex）：基为 $[1]$ ⟹ 该层空；某层非 $[1]$ ⟹ 该图卡有解；
5. **可靠性条件**：$h_0$-子式必须**全部枚举**（不截断）；当前实现截断在 200 个，
   被截断的"空集"结论一律降级为 `unknown`（工具按此实现，不会输出不可信的 `no`）。

## 进展

| 实例 | 阶 | 图卡 | 判定 | 说明 |
|---|---|---|---|---|
| 公开例子（$n=8,p=r=2$）| $q=3$（3 参数）| 4 个 | 全部 **yes** | $h_0=7$ 层有解 ⟹ $(5a)$ 可满足（与显式 $\\mathcal L$ 一致）|
| 异常实例（$n=7,p=r=2$）| $q=3$（2 参数）| (0,1)、(0,2) | **yes** | $h_0=5,6$ 层有解 |
| 同上 | 同上 | **(1,2)** | **no（certified 空集，$h_0=6$ 层）** | 见证子式未截断时的真证书 |

耗时：公开例子四图卡 + 异常实例三图卡共约 **146 s**（$h_0\\approx7$、$\\le200$ 见证/层）。

**这就是 §8.1 第一个真正的证书**：图卡 `rows=(1,2)` 上 $(5a)$ **无解**（在 $h_0=6$ 层）。

## 最终结论

1. **sympy 可用**（base 环境 1.13.2），精确消元不再受"无 CAS"限制；
2. **工具已实现且默认可靠**：截断即降级为 `unknown`，只在未截断时输出 `no`；
3. 已得到**一个真正的空集证书**（某图卡上 $(5a)$ 不可满足）与两处"可满足"确认；
4. **仍缺**：把"截断"去掉（需枚举全部 $h_0$-子式，代价可达数千次 Gröbner），
   以及对**谱条件**做同样的精确消元（$(5b)$ 需引入 Bézout 辅助变量，变量数会显著增加）。

## 放弃原因

不适用（阶段性完成）。**未做**：全量见证枚举（性能）与谱条件的精确消元（变量规模）。

## 残留价值

* §8.1 的**可运行**实现路线（sympy + 分层 + Rabinowitsch），并给出首个空集证书；
* 明确的**可靠性条件**（见证枚举不得截断），避免再出现"看起来对、其实漏解"；
* 性能基线（146 s / 7 个图卡 / $h_0\\approx7$），可用于判断哪些实例可做完整判定。

## 相关文件

- [tools/verification/exact_elimination.py](../../../../tools/verification/exact_elimination.py)
- [tools/verification/complete_small.py](../../../../tools/verification/complete_small.py)（纯 Python 单参数版）
- [workspace/q1_false/feasibility_geometry/attempts/39_elimination_attempt.md](39_elimination_attempt.md)（自实现 Buchberger 的规模界）
- [CLAUDE.md](../../../../CLAUDE.md) §6（环境：sympy 可用）
