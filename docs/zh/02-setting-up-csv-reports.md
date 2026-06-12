---
title: "设置你的 CSV 报告"
description: "Google Authorized Buyers 没有报告 API，因此 Cat-Scan 从五份计划的 CSV 报告重建漏斗。完整指标和维度参考以及设置指南。"
---

# 设置你的 CSV 报告

*适用读者：媒体买家、账户经理*

在 Cat-Scan 能够分析任何内容之前，它需要数据。Google Authorized Buyers 没有报告 API，因此所有数据都通过**五份计划的 CSV 报告**流动，这些报告你只需在 Google AB 账户中创建一次。

!!! warning "为什么需要五份单独的报告？"
    Google 的报告列并非全部相互兼容。例如，“竞价请求”不能与“移动应用 ID”或“创意 ID + 账单 ID”出现在同一报告中。要获得完整的漏斗可见性，你需要五份 Cat-Scan 会自动合并的报告。

## 五份报告一览

| # | 报告名称 | 它告诉 Cat-Scan 什么 | 关键列 |
|---|----------|----------------------|--------|
| 1 | **Quality** | 带可见性的创意级性能 | Billing ID、Creative ID、Impressions、Spend、Active View |
| 2 | **Bids in Auction** | 创意级出价管道（出价 -> 胜出） | Creative ID、Bids、Bids in auction、Auctions won |
| 3 | **Pipeline -- Geo** | 按国家划分的完整竞价流漏斗 | Bid requests、Country、Reached queries、Impressions |
| 4 | **Pipeline -- Publisher** | 按发布商划分的完整竞价流漏斗 | Bid requests、Publisher ID、Publisher name |
| 5 | **Bid Filtering** | Google 为什么拒绝你的出价 | Filtering reason、Bids、Opportunity cost |

---

## 完整指标参考

Cat-Scan 摄取的每个指标、它的含义，以及哪个报告携带它。

### 漏斗指标（竞价流管道）

这些跟踪竞价请求通过 Google 拍卖系统的过程。
存在于 **Pipeline -- Geo** 和 **Pipeline -- Publisher** 报告中。

| 指标 | 定义 | 单位 | 报告 |
|------|------|------|------|
| **Bid requests** | Google 发送到你竞价器端点的总竞价请求。这是原始入站量——漏斗的顶部。包括你的竞价器可能未及时响应的请求。 | 计数 | Pipeline -- Geo, Pipeline -- Publisher |
| **Reached queries** | 实际到达你的竞价器并获得响应（成功或不成功）的竞价请求。如果你的竞价器有延迟问题或超时，则低于“Bid requests”。 | 计数 | Pipeline -- Geo, Pipeline -- Publisher |
| **Inventory matches** | 你的竞价器找到匹配库存（适合请求的素材）的请求。这是第一个过滤器：如果你没有适合请求尺寸/格式的素材，它就会在这里停止。 | 计数 | Pipeline -- Geo, Pipeline -- Publisher |
| **Successful responses** | 你的竞价器返回有效、可解析出价响应的请求（HTTP 200 且格式良好的出价）。不包括超时、错误和无出价。 | 计数 | Pipeline -- Geo, Pipeline -- Publisher |
| **Bids** | 你的竞价器实际放置的出价响应。成功响应的子集——你的竞价器可能成功响应但选择不出价（无出价响应）。 | 计数 | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction, Bid Filtering |
| **Bids in auction** | 被 Google 接受进入拍卖的出价。由于过滤规则（创意未批准、政策违规、底价、预定向排除），出价可能在进入拍卖前被拒绝。“Bids”与“Bids in auction”之间的差距显示在 Bid Filtering 报告中。 | 计数 | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Auctions won** | 赢得拍卖的出价。你为这些付费。“Bids in auction”与“Auctions won”之间的差距是竞争——其他买家出价高于你。 | 计数 | Pipeline -- Geo, Pipeline -- Publisher, Bids in Auction |
| **Impressions** | 赢得拍卖后实际在用户浏览器或应用中渲染的广告。由于广告渲染失败、渲染前页面导航和广告拦截器干扰，略少于“Auctions won”。 | 计数 | 所有五份报告 |
| **Clicks** | 用户对你展示的广告的交互（点击/轻触）。 | 计数 | Pipeline -- Geo, Pipeline -- Publisher, Quality |

### 花费和成本指标

| 指标 | 定义 | 单位 | 报告 |
|------|------|------|------|
| **Spend** | 期间赢得展示的总花费。这是你实际的媒体成本。以你账户的货币计价（通常是 USD）。 | 货币（原始数据为 micros，UI 中为美元） | Quality |
| **Opportunity cost** | 因为 Google 在出价进入拍卖前过滤了你的出价而导致你损失的估计收入。由 Google 根据类似库存的历史胜出率和 CPM 计算。用于优先考虑首先修复哪些过滤原因。 | 货币 | Bid Filtering |

