# IANA TLD 列表 (自动更新分支)

🌍 **语言**: [English](README.md) | [中文](README_CN.md)

🔄 **自动更新的 IANA TLD 数据库** - 基于 [jophy/iana_tld_list](https://github.com/jophy/iana_tld_list)

一个用于下载和解析 IANA 顶级域名数据库的综合工具，具有 **GitHub Actions 自动更新**功能。

## 📊 项目状态

- ✅ **自动更新**: 每周三自动更新 TLD 数据
- 🤖 **GitHub Actions**: 自动化执行和数据发布
- 📈 **TLD总数**: 1500+ (持续增长)
- 🕐 **最后更新**: 通过 GitHub Releases 追踪

## 🚀 主要改进

与原项目相比，此分支添加了以下功能：

### 🔄 自动更新机制
- 每周三自动执行
- 支持手动触发更新
- 自动创建 Release 和数据备份

### 📊 更新报告
- 详细的 TLD 变更统计
- 新增/移除 TLD 列表
- 自动生成更新日志

### 🛠️ 增强的脚本
- 支持命令行参数
- 更好的错误处理
- GitHub Actions 优化

## 📥 快速开始

### 下载最新数据

```bash
# 下载最新的 TLD JSON 数据
curl -L https://github.com/SzeMeng76/iana_tld_list/releases/latest/download/tld.json -o tld.json

# 或使用 wget
wget https://github.com/SzeMeng76/iana_tld_list/releases/latest/download/tld.json
```

### 在代码中使用

```python
import requests
import json

# 获取最新TLD数据
response = requests.get('https://raw.githubusercontent.com/SzeMeng76/iana_tld_list/master/data/tld.json')
tld_data = response.json()

# 查询特定TLD
def get_tld_info(tld):
    tld_clean = tld.lower().lstrip('.')
    for item in tld_data:
        if item.get('tld') == tld_clean:
            return item
    return None

# 示例使用
com_info = get_tld_info('com')
print(f"TLD: {com_info['tld']}")
print(f"类型: {com_info['tldType']}")
print(f"管理机构: {com_info['nic']}")
```

### 本地开发

```bash
git clone https://github.com/SzeMeng76/iana_tld_list.git
cd iana_tld_list

# 安装依赖
pip install requests beautifulsoup4 lxml

# 运行更新
python update_tld.py --non-interactive --overwrite --verbose
```

## 📋 数据格式

TLD数据以JSON格式存储，每个TLD包含以下字段：

```json
{
  "tld": "com",
  "dm": ".com",
  "isIDN": false,
  "tldType": "gTLD",
  "nic": "http://www.verisigninc.com",
  "whois": "whois.verisign-grs.com",
  "lastUpdate": "2024-01-15",
  "registration": "1985-01-01"
}
```

### 字段说明

- `tld`: TLD名称（不带点）
- `dm`: 完整域名（带点）
- `isIDN`: 是否为国际化域名
- `tldType`: TLD类型（gTLD/ccTLD/iTLD）
- `nic`: 管理机构网站
- `whois`: WHOIS服务器
- `lastUpdate`: 最后更新日期
- `registration`: 注册日期

## 💡 使用场景

- **域名验证工具**
- **WHOIS查询服务**
- **网络安全分析**
- **域名管理系统**
- **TLD研究和监控**

## 📊 更新计划

- **自动更新**: 每周三
- **手动触发**: 随时支持
- **数据来源**: [IANA根区数据库](https://www.iana.org/domains/root/db/)

## 🤝 贡献

欢迎提交Issue和Pull Request！

如果发现数据问题或需要新功能：

1. 创建Issue描述问题
2. Fork项目并创建分支
3. 提交Pull Request

## 🤝 贡献者

- **原作者**: [Jophy](https://github.com/jophy) - 初始实现
- **Python 3移植**: [mboot](https://github.com/maarten-boot) - Python 3兼容性和增强功能
- **自动化**: [SzeMeng76](https://github.com/SzeMeng76) - GitHub Actions自动更新

## 📄 许可证

MIT许可证 - 与原项目保持一致

---

⏱️ **性能说明**: 完整的TLD处理大约需要20分钟（在DigitalOcean VPS上测试）