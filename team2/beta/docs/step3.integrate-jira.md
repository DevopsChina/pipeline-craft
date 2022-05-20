?> Jira 是非常流行的需求管理工具，可以轻松和场景的聊天软件集成，对 Gitlab 的集成也很友好。

## 集成步骤

和 Slack 的基础我们在前文已经提供文档，这里不再赘述。

和 Gitlab 的集成需要依赖于 Jira 的插件市场。

1. 在插件市场中搜索 Gitlab 后安装
2. 在 Gitlab 插件中设置 Jira 的配置，在此之前需要先登录 Jira 并生成一个 token

截图示例如下：

如果和 Slack 集成成功后，那么在 Slack 中我们可以创建和订阅需求。
如果和 Gitlab 集成成功过后，我们可以 Jira 中收到 Gitlab 的提交消息和 CICD 结果。

## 参考文档

1. https://docs.gitlab.com/ee/integration/jira/
2. https://marketplace.atlassian.com/apps/1223003/gitlab-integration-for-jira-gitlab-jira-sync