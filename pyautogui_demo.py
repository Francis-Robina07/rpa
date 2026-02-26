import pyautogui
import pyperclip
import time

# Give yourself 5 seconds to move hands away
time.sleep(5)

# 1️⃣ Open Windows Search
pyautogui.press('win')
time.sleep(1)

# 2️⃣ Type WhatsApp
pyautogui.write('WhatsApp', interval=0.1)
time.sleep(1)

# 3️⃣ Press Enter
pyautogui.press('enter')
time.sleep(5)   # Wait for WhatsApp to fully open

# 4️⃣ Search for Contact
pyautogui.click(465,157)
time.sleep(2)

pyautogui.write('contact_name', interval=0.1)
time.sleep(1)

# 5️⃣ Open Chat
pyautogui.press('enter')
time.sleep(2)

# 6️⃣ Prepare Message
message = "Hi "

# Copy to clipboard
pyperclip.copy(message)

# Paste Message
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 7️⃣ Send Message
pyautogui.press('enter')

print("✅ Message Sent Successfully!")