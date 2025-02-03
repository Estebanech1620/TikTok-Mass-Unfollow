"""
TikTok Mass Unfollow Tool - Public Version
Developed by: DestinyX Studios
Written by: Estebanech
Date: February 2, 2025
Purpose: Automates the process of unfollowing users on TikTok while following rate limits.

Usage:
- The script asks for the user's TikTok username.
- The script navigates to the user's TikTok profile.
- The user manually clicks the "Following" button to open the list.
- The script ensures 200 users are unfollowed before stopping.

Features:
1. User inputs their TikTok username at runtime.
2. Unfollows **7 users at a time**, then scrolls down to load more.
3. Saves a log of unfollowed users (usernames or profile URLs) in `unfollowed_log.txt`.

TikTok Unfollowing Regulations:
- **Do not unfollow more than 200-300 users per day** to avoid account restrictions.
- **Unfollow in intervals** of 50-100 users every few hours to stay safe.
- **Keep delays of 2-5 seconds** between actions to mimic human behavior.

Disclaimer:
Use this script responsibly and in accordance with TikTok's terms of service.
Unauthorized use of automation may lead to account restrictions or bans.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-data-dir=./tiktok_profile")  # Saves session

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ask the user for their TikTok username
TIKTOK_USERNAME = input("Enter your TikTok username (without @): ").strip()

LOG_FILE = "unfollowed_log.txt"  # Log file to save unfollowed users
MAX_UNFOLLOWS = 200  # Ensure exactly 200 users are unfollowed
BATCH_SIZE = 7  # Number of users to unfollow before scrolling


def log_unfollowed_user(username):
    """Log the username of the unfollowed user to a file."""
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{username}\n")


def scroll_down():
    """Scroll down to load more users in the 'Following' list."""
    driver.execute_script("window.scrollBy(0, 800);")  # Scroll down
    time.sleep(random.uniform(3, 5))  # Randomized wait to mimic human behavior


def unfollow_users():
    """Find and unfollow exactly 200 users, scrolling as needed."""
    unfollowed_count = 0

    while unfollowed_count < MAX_UNFOLLOWS:
        # Find all "Following" buttons under the correct container
        unfollow_buttons = driver.find_elements(By.XPATH, "//button[text()='Following']")

        if not unfollow_buttons:
            print("⚠️ No unfollow buttons found, scrolling for more users...")
            scroll_down()
            continue  # Retry after scrolling

        print(f"🔍 Found {len(unfollow_buttons)} users to unfollow.")

        for i, button in enumerate(unfollow_buttons):
            if unfollowed_count >= MAX_UNFOLLOWS:
                break  # Stop once we hit 200

            try:
                driver.execute_script("arguments[0].scrollIntoView();", button)  # Ensure button is visible
                time.sleep(random.uniform(1, 2))  # Small delay

                # Try to find the username (adjust XPath based on TikTok's structure)
                try:
                    username_element = button.find_element(By.XPATH, "./ancestor::div//a[contains(@href, '/@')]")
                    username = username_element.get_attribute("href").split("/")[-1]
                except:
                    username = "Unknown_User"

                # Click the "Following" button to unfollow
                button.click()
                time.sleep(random.uniform(2, 3))  # Delay between clicks

                # Confirm the unfollow pop-up (if TikTok asks)
                confirm_button = driver.find_elements(By.XPATH, "//button[contains(text(), 'Unfollow')]")
                if confirm_button:
                    confirm_button[0].click()
                    time.sleep(random.uniform(2, 3))

                # Log the unfollowed user
                log_unfollowed_user(username)
                unfollowed_count += 1
                print(f"🚀 Unfollowed {username} ({unfollowed_count}/{MAX_UNFOLLOWS}).")

                time.sleep(random.uniform(3, 6))  # Random delay to avoid detection

            except Exception as e:
                print(f"❌ Error while unfollowing: {e}")

            # Scroll after every 7 unfollows
            if (i + 1) % BATCH_SIZE == 0:
                print("🔄 Scrolling down for more users...")
                scroll_down()

        if unfollowed_count < MAX_UNFOLLOWS:
            scroll_down()  # Keep scrolling to load more users

    print(f"✅ Unfollowed {unfollowed_count} users. Task Complete!")


# Main execution
try:
    # Open TikTok and log in
    driver.get("https://www.tiktok.com/login")
    time.sleep(5)

    # Wait for user to log in
    input("🔄 Please log in to your TikTok account and then press Enter to continue...")

    # Navigate to profile page
    driver.get(f"https://www.tiktok.com/@{TIKTOK_USERNAME}")
    print("✅ Navigated to your profile page.")
    time.sleep(5)

    print("🔄 Please manually click on the 'Following' button to open the list.")
    input("👉 Press Enter after you've opened the 'Following' tab...")

    # Start unfollowing users
    unfollow_users()

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
