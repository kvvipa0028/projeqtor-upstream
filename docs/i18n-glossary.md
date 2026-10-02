# ProjeQtOr 中英术语表

界面只提供**中文**和 **English**。本表是 `tool/i18n/nls/zh/lang.js` 的统一译法。同一英文术语全站只用一种中文，不随页面改口。

译法按项目管理（项目、计划、工时、需求、工单、风险）和本系统里的对象含义确定，不按词典逐词硬套。英文原文有语法错误时，中文按原意翻译。

## 1. 对象

| English | 中文 | 使用场景 / 备注 |
|---|---|---|
| Project | 项目 | 项目对象 |
| Activity | 活动 | 计划中的工作包，不是“动态” |
| Activity stream | 动态 | 对象上的动态流 |
| Milestone | 里程碑 | |
| Ticket | 工单 | 事件/请求类工单，不用“票据” |
| Issue | 问题 | 问题对象。与 Question 区分 |
| Question | 疑问 | 本系统的疑问对象，不译成“问题” |
| Requirement | 需求 | |
| Risk | 风险 | |
| Opportunity | 机会 | 风险的正向对应项 |
| Action | 行动 | 待办行动项。旧译“措施”已统一改掉 |
| Decision | 决策 | 旧译“决议”已统一为决策 |
| Meeting | 会议 | 周期性会议为“例会” |
| Incoming | 收件 | 来文/收件对象 |
| Outgoing | 发件 | |
| Document | 文档 | |
| Note | 备注 | |
| Attachment | 附件 | |
| Link | 关联 | 对象之间的关联 |
| Dependency | 依赖关系 | 计划依赖。旧译“从属链接”已改 |
| Predecessor | 前置任务 | |
| Successor | 后置任务 | |
| Origin | 来源 | |
| Product | 产品 | |
| Component | 组件 | |
| Version | 版本 | 产品版本、组件版本、目标版本都用“版本” |
| Baseline | 基线 | |
| Deliverable | 交付物 | |
| Acceptance | 验收 | |
| Change request | 变更请求 | |
| Assumption | 假设 | |
| Constraint | 约束 | |
| Lesson learned | 经验教训 | |
| Context | 上下文 | 测试/产品运行上下文。旧译“语境”已改 |
| Test case | 测试用例 | 不用“测试样例” |
| Test session | 测试场次 | 一次测试执行批次。不用“测试序列” |
| User session | 会话 | 登录会话。与测试场次不是同一个词 |
| Budget | 预算 | |
| Expense | 费用 | |
| Client | 客户 | 不用“顾客” |
| Provider | 供应商 | 不用“供方” |
| Bill / Client invoice | 客户发票 | 本系统 Bill 是向客户开出的发票 |
| Invoice line | 发票行 | |
| Provider invoice | 供应商发票 | |
| Client order / Command | 客户订单 | Command 在本系统中是客户订单 |
| Provider order | 供应商订单 | |
| Quotation | 客户报价 | |
| Term (payment) | 付款节点 | 合同/发票上的付款期次，不是“条款”全文 |
| Contract | 合同 | |
| Tender | 投标 | Call for tender：招标 |
| Asset | 资产 | |
| Contact | 联系人 | |
| Organization | 组织 | |
| Team | 团队 | |
| Resource | 资源 | 可投入项目的人或设备 |
| Pool / resource pool | 资源池 | |
| Material resource | 物料资源 | |
| Employee | 员工 | |
| User | 用户 | 登录账号 |
| Stakeholder | 干系人 | |
| Prospect | 潜在客户 | CRM |
| Diary | 日程 | 按日查看工作的视图。存疑见文末 |
| Portfolio | 项目组合 | |
| Indicator | 指标 | |
| Alert | 警报 | |
| Notification | 通知 | 不用“消息”（消息留给 Message） |
| Message | 消息 | |
| Report | 报表 | 系统报表功能 |
| Filter | 筛选 | 不用“过滤器” |
| History | 历史 | |
| Today | 今日 | 今日视图 |
| Plugin | 插件 | |
| Abacus | 测算表 | 本系统用于估算的计算表，不是字面“算盘”。存疑见文末 |
| Work unit | 工作单元 | 复杂度目录中的工作单元 |
| Work command | 工时订单 | 以工作单元计价的订购 |
| Work token | 工时额度 | 购买的工时额度，不是加密代币 |
| Catalog | 目录 | |
| Checklist | 检查单 | |
| Tag | 标签 | |
| Voting attribution | 投票配额 | |

## 2. 计划与工时

