# IANA TLD List (Auto-Updated Fork)

🔄 **自动更新的 IANA TLD 数据库** - 基于 [jophy/iana_tld_list](https://github.com/jophy/iana_tld_list)

## 📊 项目状态

- ✅ **自动更新**: 每周三自动更新数据
- 🕐 **最后更新**: ![GitHub release (latest by date)](https://img.shields.io/github/v/release/yourusername/iana_tld_list)
- 📈 **TLD总数**: 1500+ (持续增长)
- 🤖 **维护方式**: GitHub Actions 自动化

## 🚀 主要改进

与原项目相比，此fork添加了以下功能：

1. **🔄 自动更新机制**
   - 每周三北京时间10:00自动运行
   - 支持手动触发更新
   - 自动创建Release和数据备份

2. **📊 更新报告**
   - 详细的TLD变更统计
   - 新增/移除TLD列表
   - 自动生成更新日志

3. **🛠️ 增强的脚本**
   - 支持命令行参数
   - 更好的错误处理
   - GitHub Actions优化

## 📥 使用方法

### 直接下载最新数据

```bash
# 下载最新的 TLD JSON 数据
curl -L https://github.com/yourusername/iana_tld_list/releases/latest/download/tld.json -o tld.json

# 或使用 wget
wget https://github.com/yourusername/iana_tld_list/releases/latest/download/tld.json
```

### 在代码中使用

```python
import requests
import json

# 获取最新TLD数据
response = requests.get('https://raw.githubusercontent.com/yourusername/iana_tld_list/master/data/tld.json')
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

### 本地运行更新

```bash
git clone https://github.com/yourusername/iana_tld_list.git
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

## 🔗 集成到项目

此数据库可轻松集成到各类项目中：

- **域名验证工具**
- **WHOIS查询服务**
- **网络安全分析**
- **域名管理系统**

## 📊 更新频率

- **自动更新**: 每周三
- **手动触发**: 支持随时手动运行
- **数据来源**: [IANA Root Zone Database](https://www.iana.org/domains/root/db/)

## 🤝 贡献

欢迎提交Issue和Pull Request！

如果发现数据问题或需要新功能，请：

1. 创建Issue描述问题
2. Fork项目并创建分支
3. 提交Pull Request

## 📄 许可证

MIT License - 与原项目保持一致

## 🙏 致谢

- **原作者**: [Jophy](https://github.com/jophy) - 创建了原始项目
- **Python 3 更新**: [mboot](https://github.com/maarten-boot) - Python 3兼容性
- **自动化维护**: 本fork添加了GitHub Actions自动更新

## 📈 统计信息

![GitHub issues](https://img.shields.io/github/issues/yourusername/iana_tld_list)
![GitHub forks](https://img.shields.io/github/forks/yourusername/iana_tld_list)
![GitHub stars](https://img.shields.io/github/stars/yourusername/iana_tld_list)
![GitHub license](https://img.shields.io/github/license/yourusername/iana_tld_list)

---

💡 **提示**: 将 `yourusername` 替换为你的GitHub用户名