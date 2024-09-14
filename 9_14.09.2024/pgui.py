import pyautogui

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
posx, posy = pyautogui.position()
print(posx, posy)
# pyautogui.alert('This is an alert box.')
# pyautogui.confirm('Shall I proceed?')
# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
# pyautogui.prompt('What is your name?')
# pyautogui.password('Enter password (text will be hidden)')
im1 = pyautogui.screenshot()
im1.save('button.png')
# im2 = pyautogui.screenshot('my_screenshot2.png')
# buttonx, buttony = pyautogui.locateCenterOnScreen('button.png')
# print(buttonx, buttony)
# pyautogui.useImageNotFoundException()
# try:
#     location = pyautogui.locateOnScreen('button.png')
#     print('image found')
# except pyautogui.ImageNotFoundException:
#     print('ImageNotFoundException: image not found')
pyautogui.locate('button.png', 'button1.png')