import pyautogui
import time

print("Starting the automated browser script...")
time.sleep(3)

# Step 1: Locate the Microsoft Edge shortcut on the desktop and click on it
try:
    edge_icon_location = pyautogui.locateOnScreen('./edge_icon.png', confidence=0.8)
    if edge_icon_location:
        pyautogui.moveTo(edge_icon_location.left + edge_icon_location.width / 2, edge_icon_location.top + edge_icon_location.height / 2, duration=1.2)
        pyautogui.click()
        pyautogui.click()
    else:
        print("Microsoft Edge shortcut not found on the desktop.")
except pyautogui.ImageNotFoundException:
    print("Microsoft Edge shortcut not found on the desktop.")
time.sleep(3) 

# Step 2: Navigate to YouTube
pyautogui.typewrite('https://www.youtube.com')
pyautogui.press('enter')
time.sleep(5)  # Wait for YouTube to load

# Step 3: Locate the YouTube search bar or search icon, type "hello", and hit Enter
try:
    youtube_search_bar_location = pyautogui.locateOnScreen('./youtube_search_bar.png', confidence=0.8)
    if youtube_search_bar_location:
        pyautogui.moveTo(youtube_search_bar_location.left + youtube_search_bar_location.width / 2, youtube_search_bar_location.top + youtube_search_bar_location.height / 2, duration=2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.typewrite('hello')
        pyautogui.press('enter')
    else:
        youtube_search_icon_location = pyautogui.locateOnScreen('./youtube_search_icon.png', confidence=0.8)
        if youtube_search_icon_location:
            pyautogui.moveTo(youtube_search_icon_location.left + youtube_search_icon_location.width / 2, youtube_search_icon_location.top + youtube_search_icon_location.height / 2, duration=2)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite('hello')
            pyautogui.press('enter')
        else:
            print("YouTube search icon not found on the page.")
except pyautogui.ImageNotFoundException:
    print("YouTube search bar or icon not found on the page.")
time.sleep(5)  # Wait for search results to load

print("Script completed.")