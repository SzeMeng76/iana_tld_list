# IANA TLD List (Auto-Updated Fork)

🌍 **Language**: [English](README.md) | [中文](README_CN.md)

🔄 **Automated IANA TLD Database** - Fork of [jophy/iana_tld_list](https://github.com/jophy/iana_tld_list)

A comprehensive tool for downloading and parsing IANA Top-Level Domain database with **automated GitHub Actions updates**.

## 📊 Project Status

- ✅ **Auto-Updated**: Weekly automated TLD data updates
- 🤖 **GitHub Actions**: Automated execution and data publishing
- 📈 **TLD Count**: 1500+ (continuously growing)
- 🕐 **Last Update**: Check commit history or tld.json file

## 🚀 Key Improvements

This fork adds the following features compared to the original project:

### 🔄 Automated Update Mechanism
- Weekly automated execution (every Wednesday)
- Manual trigger support
- Automatic data updates to tld.json

### 📊 Update Reports
- Detailed TLD change statistics
- Added/removed TLD lists
- Automatic changelog generation

### 🛠️ Enhanced Scripts
- Command-line argument support
- Better error handling
- GitHub Actions optimization

## 📥 Quick Start

### Download Latest Data

```bash
# Download latest TLD JSON data
curl -L https://raw.githubusercontent.com/SzeMeng76/iana_tld_list/master/data/tld.json -o tld.json

# Or using wget
wget https://raw.githubusercontent.com/SzeMeng76/iana_tld_list/master/data/tld.json
```

### Use in Code

```python
import requests
import json

# Get latest TLD data
response = requests.get('https://raw.githubusercontent.com/SzeMeng76/iana_tld_list/master/data/tld.json')
tld_data = response.json()

# Query specific TLD
def get_tld_info(tld):
    tld_clean = tld.lower().lstrip('.')
    for item in tld_data:
        if item.get('tld') == tld_clean:
            return item
    return None

# Example usage
com_info = get_tld_info('com')
print(f"TLD: {com_info['tld']}")
print(f"Type: {com_info['tldType']}")
print(f"Registry: {com_info['nic']}")
```

### Local Development

```bash
git clone https://github.com/SzeMeng76/iana_tld_list.git
cd iana_tld_list

# Install dependencies
pip install requests beautifulsoup4 lxml

# Run update
python update_tld.py --non-interactive --overwrite --verbose
```


## 📋 Data Format

TLD data is stored in JSON format, each TLD contains the following fields:

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

### Field Descriptions

- `tld`: TLD name (without dot)
- `dm`: Full domain name (with dot)
- `isIDN`: Whether it's an Internationalized Domain Name
- `tldType`: TLD type (gTLD/ccTLD/iTLD)
- `nic`: Registry website
- `whois`: WHOIS server
- `lastUpdate`: Last update date
- `registration`: Registration date

## 📊 Update Schedule

- **Automatic Updates**: Every Wednesday
- **Manual Trigger**: Supported anytime
- **Data Source**: [IANA Root Zone Database](https://www.iana.org/domains/root/db/)

## 🤝 Contributing

Welcome to submit Issues and Pull Requests!

If you find data issues or need new features:

1. Create an Issue describing the problem
2. Fork the project and create a branch
3. Submit a Pull Request

## 💡 Use Cases

- **Domain validation tools**
- **WHOIS query services**
- **Network security analysis**
- **Domain management systems**
- **TLD research and monitoring**

## 🤝 Contributors

- **Original Author**: [Jophy](https://github.com/jophy) - Initial implementation
- **Python 3 Port**: [mboot](https://github.com/maarten-boot) - Python 3 compatibility and enhancements
- **Automation**: [SzeMeng76](https://github.com/SzeMeng76) - GitHub Actions automated updates

## 📄 License

MIT License - Consistent with the original project

---

⏱️ **Performance Note**: Complete TLD processing takes approximately 20 minutes (tested on DigitalOcean VPS)
