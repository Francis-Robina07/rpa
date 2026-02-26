Day 4 – RPA & Automation (PyAutoGUI + Playwright)

This folder contains simple RPA-style automation demos using pyautogui (desktop GUI automation) and playwright (browser automation).

Structure

pyautogui/

whatsapp_automation.py – Script that:
Opens Windows Search
Launches WhatsApp Desktop
Searches for a contact
Sends a predefined message automatically

playwright/

wikipedia_extractor.py – Script that:
Opens Wikipedia
Searches for a topic
Extracts the first valid paragraph
Formats the text properly
Saves output into output.txt

Prerequisites

Create/activate a virtual environment (optional but recommended) and install dependencies:

Windows:

python -m venv myenv
myenv\Scripts\activate

macOS / Linux:

python3 -m venv myenv
source myenv/bin/activate

Install required packages:

pip install pyautogui pyperclip playwright
playwright install

On Windows/macOS, you may need to grant Accessibility or Screen Recording permissions for pyautogui.

Run PyAutoGUI script

From the project folder:

python whatsapp_automation.py

Before running:
Update "contact_name" inside the script.
Make sure WhatsApp Desktop is installed.
Do not move the mouse while the script runs.

Run Playwright script

From the project folder:

python wikipedia_extractor.py

After execution:
output.txt will be created.
The extracted paragraph will be saved in formatted multiple lines.
