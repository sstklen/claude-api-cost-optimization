# 🐾 從「無限貓報恩」到「省錢大絕招」的故事

> The Story Behind These Skills | この Skills が生まれた物語

---

## 🏠 和心村的 28 隻毛孩

在日本房總半島，有一個叫「和心村」的地方，住著 **28 隻貓狗**。

牠們每天做的事很簡單：
- 🐱 曬太陽
- 🐕 在院子裡跑
- 😴 睡覺
- 🎁 偶爾叼東西回家「報恩」

---

## 💡 靈感來源：貓的報恩

貓咪會把「禮物」叼回家——老鼠、蟲子、樹葉。這是牠們的報恩方式。

有一天，我們在做和心村的 **AI 動物辨識系統**，需要研究很多技術：
- 怎麼辨識貓臉？
- ArcFace 還是 Triplet Loss？
- MegaDescriptor 怎麼用？
- 競爭對手 Petnow 怎麼達到 99%？

**一個人根本查不完！**

---

## 🐱 第一個 Skill：無限報恩（Infinite Gratitude）

於是我們想到：

> 「讓 AI 代理像村裡的貓一樣工作吧！」

```
你：「幫我查這個主題」
     ↓
🐱🐱🐱🐱🐱 5-10 個代理出動（平行）
     ↓
🎁🎁🎁🎁🎁 帶回研究發現
     ↓
你：「不錯！但我還想知道更多...」
     ↓
🔄 無限循環直到滿意
```

**成果**：10 個代理、3 波報恩、9 份報告、達成 **77.6% 準確率**！

