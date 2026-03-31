# 百度网盘签到配置文件
# 复制此文件为 config.py 并填写你的真实信息

# ============= 必填配置 =============

# Cookie 信息（从浏览器开发者工具获取）
# 获取方法：
# 1. 打开 https://pan.baidu.com/ 并登录
# 2. 按 F12 打开开发者工具
# 3. 刷新页面，找到任意请求
# 4. 复制 Request Headers 中的 Cookie 字段
BAIDU_COOKIE = ""

# ============= 可选配置 =============

# 隐私保护模式（true/false）
# true: 隐藏用户信息，false: 显示完整用户信息
PRIVACY_MODE = "true"

# 通知方式（后续可扩展）
# - feishu: 飞书 webhook
# - telegram: Telegram Bot
# - wechat: 企业微信
NOTIFY_METHOD = "feishu"

# Webhook URL（如使用飞书/钉钉通知）
WEBHOOK_URL = ""

# Telegram 配置（如使用 Telegram 通知）
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""
