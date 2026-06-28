<img width="1190" height="570" alt="Screenshot_2026-06-28_18-05-51" src="https://github.com/user-attachments/assets/8fa99f8e-682b-4f62-85d7-9b5dd75289c6" />


[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-5865F2?logo=discord&logoColor=white)](https://discordpy.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)]()
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)]()

**A lightweight, powerful Discord server management framework with only 3 basic commands.**

---

## Quick Start

> **⚠️ WARNING: This bot contains DESTRUCTIVE commands. Only run this on servers you own or have explicit permission to test on.**

### Prerequisites

- Python 3.8 or higher
- A Discord Bot Token ([Get one here](https://discord.com/developers/applications))

### Installation (2-Step Setup)

**Step 1:** Clone and install dependencies
```bash
git clone https://github.com/yourusername/entropy.git
cd entropy
pip3 install discord.py
python3 entropy.py
```

**Step 2:** Configure your token

```python
# Create a config.py file in the root directory
TOKEN = 'your-bot-token-here'
```

📋 Available Commands
Command	Permission Required	Description
!nuke	Administrator	Deletes ALL channels in the server
!mass_ban	Administrator	Bans ALL non-bot members
!spam <message>	Administrator	Sends your message 100 times

Check before running:
My bot token is in config.py (not hardcoded)

Troubleshooting
Issue	Solution
ModuleNotFoundError	Run pip install discord.py
Invalid token	Verify your token in config.py
403 Forbidden	Ensure bot has Administrator permissions
Commands not working	Bot needs application.commands scope

License
MIT License - Use at your own risk. The authors are not responsible for any server damage caused by this tool.
