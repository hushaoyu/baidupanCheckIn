# 百度网盘签到

一个用于百度网盘自动签到的脚本，支持在 GitHub Actions 中运行。

## 功能特性

- ✅ 自动签到获取积分
- ✅ 自动回答每日问题获取积分
- ✅ 支持多账号签到
- ✅ 支持隐私保护模式
- ✅ 支持随机延迟签到（在 GitHub Actions 中处理）
- ✅ 支持多种通知方式（飞书、Telegram、企业微信）

## 快速开始

### 1. Fork 本仓库

点击仓库右上角的 "Fork" 按钮，将本仓库复制到你的 GitHub 账号。

### 2. 配置 GitHub Secrets

在你的 Fork 仓库中，进入 "Settings" → "Secrets and variables" → "Actions"，添加以下 Secrets：

| Secret 名称 | 描述 | 是否必填 |
|------------|------|---------|
| `BAIDU_COOKIE` | 百度网盘的 Cookie 值 | ✅ |
| `NOTIFY_METHOD` | 通知方式（feishu/telegram/wechat） | ❌ |
| `WEBHOOK_URL` | 飞书或企业微信的 Webhook URL | ❌ |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Token | ❌ |
| `TELEGRAM_CHAT_ID` | Telegram Chat ID | ❌ |

### 3. 获取百度网盘 Cookie

1. 打开百度网盘网页版：https://pan.baidu.com/
2. 登录你的账号
3. 按 F12 打开开发者工具
4. 切换到 Network 标签页，刷新页面
5. 找到任意请求的 Request Headers
6. 复制完整的 Cookie 值

### 4. 启用 GitHub Actions

在你的 Fork 仓库中，进入 "Actions" 标签页，点击 "I understand my workflows, go ahead and enable them" 按钮启用工作流。

### 5. 手动触发签到

在 "Actions" 标签页中，点击 "Baidu Netdisk Checkin" 工作流，然后点击 "Run workflow" 按钮手动触发一次签到，测试配置是否正确。

## 配置说明

### 环境变量

| 环境变量 | 描述 | 默认值 |
|---------|------|-------|
| `BAIDU_COOKIE` | 百度网盘的 Cookie 值（多个账号用换行分隔） | 空 |
| `PRIVACY_MODE` | 是否启用隐私保护模式 | true |
| `NOTIFY_METHOD` | 通知方式（feishu/telegram/wechat） | feishu |
| `WEBHOOK_URL` | 飞书或企业微信的 Webhook URL | 空 |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Token | 空 |
| `TELEGRAM_CHAT_ID` | Telegram Chat ID | 空 |

### 签到时间

默认每天 UTC 时间 0:30（北京时间 8:30）执行签到。如果需要修改签到时间，请编辑 `.github/workflows/checkin.yml` 文件中的 cron 表达式。

## 注意事项

1. Cookie 值会定期失效，需要定期更新
2. 不要在公共仓库中暴露你的 Cookie 值
3. 建议启用隐私保护模式，避免在通知中显示完整的用户名
4. 随机延迟签到在 GitHub Actions workflow 中处理，可以降低被检测的风险

## 故障排除

### 签到失败

1. 检查 Cookie 值是否正确
2. 检查网络连接是否正常
3. 查看 GitHub Actions 的运行日志，了解具体错误信息

### 通知失败

1. 检查通知配置是否正确
2. 检查网络连接是否正常
3. 查看 GitHub Actions 的运行日志，了解具体错误信息

## 许可证

本项目采用 MIT 许可证。
