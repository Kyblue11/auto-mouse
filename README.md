# Automated Browser Script

This project contains a Python script that automates the process of opening Microsoft Edge, navigating to YouTube, and performing a search.</br>

Author: **Aaron**

## Prerequisites

- Python 3.x
- `pyautogui` library
- Microsoft Edge browser, or other relevant browser `.png`s
- Screenshots of the Microsoft Edge icon, YouTube search bar, and YouTube search icon saved in the same directory as `main.py`

## Installation

1. Clone the repository or download the script.
2. Install the required Python library:
   ```sh
   pip install pyautogui
   ```

## Usage

1. Ensure that the screenshots of the Microsoft Edge icon, YouTube search bar, and YouTube search icon are saved in the same directory as `main.py` with the following filenames:
   - `edge_icon.png`
   - `youtube_search_bar.png`
   - `youtube_search_icon.png`
2. Run the script:
   ```sh
   python main.py
   ```

## Script Details

The script performs the following steps: _(incomplete)_

1. Waits for 3 seconds.
2. Locates the Microsoft Edge shortcut on the desktop and clicks on it.
3. Waits for 3 seconds to allow the browser to open.
4. Navigates to YouTube by typing the URL and pressing Enter.
5. Waits for 5 seconds to allow YouTube to load.
6. Locates the YouTube search bar or search icon, types "hello", and presses Enter.
7. Waits for 5 seconds to allow the search results to load.
8. Prints "Script completed."

## Error Handling

- If the Microsoft Edge shortcut is not found, the script prints "Microsoft Edge shortcut not found on the desktop."
- If the YouTube search bar or search icon is not found, the script prints "YouTube search icon not found on the page."

## Notes

- The script uses relative paths to locate the images. Ensure that the images are in the same directory as `main.py`.
- Adjust the confidence parameter in the `pyautogui.locateOnScreen` function if the script has trouble locating the images.

## License

This project is licensed under the MIT License.