| English | 中文 | 使用场景 / 备注 |
|---|---|---|
| Planning | 计划 | 计划编制与排程。旧译“规划”已统一为计划 |
| Gantt | 甘特图 | |
| WBS | WBS | 保留缩写，含义是工作分解结构 |
| BBS | BBS | 预算分解结构，保留缩写 |
| Critical path | 关键路径 | |
| Assignment | 分配 | 把资源分到活动上。旧译“委派”已改 |
| Allocation / Affectation | 投入 | 资源投入到项目。旧译“配置”已改，避免和系统配置混淆 |
| Work | 工时 | 本系统的 work 是工时数量，不是泛指“工作” |
| Real work | 实际工时 | |
| Planned work | 计划工时 | |
| Assigned work | 已分配工时 | |
| Left work | 剩余工时 | |
| Validated work | 已确认工时 | |
| Timesheet / Imputation | 工时表 / 工时填报 | 菜单 Imputation 译“工时表”。不用“归集” |
| Workload | 工作量 | |
| Capacity | 能力 | 资源可用能力 |
| Overuse / surbooking | 超额使用 | 超出可用能力的计划 |
| Planning mode | 计划模式 | |
| Duration | 工期 | |
| Due date | 到期日 | |
| Milestone date | 里程碑日期 | |
| Baseline | 基线 | |
| Replan | 重新计划 | |
| Lead project | 线索项目 | 销售线索阶段的项目，不是“主导项目” |
| Project dedicated to leaves | 休假专用项目 | 休假模块占用的项目 |

## 3. 状态、工作流、权限

| English | 中文 | 使用场景 / 备注 |
|---|---|---|
| Status | 状态 | |
| Workflow | 工作流 | |
| Idle / closed (flag) | 已关闭 | 系统里的 idle 标记表示关闭/停用，不是“空闲” |
| Show idle | 显示已关闭项 | |
| recorded | 已记录 | 初始状态 |
| qualified | 已定性 | 工单已完成初步定性 |
| in progress | 进行中 | |
| done | 已完成 | 旧译“完工”在状态上改为已完成 |
| verified | 已验证 | |
| delivered | 已交付 | |
| closed | 已关闭 | |
| cancelled | 已取消 | |
| assigned | 已分配 | |
| accepted | 已接受 | |
| validated | 已确认 | |
| prepared | 已准备 | |
| paused | 已暂停 | |
| copied | 已复制 | |
| re-opened | 已重新打开 | |
| to do | 待办 | 敏捷状态 |
| to test | 待测试 | |
| Priority | 优先级 | 低 / 中 / 高 / 关键优先级。取值不用「紧急」，「紧急」留给紧急程度 |
| Severity | 严重程度 | 不用“严重性”“严重度”混用 |
| Urgency | 紧急程度 | 阻塞 / 紧急 / 不紧急 |
| Criticality | 关键程度 | 低 / 中 / 高 / 严重 |
| Likelihood | 可能性 | 风险发生可能性 |
| Impact | 影响 | |
| Profile | 权限配置 | 一组访问权限。不是“属性”，也不是人员简历 |
| Access mode | 访问模式 | 项目相关的访问方式 |
| Reader | 只读 | 访问角色。旧译“审阅者”已改 |
| Creator | 创建者 | |
| Updater | 更新者 | |
| Manager (access profile) | 管理者 | 访问角色。项目经理仍译“项目经理” |
| No access | 无访问权限 | |
| Responsible | 负责人 | 对象上的负责人字段。旧译“责任人”已统一 |
| Requestor | 请求人 | |
| Issuer | 提出人 | |
| Approver | 审批人 | |
| Role / Function (of a resource) | 职能 | 人员职能及对应费率。不是软件“功能” |
| Right / habilitation | 权限 | |
| RACI | RACI | 缩写保留 |
| Responsible (RACI) | 执行 | RACI 的 R。对象字段 Responsible 仍是“负责人”，二者键不同 |
| Accountable (RACI) | 问责 | RACI 的 A。旧译“可入账的”是错的 |
| Consulted (RACI) | 协商 | RACI 的 C |
| Informed (RACI) | 知会 | RACI 的 I |
| Locked | 已锁定 | |
| Mandatory | 必填 | |
| Element | 要素 | 沿用本语言包已有说法，指一条业务数据 |

## 4. 敏捷与人力资源

