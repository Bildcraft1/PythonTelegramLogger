# TelegramLogger
Telegram Logger written in Python using Telethon
# Installation
First clone the repo using git with this command:

```bash
git clone https://github.com/Bildcraft1/TelegramLogger.git
```

then install with pip telethon using this command:

```bash
pip3 install telethon pyfiglet
```

then you need to add those OS Variables:

```bash
export api_hash="<Insert API Hash from my.telegram.org>"
export api_id=<Your API ID>
export log_id=<Telegram Channel ID where you want to log messages>
```
# Running
The first time you run the script, it will ask for your Telegram Number to get a session (a file named `session_lock.session` will appear, if you delete it the program will reask for login), after logging in it will ask you the Chat ID of the group/channel you wanna log, then the bot will start logging messages on the console and on the Telegram Channel you set-up early on OSEnv