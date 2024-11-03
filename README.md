Automated Browser Script
This project contains a Python script that automates the process of opening Microsoft Edge, navigating to YouTube, and performing a search.

Prerequisites
Python 3.x
pyautogui library
Microsoft Edge browser
Screenshots of the Microsoft Edge icon, YouTube search bar, and YouTube search icon saved in the same directory as main.py
Installation
Clone the repository or download the script.
Install the required Python library:
pip install pyautogui
Usage
Ensure that the screenshots of the Microsoft Edge icon, YouTube search bar, and YouTube search icon are saved in the same directory as main.py with the following filenames:

edge_icon.png
youtube_search_bar.png
youtube_search_icon.png
Run the script:
python main.py

Script Details
The script performs the following steps:

Waits for 3 seconds.
Locates the Microsoft Edge shortcut on the desktop and clicks on it.
Waits for 3 seconds to allow the browser to open.
Navigates to YouTube by typing the URL and pressing Enter.
Waits for 5 seconds to allow YouTube to load.
Locates the YouTube search bar or search icon, types "hello", and presses Enter.
Waits for 5 seconds to allow the search results to load.
Prints "Script completed."
Error Handling
If the Microsoft Edge shortcut is not found, the script prints "Microsoft Edge shortcut not found on the desktop."
If the YouTube search bar or search icon is not found, the script prints "YouTube search icon not found on the page."
Notes
The script uses relative paths to locate the images. Ensure that the images are in the same directory as main.py.
Adjust the confidence parameter in the pyautogui.locateOnScreen function if the script has trouble locating the images.
License
This project is licensed under the MIT License.