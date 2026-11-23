# 🌱 Life

> Turn personal and professional growth into a game, privately and entirely on your own device.

<img src="https://skillicons.dev/icons?i=python,flask,html,css,sql,git&theme=dark" alt="Technology Stack"/>

---

## About

Life goes beyond a simple personal organizer. It is an open-source project that gamifies self-improvement, making personal and professional growth more engaging, dynamic, and rewarding.

It is built around **privacy, transparency, and user autonomy**:

- **100% local:** no external servers and no internet connection required.
- **Encrypted data:** journals, schedules, and personal information are protected with strong encryption.
- **Yours alone:** your data stays under your exclusive control.

## Features

- 🎮 Gamified progress and rewards for your goals
- 📓 Private, encrypted journal
- 📅 Schedules and personal organization
- 🔒 Fully offline operation

> ✏️ *Adjust this list to match what is actually implemented.*

## Requirements

- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/downloads/)

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/nullzinx/life && cd life
```

**2. Install the dependencies**

```bash
pip install -r requirements.txt
```

**3. Create the configuration file** 

```.env
SECRET_KEY="ABC2" # Enter a strong password here 
DATABASE_URI ="sqlite:///database.db" # the sqlalchemy uri If you do not wish to use SQLite, please select a database management system of your choice 
```

**3. Run the application**

```bash
python run.py
```

Then open the address shown in the terminal (usually `http://127.0.0.1:5000`) in your browser.

### 📱 Termux (Android)

On Termux, install the cryptography package through `pkg` **first**, then the remaining dependencies:

```bash
pkg install python-cryptography
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Open an issue to discuss an idea or bug, or send a pull request.

