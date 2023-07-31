# My first Discord Bot

It just responds to messages and lists members. It is just my first test.

![discord bot in a guild channel](media/image.png)

## Discord Bot Setup

Create a new app and a bot in Discord Developer Portal, set up permissions and intents. Get a token.

Create a `.env` file and paste your token there:

```
DISCORD_TOKEN=<YOUR-TOKEN>
```

## Installation and requirements

Python 3.9 and higher is requireed, get the code, create a virtual environment and install the pip packages

```bash
python -m venv tdb001-venv
pip install -r requirements.txt
```

(If required, you might need to install venv: `sudo apt install python3-venv -y`).

In Visual Studio Code the virtual environment will be loaded automatically, so just press F5.

If in terminal, activate the virtual environment

```powershell
.\tdb001-venv\Scripts\activate.ps1
```

```bash
source tdb001-venv\bin\activate
```

To start the bot from terminal run:

```bash
python bot.py
```

If you want to start it from SSH and log out, run the following:

```bash
nohup python bot.py &
```
