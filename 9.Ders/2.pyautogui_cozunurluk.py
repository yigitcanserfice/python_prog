import pyautogui

# Ekran Cozunurlugu
screenWidth, screenHeight = pyautogui.size()
print("Ekran Cozunurlugu  :", screenWidth, screenHeight)

# Fare Pozisyonu
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
