# TikTok Mass Unfollow Tool

## Overview

The TikTok Mass Unfollow Tool is designed to automate the process of unfollowing users on TikTok while adhering to TikTok's rate limits. This tool is intended for personal use and should be used responsibly in accordance with TikTok's terms of service.

## Features

- Unfollows up to 200 users per session.
- Unfollows 7 users at a time, then scrolls to load more.
- Logs unfollowed users in `unfollowed_log.txt`.
- Mimics human behavior with randomized delays.

## Installation

### Prerequisites

- Python 3.x
- Google Chrome browser

### macOS

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**:
   ```bash
   brew install python
   ```

3. **Install Google Chrome**:
   Download and install from [Google Chrome](https://www.google.com/chrome/).

4. **Install pip (Python package manager)**:
   ```bash
   python3 -m ensurepip --upgrade
   ```

5. **Install required Python packages**:
   ```bash
   pip3 install selenium webdriver-manager
   ```

### Windows

1. **Install Python**:
   Download and install from [Python.org](https://www.python.org/downloads/).

2. **Add Python to PATH**:
   During installation, ensure you check "Add Python to PATH".

3. **Install Google Chrome**:
   Download and install from [Google Chrome](https://www.google.com/chrome/).

4. **Install required Python packages**:
   Open Command Prompt and run:
   ```bash
   pip install selenium webdriver-manager
   ```

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/TikTok-Mass-Unfollow.git
   cd TikTok-Mass-Unfollow
   ```

2. **Run the script**:
   ```bash
   python TikTok_MassUnfollow.py
   ```

3. **Follow the on-screen instructions**:
   - Enter your TikTok username when prompted (without the '@').
   - The script will open a browser window and navigate to TikTok.
   - Log in to your TikTok account if not already logged in.
   - Manually click on the "Following" button to open the list of users you follow.
   - Press Enter in the terminal after opening the "Following" tab.

4. **The script will begin unfollowing users**:
   - It will unfollow users in batches of 7, scrolling as needed.
   - The process will stop after unfollowing 200 users or when no more users are available to unfollow.
   - Unfollowed users are logged in `unfollowed_log.txt`.

## Important Notes

- **Use responsibly**: Ensure you do not exceed TikTok's unfollow limits to avoid account restrictions.
- **Delays**: The script includes randomized delays to mimic human behavior and reduce the risk of detection.
- **Disclaimer**: Unauthorized use of automation may lead to account restrictions or bans. Use this tool at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes. # TikTok-Mass-Unfollow