| English | 中文 | 使用场景 / 备注 |
|---|---|---|
| Agile / Scrum | 敏捷 / Scrum | Scrum 保留原文 |
| Epic | 史诗 | |
| Sprint | 冲刺 | |
| User story | 用户故事 | |
| Backlog | 待办列表 | |
| Kanban | 看板 | |
| Planning poker | 估算扑克 | |
| Story point | 故事点 | |
| Vote | 投票 | |
| Leave | 休假 | |
| Absence | 缺勤 | |
| Employment contract | 劳动合同 | |
| Calendar | 日历 | |
| Off day | 休息日 | |
| Skill | 技能 | |
| Human resources / HR | 人力资源 / HR | HR 作为菜单短名可保留 |

## 5. 界面动作

| English | 中文 | 使用场景 / 备注 |
|---|---|---|
| Login | 登录 | |
| Password | 密码 | |
| Save | 保存 | |
| Cancel | 取消 | |
| Delete | 删除 | |
| Close | 关闭 | |
| Copy | 复制 | |
| Add | 添加 | |
| Edit | 编辑 | |
| Search | 搜索 | |
| Refresh | 刷新 | |
| Print | 打印 | |
| Export | 导出 | |
| Import | 导入 | |
| Yes / No | 是 / 否 | |
| OK | 确定 | 按钮 |
| Warning | 警告 | |
| Error | 错误 | |
| Parameter | 参数 | |
| Global parameters | 全局参数 | |
| Language | 语言 | 切换器标签为“中文”和 “English”，不随界面语言改写 |
| Default language | 默认语言 | 新产品默认中文 |

## 6. 保留原文

下列词保持原文，不翻译：

| 原文 | 原因 |
|---|---|
| ProjeQtOr | 产品名 |
| WBS、BBS、RACI、KPI、SLA、HR、CRM | 业界通用缩写 |
| Scrum | 敏捷方法名 |
| LDAP、SSO、SAML、IMAP、SMTP、SSL、PDF、CSV、Excel、xlsx、SQL、HTML、JSON、XML、URL、API、cron、UTF-8 | 技术标识 |
| Dojo | 界面库名称，仅在说明技术来源时出现 |

数据库里由用户维护的名称（自建的类型、自建的状态名）不在语言包里，界面只翻译安装时带入的默认名称。

## 7. 占位与格式

- `${1}`、`${name}` 等占位符原样保留。
- `<br/>`、`<b>` 等标签原样保留。
- `&#58;`（冒号）、`&#44;`（逗号）、`&#34;`（引号）、`&#10;`（换行）原样保留。语言包解析按英文逗号和冒号切分，译文里不能新出现裸的 `,` 或 `:`。
- 作为类名、参数名、字段名出现的标识（如 `idResource`、`refType`）不翻译。

## 8. 存疑译法（请复核）

| English | 当前译法 | 犹豫点 |
|---|---|---|
| Diary | 日程 | 也可能理解成个人“日记”。本系统是按日汇总会议和工时，故用日程 |
| Abacus | 测算表 | 官方英文就叫 Abacus。若希望保留“算盘表”或“估算表”，可以改 |
| Action | 行动 | 质量领域常称“措施”。这里是通用行动项，故用行动 |
| Decision | 决策 | 会议结论也常称“决议” |
| Lead project | 线索项目 | 对应销售线索（lead），不是“牵头项目” |
| qualified | 已定性 | 工单流程中的分诊/定性，不是“合格” |
| Term | 付款节点 | 也可能译“账期” |
| Work token | 工时额度 | 功能较偏，若业务上是代币结算，可改回“工时代币” |
| Element | 要素 | 也可译“条目”。为与原有中文包一致而保留 |
| Sprint | 冲刺 | 有的团队固定说“迭代” |
| Accountable | 问责 | RACI 的 A。有的团队写成“最终负责” |
| Provider | 供应商 | 采购语境里“供方”也对，已统一为供应商 |
| Bill | 客户发票 | 口语里也说“账单”。与 Invoice 对齐为发票 |
| Hight priority | 高优先级 | 仅未升级的旧库仍可能保留这个拼写，键为 priorityHightPriority。V2.4.0 起库内名称是 High priority |
| High priority | 高优先级 | 升级后的优先级名称，键为 priorityHighPriority |
| Critical priority | 关键优先级 | V1.3.0 起库内名称。不用“紧急”，以免和紧急程度 urgencyUrgent 重名 |
| Critical priority (immediate action required) | 关键优先级（需立即处理） | 旧名称，键 priorityCriticalPriorityImmediateActionRequired 仍保留 |
| Function (resource) | 职能 | 调试日志里的 function tracing 仍是“函数跟踪”，不是职能 |