### 质量和可见性指标

这些是来自 **Quality** 报告的创意级指标。它们衡量展示被投放*之后*发生的事情。

| 指标 | 定义 | 单位 | 报告 |
|------|------|------|------|
| **Active View viewable** | 符合 MRC 可见性标准的展示：至少 50% 的广告像素在浏览器可视区域内至少连续 1 秒（视频为 2 秒）。这是“广告是否真正被看到”的行业标准。 | 计数 | Quality |
| **Active View measurable** | 可见性*可以*被测量的展示。某些环境（某些应用、跨域 iframe、旧浏览器）会阻止测量。可见性率 = Active View viewable / Active View measurable。 | 计数 | Quality |
| **Video starts** | 视频创意开始播放的次数。仅对视频格式的素材填充。 | 计数 | Quality |
| **Video completions** | 视频创意播放到 100% 完成（或可跳过时的跳过点）的次数。视频完成率 = completions / starts。 | 计数 | Quality |

### 出价过滤指标

来自 **Bid Filtering** 报告。这些告诉你 *为什么* 出价在进入拍卖前被 Google 拒绝。

| 指标 | 定义 | 单位 | 报告 |
|------|------|------|------|
| **Bids** | 你的竞价器放置的总出价（与上面的定义相同）。在此报告中，用作计算过滤率的 分母。 | 计数 | Bid Filtering |
| **Bids in auction** | 存活过滤并进入拍卖的出价。`Bids - Bids in auction` = 总过滤出价。 | 计数 | Bid Filtering |
| **Opportunity cost** | 见上面的花费指标。在此报告中，按每个过滤原因细分，以便你可以看到哪个原因 costing 你最多。 | 货币 | Bid Filtering |

### 维度（分组列）

维度不是指标——它们是指标沿其拆分的轴。Cat-Scan 使用这些来切片你的数据。

| 维度 | 它是什么 | 哪些报告 |
|------|----------|----------|
| **Day** | 日历日期（UTC）。所有报告中必需。Cat-Scan 使用此进行去重和时间序列显示。 | 所有五份 |
| **Hour** | 一天中的小时（0--23，UTC）。在管道分析中启用小时粒度。 | Pipeline -- Geo, Pipeline -- Publisher |
| **Country** | 两位 ISO 国家代码（例如 US、DE、IL）。竞价请求的地理来源。 | Quality, Bids in Auction, Pipeline -- Geo, Bid Filtering（可选） |
| **Billing ID (Pretargeting config)** | 接受此流量的预定向配置的数字 ID。在 Cat-Scan 中 1:1 映射到配置卡。 | Quality |
| **Creative ID** | Google 为素材资产分配的数字 ID。链接到 Cat-Scan 中的素材库。 | Quality, Bids in Auction, Bid Filtering（可选） |
| **Creative size** | 素材的像素尺寸（例如 `300x250`、`728x90`）。用于基于尺寸的浪费分析。 | Quality |
| **Creative format** | 广告格式：`DISPLAY_IMAGE`、`DISPLAY_HTML`、`VIDEO`、`NATIVE`。 | Quality（可选） |
| **Platform** | 设备平台：`DESKTOP`、`MOBILE_APP`、`MOBILE_WEB`、`CONNECTED_TV`。 | Quality（可选） |
| **Environment** | 广告投放位置：`WEB`、`APP`。 | Quality（可选） |
| **App ID** | 移动应用包 ID（例如 `com.example.app`）。仅针对应用内库存填充。 | Quality（可选） |
| **App name** | 人类可读的应用名称。 | Quality（可选） |
| **Publisher ID** | 发布商（网站或应用）的数字 ID。 | Quality（可选）、Pipeline -- Publisher |
| **Publisher name** | 人类可读的发布商名称。 | Quality（可选）、Pipeline -- Publisher |
| **Publisher domain** | 发布商网站的域名（例如 `news.example.com`）。 | Quality（可选） |
| **Buyer account ID** | 你的买方账户 / 席位 ID。在你运行多个席位时需要。 | Bids in Auction, Bid Filtering（可选） |
| **Filtering reason** | Google 在出价进入拍卖前被过滤的原因代码（例如 `CREATIVE_NOT_APPROVED`、`BID_BELOW_AUCTION_FLOOR`、`DISAPPROVED_BY_EXCHANGE`）。 | Bid Filtering |

---

## 分步：创建每份报告

### 1. Quality 报告

这是你的带可见性和花费数据的创意级性能报告。

**在 Google Authorized Buyers -> Reporting -> New Report 中：**

