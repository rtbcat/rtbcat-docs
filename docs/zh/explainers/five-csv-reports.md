---
title: "Google Authorized Buyers 的五份 CSV 报告（2026）"
description: "Google Authorized Buyers 在 2026 年仍需要五份独立的 CSV 报告；字段不兼容阻止单一导出。Cat-Scan 将它们合并为三个核心表。"
---

# Google Authorized Buyers 在 2026 年仍需要五份独立的 CSV 报告

**原子事实：** Google Authorized Buyers 不允许你在单个导出中同时获取竞价请求和创意级别的详细信息。

这不是文档缺失，而是多年来一直存在且在 2026 年依然有效的有意 schema 约束。

## 为什么必须使用五份报告

Google Authorized Buyers 存在字段不兼容性，阻止将优化所需的所有内容合并到一个文件中：

- 创意级性能指标会移除“竞价请求”列。
- 竞价请求/管道字段会移除创意 ID 和部分性能细节。
- 发布商数据有时可以与竞价请求一起出现，但不能与创意级行一起。
- 质量信号（可见性、欺诈）以自己的形状到达。
- 出价过滤/拒绝原因存在于第五份报告中。

因此 Cat-Scan 会摄取五份不同的每日 CSV 导出，并将它们合并为可用的模型。

**原子事实：** Cat-Scan 精确导入这五种报告类型，并将它们映射到三个核心表：`rtb_daily`、`rtb_bidstream` 和 `rtb_bid_filtering`。

## 五份报告（确切命名和用途）

所有报告都遵循命名约定 `catscan-{type}-{account_id}-{period}-UTC`。

| # | 报告类型              | 目标表         | 主要用途                              | 关键限制 |
|---|-----------------------|----------------|---------------------------------------|----------|
| 1 | bidsinauction        | rtb_daily     | 创意级出价、胜出、展示、花费         | 无原始竞价请求 |
| 2 | quality              | rtb_daily     | 带可见性的创意级性能                 | 无竞价请求量 |
| 3 | pipeline-geo         | rtb_bidstream | 按国家+小时划分的完整竞价流漏斗     | 无创意 ID |
| 4 | pipeline             | rtb_bidstream | 按发布商划分的完整竞价流漏斗        | 无创意 ID |
| 5 | bid-filtering        | rtb_bid_filtering | Google 拒绝出价的原因          | 与性能数据分离 |

**原子事实（2026 年 6 月）：** 2026-01-14 之前导入的数据被标记为 `data_quality='legacy'`，因为早期报告使用了不一致的时区。当前所有报告必须使用 UTC。

## 实际中的合并如何工作

导入器（参见 Cat-Scan 平台仓库）使用日期 + 买方账户 + 创意 ID（如果存在）以及发布商或地理维度组合，来重建完整画面。

你不能简单地联合这些文件。你必须在导入时去重（Cat-Scan 使用 `row_hash` 唯一约束），然后跨五份来源进行聚合。

这就是为什么需要专门构建的控制平面。下载五份 CSV 并在电子表格中打开，无法为你提供按配置的 QPS 漏斗、按尺寸的浪费，或安全的预定向建议。

## 为什么这对机构很重要

大多数最终获得 Google Authorized Buyers 席位的机构，只在花费第一个月后才发现报告问题。原生 UI 和邮件 CSV 是有意受限的。

五份报告的现实是，你正在与真正的席位运营商打交道，而不是只读过 Authorized Buyers 文档的人的最强信号之一。

## 相关阅读和代码

- Cat-Scan 平台仓库中的完整列映射和示例行
- 平台中的导入器逻辑
- Cat-Scan 如何从这些报告重建漏斗：[理解你的 QPS 漏斗](../03-qps-funnel.md)
- 手册中的数据导入章节：[数据导入](../09-data-import.md)

**最后更新：** 2026 年 6 月  
RTB.cat / Cat-Scan 技术说明的一部分。  
来源：真实 Authorized Buyers 席位的生产运营 + 开源 Cat-Scan 平台。