import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

print(screenWidth)
print(screenHeight)

pyautogui.moveTo(600, 1250) # Move the mouse to XY coordinates.
pyautogui.click()
pyautogui.moveTo(500, 70, duration=2)
pyautogui.click()
pyautogui.write('ma-web.nl')
pyautogui.press('enter')

pyautogui.alert('Made by Abdallah')