| 设置 | 值 |
|------|----|
| 报告类型 | RTB |
| 时间范围 | 昨天（每日计划） |
| 维度 | Day, Billing ID (Pretargeting config), Creative ID, Creative size, Country |
| 可选维度 | Hour, Creative format, Platform, Environment, App ID, App name, Publisher ID, Publisher name, Publisher domain |
| 指标 | Reached queries, Impressions, Clicks, Spend |
| 可选指标 | Video starts, Video completions, Active View viewable, Active View measurable |

**建议文件名：** `catscan-quality`

!!! note
    此报告**不得**包含“Bid requests”、“Bids”或“Bids in auction”——这些列与 Google 报告中的“Billing ID”不兼容。

---

### 2. Bids in Auction 报告

此报告在创意级别捕获出价管道，填补 Quality 报告无法包含的指标。

| 设置 | 值 |
|------|----|
| 报告类型 | RTB |
| 时间范围 | 昨天（每日计划） |
| 维度 | Day, Country, Creative ID, Buyer account ID |
| 指标 | Bids in auction, Auctions won, Bids, Impressions |

**建议文件名：** `catscan-bidsinauction`

!!! info "Cat-Scan 如何合并这些"
    Quality + Bids in Auction 在 `(Day, Creative ID)` 上合并，为你提供完整画面：从放置出价到展示投放和产生的花费。

---

### 3. Pipeline -- Geo 报告

这是你的漏斗顶部报告：Google 按国家向你发送多少竞价请求，以及每个漏斗阶段有多少存活。

| 设置 | 值 |
|------|----|
| 报告类型 | RTB |
| 时间范围 | 昨天（每日计划） |
| 维度 | Day, Country, Hour |
| 指标 | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**建议文件名：** `catscan-pipeline-geo-{account_id}-yesterday-UTC`

!!! warning
    **不要**向此报告添加 Creative ID、Billing ID 或 App ID。这些列与“Bid requests”不兼容。

---

### 4. Pipeline -- Publisher 报告

与 Pipeline -- Geo 相同，但按发布商（而非或除了地理）细分。

| 设置 | 值 |
|------|----|
| 报告类型 | RTB |
| 时间范围 | 昨天（每日计划） |
| 维度 | Day, Country, Hour, Publisher ID, Publisher name |
| 指标 | Bid requests, Reached queries, Inventory matches, Successful responses, Bids, Bids in auction, Auctions won, Impressions, Clicks |

**建议文件名：** `catscan-pipeline-{account_id}-yesterday-UTC`

---

### 5. Bid Filtering 报告

此报告向你展示 *为什么* Google 在出价进入拍卖前过滤你的出价——对诊断预定向问题至关重要。

| 设置 | 值 |
|------|----|
| 报告类型 | RTB |
| 时间范围 | 昨天（每日计划） |
| 维度 | Day, Filtering reason |
| 可选维度 | Country, Buyer account ID, Creative ID |
| 指标 | Bids, Bids in auction, Opportunity cost |

**建议文件名：** `catscan-bid-filtering`

### 常见过滤原因

这些是你将在 **Filtering reason** 维度中看到的值。每一个都告诉你 Google 在进入拍卖前拒绝出价的具体原因。

| 过滤原因 | 含义 | 该怎么做 |
|----------|------|----------|
| `CREATIVE_NOT_APPROVED` | 素材未通过 Google 审核，或已被否决 | 在 Google AB 中检查素材状态。修复政策违规。 |
| `BID_BELOW_AUCTION_FLOOR` | 你的出价价格低于发布商的最低 CPM | 提高出价或通过预定向排除低价值库存 |
| `DISAPPROVED_BY_EXCHANGE` | Google 的交易所级政策阻止了出价 | 查看 Google 针对特定素材的广告政策 |
| `FILTERED_BY_PRETARGETING` | 你自己的预定向规则排除了此流量 | 如果你的规则正确则是有意的；如果意外则审查 |
| `NO_MATCHING_CREATIVE` | 竞价请求要求的尺寸/格式你没有 | 为缺失的尺寸上传素材，或在预定向中排除这些尺寸 |
| `CREATIVE_SIZE_MISMATCH` | 素材尺寸与广告位不匹配 | 检查素材尺寸与发布商请求的内容 |
| `LANDING_PAGE_DISAPPROVED` | 目标 URL 未通过 Google 审核 | 修复落地页或使用不同的 URL |
| `SSL_REQUIRED` | 发布商要求 HTTPS，但你的素材或落地页使用 HTTP | 将所有资产和 URL 切换到 HTTPS |
| `FREQUENCY_CAPPED` | 用户已经看到此素材太多次 | 预期行为；如果过于激进则调整频次上限 |

---

## 安排交付

对于五份报告中的每一份：

1. 在 Google Authorized Buyers 中点击 **Schedule**。
2. 将频率设置为 **Daily**。
3. 设置交付方式：
   - **Email** —— 发送到连接到 Cat-Scan 的 Gmail 账户（启用自动导入）。有关 Gmail 自动导入设置，请参阅 [数据导入](09-data-import.md)。
   - **Manual** —— 如果你更喜欢自己通过 `/import` 下载和上传 CSV。