這就是 **[infinite-gratitude](https://github.com/sstklen/infinite-gratitude)** 的由來。

---

## 💰 第二個 Skill：省錢大絕招

但是，跑了這麼多代理，我們發現一個問題：

> **「API 費用好貴啊！」**

於是我們開始研究怎麼省錢，發現了 Claude API 的三大省錢技巧：

| 技巧 | 節省 | 我們怎麼發現的 |
|------|------|---------------|
| **Batch API** | 50% | 批量生成報告時發現 |
| **Prompt Caching** | 90% | 重複跑相同系統提示時發現 |
| **Extended Thinking** | ~80% | 做策略分析時發現 |

我們把這些經驗整理成 **[claude-api-cost-optimization](https://github.com/sstklen/claude-api-cost-optimization)**。

---

## 🎯 兩個 Skills 的關係

```
和心村 28 隻貓狗
       ↓
啟發了「貓報恩」的概念
       ↓
創造了「無限報恩」多代理研究 Skill
       ↓
跑代理時發現 API 很貴
       ↓
研究出三大省錢技巧
       ↓
創造了「省錢大絕招」Skill
```

**一隻貓的報恩，變成了兩個開源 Skills！**

---

## 📊 實際成果

| 項目 | 數據 |
|------|------|
| 動物辨識準確率 | 77.6% → 82.53% |
| 研究報告產出 | 9 份完整報告 |
| API 費用節省 | ~82% |
| 代理數量 | 10 個平行運作 |

---

## 🌍 品牌理念

```
和牠一起，療癒全世界
Heal the world, together with your pet
ペットと一緒に、世界を癒そう
```

和心村的使命是讓每隻毛孩都能被世界看見。這兩個 Skills 是我們在這條路上的副產品——

**如果它們能幫助到其他開發者，那就是貓咪們的另一種「報恩」了。** 🐾

---

## 📁 Skills 列表

| Skill | 功能 | 連結 |
|-------|------|------|
| **infinite-gratitude** | 多代理平行研究 | [GitHub](https://github.com/sstklen/infinite-gratitude) |
| **claude-api-cost-optimization** | API 省錢技巧 | [GitHub](https://github.com/sstklen/claude-api-cost-optimization) |

---

## 🐾 Credits

Made with 🐾 by **Washin Village**（和心村）

*28 cats & dogs from Japan's Boso Peninsula*

---

> 「貓咪的報恩是叼老鼠回家，工程師的報恩是寫開源 Skills。」
>
> — 和心村 AI 團隊

---

## 🎬 第三章：真實世界驗證（2026-02-02）

### Jelly 的 294 支影片

早上醒來，看到 Anthropic Console 的通知：

```
Batch msgbatch_01C38nrb7AgAefCvpD2sZtqM: 283/283 completed ✓
Batch msgbatch_01LFjKaejJ9JUcX3ZwktMPtV: 283/283 completed ✓
Total cost: $5.32
```

我幾乎不敢相信。

**背景**：我們為和心村的 28 隻貓狗建立了 AI 分身系統。其中一隻叫 Jelly 的黑貓，有 294 支日常影片需要標註（行為、情緒、場景分析）。

**困境**：如果用標準 Message API，成本是 $714.86。我們是動物保護所，這個數字完全超出預算。

**實驗**：昨天晚上，我配置好 Batch API + Prompt Caching：
1. 把標註規範寫成 3,500 tokens 的系統提示
2. 將 294 個請求分為 2 個批次（各 283 個）
3. 加上 `cache_control: {type: "ephemeral"}` 標記
4. 睡前按下「Submit Batch」

**結果**：醒來看到 **$5.32** 的帳單。節省了 **99.3%**。

---

### 數據不會說謊

我打開詳細報告，仔細驗證每個數字：

| 項目 | Token | 原價 | Batch 50% | 實付 |
|------|-------|------|-----------|------|
| Input (no cache) | 102K | $0.306 | ✓ | **$0.51** |
| Cache Write (1h) | 110K | $0.413 | ✓ | **$0.33** |
| Cache Read | 40K | $0.012 | ✓ | **$0.06** |
| Output | 148K | $2.220 | ✓ | **$4.42** |

**關鍵發現 1**: Batch API 的 50% 折扣**不只適用於 Input/Output**，連 **Cache Write 和 Cache Read 都打折**！這是官方文檔沒有明確說明的。

**關鍵發現 2**: 即使極致優化 Input（透過快取），**Output Token 仍佔 83.1% 成本**。下一步優化重點：縮短 AI 回應長度，用結構化 JSON 替代長文本。

**關鍵發現 3**: 快取命中率接近 100%。第一個請求 Cache Write，後續 282 個請求全部 Cache Read。這意味著：
```python
每次請求的系統提示成本 = $0.33 / 283 = $0.0012
vs 無快取 = $0.165 per request
節省 99.3% ✓
```

---

### 為什麼分享這個案例？

1. **真實生產數據** - 不是模擬，不是假設，是真實的 Anthropic 帳單
2. **組合技巧首次驗證** - 首個公開的 Batch API + Prompt Caching 組合案例
3. **成本透明化** - 展示完整的成本結構（Input 16.9% vs Output 83.1%）
4. **非營利視角** - 證明即使預算有限，也能用 AI 做大事

---

### 後續行動

這個驗證讓我決定：

1. ✅ **更新技能包** - 加入 Jelly 案例研究（本次更新）
2. ⏭️ **撰寫進階指南** - Batch API + Prompt Caching 組合策略
3. ⏭️ **開發成本計算工具** - 幫助其他人預估節省金額
4. ⏭️ **分享給 Anthropic** - 讓官方看到真實使用數據

---

### 給讀者的話

如果你的專案：
- 有大量 AI 請求（>100 個）
- 可以等待 24 小時（非即時）
- 使用相同的系統提示
- 成本是重要考量

**那麼這個案例就是為你準備的。** 從 $714 到 $5.32 的旅程，證明了**方法比預算更重要**。

---

_續寫中... 下一章將探討如何將成本降至 $1 以下（透過 Output Token 優化）_

**和心村 (Washin Village)** - 用 AI 讓每隻動物被世界看見
🌐 [washinmura.jp](https://washinmura.jp)
