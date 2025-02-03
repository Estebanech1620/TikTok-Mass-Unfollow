# TikTok Mass Unfollow Tool

## Developed by DestinyX Studios
### Written by Estebanech

## Overview
This tool automates the process of unfollowing users on TikTok. It is designed to unfollow exactly 200 users per session and logs the unfollowed accounts.

## Features
- Unfollows **exactly** 200 users per session.
- Unfollows **7 users at a time**, then scrolls down to load more.
- Saves a log of unfollowed users (usernames or profile URLs) in `unfollowed_log.txt`.

## TikTok Unfollowing Regulations
- **Do not unfollow more than 200-300 users per day** to avoid account restrictions.
- **Unfollow in intervals** of 50-100 users every few hours to stay safe.
- **Keep delays of 2-5 seconds** between actions to mimic human behavior.

## Disclaimer
Use this script responsibly and in accordance with TikTok's terms of service. Unauthorized use of automation may lead to account restrictions or bans.

## Setup Instructions

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: Ensure Git is installed to clone the repository. You can download it from [git-scm.com](https://git-scm.com/).

### Step 1: Clone the Repository
Open your terminal (Command Prompt on Windows, Terminal on macOS) and run:

```bash
git clone https://github.com/Estebanech1620/TikTok-Mass-Unfollow.git
cd TikTok-Mass-Unfollow
```

### Step 2: Set Up a Virtual Environment

#### On Windows
1. Open Command Prompt and navigate to the project directory.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

#### On macOS
1. Open Terminal and navigate to the project directory.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Step 3: Install Required Packages
With the virtual environment activated, install the necessary packages:

```bash
pip install selenium webdriver-manager
```

### Step 4: Run the Script
1. **Start the Script**: Run the script using:
   ```bash
   python TikTok_MassUnfollow.py
   ```

2. **Log In**: The script will open TikTok's login page. Log in manually to your TikTok account.

3. **Navigate to Profile**: After logging in, the script will navigate to your profile page.

4. **Open Following List**: Manually click on the "Following" button to open the list of users you are following.

5. **Continue the Script**: Once the "Following" list is open, return to the terminal and press Enter to start the unfollowing process.

### Step 5: Deactivate the Virtual Environment (Optional)
After you are done using the script, you can deactivate the virtual environment by running:

```bash
deactivate
```

## Logging
The script logs each unfollowed user in `unfollowed_log.txt`. This file is created on the user's desktop.

## Troubleshooting
- Ensure that the virtual environment is activated before running the script.
- If you encounter any issues with Selenium or WebDriver, ensure that all packages are up to date.
- Adjust the XPath selectors in the script if TikTok changes its HTML structure.

## Contribution
Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