!!! tip "使用 Gmail 自动导入"
    将所有五份报告安排为发送到连接的 Gmail 账户意味着 Cat-Scan 每天自动导入它们。初始设置后无需手动上传。

## 验证你的设置

在导入第一组 CSV 后（手动或通过 Gmail）：

1. 在 Cat-Scan 中转到 `/import`。
2. 检查 **数据新鲜度网格**——你应该看到昨天日期的所有五种报告类型都显示“imported”。
3. 如果任何单元格显示“missing”，则相应的报告尚未收到。

```
              bidsinauction   quality   pipeline-geo   pipeline-publisher   bid-filtering
2026-03-03    imported        imported  imported       imported             imported
2026-03-02    imported        imported  imported       imported             imported
```

一旦所有五列昨天都显示绿色，Cat-Scan 就拥有完整数据，每个功能（漏斗、浪费分析、推荐、优化器）都将工作。

## 自动检测

你不需要告诉 Cat-Scan 你正在上传哪个报告。导入系统会根据列标题自动检测报告类型：

- 有 **Bid filtering reason**？ -> Bid Filtering
- 有 **Bid requests** + **Publisher ID**？ -> Pipeline -- Publisher
- 有 **Bid requests**（无 Publisher ID）？ -> Pipeline -- Geo
- 有 **Creative ID** + **Billing ID**？ -> Quality
- 有 **Creative ID** + **Bids in auction**？ -> Bids in Auction

## Cat-Scan 如何使用每个指标

这将原始 CSV 指标映射到你在 Cat-Scan UI 中看到的内容。

| UI 功能 | 使用的指标 | 来源报告 |
|---------|------------|----------|
| **QPS 漏斗**（首页） | Bid requests, Reached queries, Bids, Bids in auction, Auctions won, Impressions, Clicks, Spend | Pipeline（两者）+ Quality |
| **浪费 % 计算** | `(Bid requests - Bids) / Bid requests` | Pipeline |
| **胜出率** | `Auctions won / Bids` | Pipeline + Bids in Auction |
| **CTR** | `Clicks / Impressions` | 同时包含两者的任何报告 |
| **CPM** | `(Spend / Impressions) * 1000` | Quality |
| **可见性率** | `Active View viewable / Active View measurable` | Quality |
| **视频完成率** | `Video completions / Video starts` | Quality |
| **地理浪费分析**（`/qps/geo`） | 按 Country 的 Bid requests、Impressions、Spend | Pipeline -- Geo + Quality |
| **发布商浪费**（`/qps/publisher`） | 按 Publisher 的 Bid requests、Impressions、Spend | Pipeline -- Publisher + Quality |
| **尺寸浪费**（`/qps/size`） | 按 Creative size 的 Impressions、Spend | Quality |
| **过滤原因**（`/qps/filtering`） | 按 Filtering reason 的 Bids、Bids in auction、Opportunity cost | Bid Filtering |
| **配置卡指标** | 按 Billing ID 的 Reached queries、Impressions、Spend | Quality |
| **素材性能** | 每个 Creative ID 的 Impressions、Clicks、Spend、Active View viewable | Quality |
| **优化器评分** | 所有管道 + 质量指标，按细分市场聚合 | 所有五份 |

## 常见错误

| 错误 | 会发生什么 | 修复 |
|------|------------|------|
| 向 Quality 报告添加“Bid requests” | Google 报错或返回不完整数据 | 移除“Bid requests”——它与“Billing ID”不兼容 |
| 忘记 Bid Filtering 报告 | Cat-Scan 无法向你展示 *为什么* 出价被拒绝 | 使用“Filtering reason”维度创建第 5 份报告 |
| 使用“Last 7 days”而不是“Yesterday” | 数据重叠、文件更大、导入更慢 | 设置为“Yesterday”并每日计划 |
| 不安排——仅手动导出 | 数据过时，健康检查失败 | 通过邮件安排每日交付 |
| Pipeline 报告上缺少“Hour”维度 | QPS 分析中没有小时粒度 | 向 Pipeline -- Geo 和 Pipeline -- Publisher 添加 Hour |
| Quality 报告上缺少可选指标 | Cat-Scan 中没有可见性或视频数据 | 添加 Active View viewable、Active View measurable、Video starts、Video completions |

## 下一步

- [管理导航](02-navigating-the-dashboard.md)：侧边栏布局和设置清单
- [数据导入](09-data-import.md)：详细的导入机制、分块上传和故障排除
- [QPS 漏斗](03-qps-funnel.md)：一旦数据流动，开始分析

**最后更新：** 2026 年 6 月  
RTB.cat / Cat-Scan 技术说明的一部分。