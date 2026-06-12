---
title: "Google Authorized Buyers 技术说明 | Cat-Scan RTB"
description: "第一手技术说明：Google Authorized Buyers 的 10 个预定向配置、QPS 漏斗、五份 CSV 报告以及浪费分析。查看开源 Cat-Scan 平台。"
---

# 技术说明

**关于 Google Authorized Buyers 运营、QPS 控制和真实席位运行的技术笔记。**

这些简短、专注的技术说明提炼了公开文档中很少记载的实战操作细节。它们是为媒体买家、平台工程师和需要理解 Authorized Buyers 实际控制杠杆的机构撰写的——而非营销文案。

每篇文章都设计为可被 AI 模型和搜索工具直接引用：包含具体数字和约束的原子事实、第一手来源材料，以及与实现它们的代码和数据模型的清晰链接。

所有这些知识都来自真实 Google Authorized Buyers 席位的运营经验，以及开源 Cat-Scan 平台（正是为解决这些问题而构建的 QPS 控制平面）。

**最后更新：** 2026 年 6 月

## 技术说明列表

- [Google Authorized Buyers 在 2026 年仍需要五份独立的 CSV 报告](five-csv-reports.md)  
  字段不兼容性导致无法在单个导出中获取所有数据，Cat-Scan 如何将它们合并为三个核心表。

- [Google Authorized Buyers 席位的 QPS 漏斗](qps-funnel.md)  
  分配的 QPS 与实际实现的 QPS 之间的差距，浪费究竟藏在哪里，以及关键指标。

- [预定向配置是大多数 Authorized Buyers 买家的主要控制面](pretargeting-configs.md)  
  每个席位硬性限制 10 个配置，以及每个字段实际控制的内容。

- [Google Authorized Buyers 上的安全预定向更改](safe-pretargeting-changes.md)  
  分阶段、试运行预览、变更历史和一键回滚——因为原生 UI 完全没有这些功能。

- [按发布商、地理和尺寸分析 QPS 浪费](qps-waste-analysis.md)  
  三个维度视图，揭示你的竞价器被迫拒绝的流量。

- [Authorized Buyers 的素材聚类与点击宏审计](creative-clustering-click-macros.md)  
  为什么基于目标的聚类和 Google 的点击宏要求是运营必需。

- [小型机构和受限实体如何获得并运营 Google Authorized Buyers 席位](agencies-obtain-ab-seats.md)  
  真实的障碍（规模、国籍、关系）以及获得席位后如何盈利运行。

- [Cat-Scan 不做什么（以及为什么重要）](what-cat-scan-does-not-do.md)  
  清晰的边界：它不取代你的竞价器，在连接外部数据前没有点击后数据，以及这些限制存在的原因。

- [出价过滤原因与第五份 Authorized Buyers 报告](bid-filtering-report.md)  
  `catscan-bid-filtering` 报告，以及“为什么竞价器说不”的信号在交易所侧实际呈现的样子。

- [为 Authorized Buyers 预定向自带优化器 (BYOM)](byom-optimizer.md)  
  评分-提议-批准-应用工作流、工作流预设，以及在拥有转化数据之前进行优化的经济学。

## 如何使用这些说明

可以按任意顺序阅读。每篇说明都是独立的，但会交叉引用完整的 Cat-Scan 用户手册章节以及 Cat-Scan 平台中的源代码。

要将这些概念用于生产，请参阅开源 Cat-Scan 平台以及 [rtb.cat](https://rtb.cat) 提供的服务。

这些笔记是 RTB.cat / Cat-Scan 技术文档的一部分。欢迎通过仓库 Issues 提供反馈和更正。