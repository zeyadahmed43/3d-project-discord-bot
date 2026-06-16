Here is a clean, professional `README.md` tailored specifically for your Discord bot repository. It highlights the tech stack (Python, Groq API), explains the existing commands clearly based on your code, and gives step-by-step instructions for setup.

---

# 3D Project Concept Generator Discord Bot

A Python-based Discord bot designed to assist 3D artists, designers, and developers by generating creative prompts and concepts. Leveraging the high-speed **Groq API**, the bot quickly delivers stylized art ideas, city layouts, and architectural building concepts directly into your Discord server.

## 🚀 Features & Commands

The bot utilizes Discord slash commands to provide instant, structured design inspiration:

* `/isometric` – Generates a creative concept for a **3D isometric art piece**, complete with a title and a brief descriptive breakdown.
* `/city_block` – Generates an detailed prompt for a **3D city block layout**, detailing buildings, streets, and urban aesthetics.
* `/building` – Generates an **architectural building concept** exploring various design styles and structural themes.

---

## 🛠️ Prerequisites

Before getting started, make sure you have the following ready:

1. **Python 3.8+** installed on your system.
2. A **Discord Bot Token** (obtained from the [Discord Developer Portal](https://discord.com/developers/applications)).
3. A **Groq API Key** (obtained from the [Groq Console](https://console.groq.com/)).

---

## ⚙️ Installation & Setup

Follow these steps to clone the repository, set up your environment variables, and run the bot locally:

### 1. Clone the Repository

```bash
git clone https://github.com/zeyadahmed43/3d-project-discord-bot.git
cd 3d-project-discord-bot

```

### 2. Install Dependencies

Install the required Python packages (such as `discord.py` and the `groq` SDK):

```bash
pip install -r requirements.txt

```

*(If you don't have a requirements file yet, run `pip install discord.py groq python-dotenv`)*

### 3. Configure API Keys (Environment Variables)

To keep your sensitive API keys secure, the bot reads them from an environment file.

1. Create a file named `.env` in the root directory of the project.
2. Open the `.env` file and add your actual tokens exactly like this:

```env
DISCORD_TOKEN=your_discord_bot_token_here
GROQ_API_KEY=gsk_your_groq_api_key_here

```

> ⚠️ **Important:** Never commit your `.env` file or push your raw tokens to GitHub. The project's `.gitignore` file should always keep this file local.

### 4. Run the Bot

Once your configuration is saved, kick off the Python script:

```bash
python bot.py

```

---
