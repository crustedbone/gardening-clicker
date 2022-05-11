import pyautogui
import time
import keyboard
import win32api, win32con
from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Users\putra\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

time.sleep(1)
print("start bot")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def clickNumber(num):
    if num == 1:
        click(1239,616)
    elif num == 2:
        click(1340,616)
    elif num == 3:        
        click(1444,616)
    elif num == 4:
        click(1239,727)
    elif num == 5:
        click(1340,727)
    elif num == 6:
        click(1444,727)
    elif num == 7:
        click(1239,835)
    elif num == 8:
        click(1340,835)
    elif num == 9:
        click(1444,835)
    elif num == 0:
        click(1541,727)

def clickGarden():
    click(1190, 458)

def printTypo(char):
    print("print typo:", char)
    return char

def typo(char):
    if char == 'j' or char == 'i' or char == 'l' or char == '[' or char == ']' or char == '|':
        return printTypo('1')
    if char == 's':
        return printTypo('5')
    if char == 'o':
        return printTypo('0')
    if (char >= 'A' and char <= 'Z' and char == 'G'):
        return printTypo('6')
    elif (char >= 'a' and char <= 'z' and char == 'g') or char == 'q':
        return printTypo('9')
    if char == 'B' or char == 'S':
        return printTypo('8')
    if char == '/':
        return printTypo('7')
    return printTypo(char)

def typo2(char,add):
    if char == '4' or char == '9' and add == 'true':
        return printTypo('+')
    return printTypo(char)

def checkArr(arr):
    if arr[len(arr)-1] == '\n':
        arr.pop()
    if len(arr) < 3:
        el = typo(arr[0])
        if el == '+' or el == '*' or el == '-':
            arr.insert(0, '1')
            return arr
        if el == 'v' or el == 'V' or el == '"':
            arr.insert(0, '1')
            arr[1] = '*'
            return arr
        el = typo(arr[1])
        if el == '+' or el == '*' or el == '-':
            arr.insert(2, '1')
            return arr
        if arr[1] == ']':
            arr.insert(2, '1')
            arr[1] = '-'
            return arr
    elif len(arr) == 4:
        if arr[0] == 'S' and arr[1] == '—' and arr[2] == '|' and arr[3] == ']':
            return ['8','-','1']
        if arr[0] == '7' and arr[1] == '-' and arr[2] == '9' and arr[3] == '5':
            return ['7','-','5']
        if arr[0] == '1' and arr[1] == '4' and arr[2] == '+' and arr[3] == ']':
            return ['1','+','1']
        if arr[0] == '1' and arr[1] == '+' and arr[2] == '/' and arr[3] == '7':
            return ['1','+','7']
        el = typo(arr[0])
        if el != '1':
            arr.pop(1)
            return arr
    if typo(arr[0]) == '0':
        arr.insert(0, '1')
        return arr
    return arr

def captcha(counter):
    #screenshot
    img = pyautogui.screenshot(region=(921,528,80,36))
    #img.save('captchaSS '+str(counter)+'.png')

    #transform
    new_size = tuple(8*x for x in img.size)
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    img = img.convert("RGB")
    d = img.getdata()
    new_image = []
    for item in d:
        if item[0] in list(range(238, 256)):
            new_image.append((0, 0, 0))
        else:
            new_image.append((255,255,255))
    img.putdata(new_image)

    #image to string
    cong = r'outputbase --oem 1'
    output = pytesseract.image_to_string(img)
    #img.save('captchaTransform '+str(counter)+'.png')
    #print("img saved")

    #calculate
    captchaArr = checkArr(list(output))
    print("old list:", list(output))
    print("new list:", captchaArr)
    arrLen = len(captchaArr)
    calculate = 0
    if arrLen == 3:
        x = typo(captchaArr[arrLen-3])
        y = typo(captchaArr[arrLen-1])
        if typo2(captchaArr[arrLen-2], 'true') == '+':
            calculate = int(x)+int(y)
        elif captchaArr[arrLen-2] == '-' or captchaArr[arrLen-2] == '—':
            calculate = int(x)-int(y)
        elif captchaArr[arrLen-2] == '*':
            calculate = int(x)*int(y)
    else:
        x = typo(captchaArr[arrLen-4])
        y = typo(captchaArr[arrLen-3])
        z = typo(captchaArr[arrLen-1])
        if typo2(captchaArr[arrLen-2], 'true') == '+':
            calculate = int(""+x+y)+int(z)
        elif captchaArr[arrLen-2] == '-':
            calculate = int(""+x+y)-int(z)
        elif captchaArr[arrLen-2] == '*':
            calculate = int(""+x+y)*int(z)   
    print("cal:", calculate)

    #fill captcha
    click(968,607)
    time.sleep(0.2)
    if calculate >= 20:
        clickNumber(2)
        time.sleep(0.2)
        calculate = calculate - 20
        clickNumber(calculate)
    elif calculate >= 10:
        clickNumber(1)
        time.sleep(0.2)
        calculate = calculate - 10
        clickNumber(calculate)
    else:
        clickNumber(calculate)
    time.sleep(0.2)
    
    #submit captcha
    click(969,759)
    time.sleep(0.2)
    click(969,759)
    time.sleep(0.2)

    #click gardening
    clickGarden()

def toggle(flag):
    if flag == True:
        print("unpause")
        return False
    else:
        print("pause")
        return True

def pause():
    print("pause")
    while keyboard.is_pressed('+') == False:
        time.sleep(0.5)
    print("unpause")
    
#list to do
    #loop
        #click gather
        #if captcha = do captcha
        #endif
    #endloop
    
#loop
counter = 0
while keyboard.is_pressed('esc') == False and pyautogui.pixel(1612,75)[2] == 255:
    #pause/unpause
    if keyboard.is_pressed('k') == True:
        pause()
    #click gather
    if pyautogui.pixel(1180, 509)[0] == 255:
        clickGarden()
        time.sleep(0.3)
    #captcha
    if 250 <= pyautogui.pixel(681, 533)[0] <= 255:
        captcha(counter)
        counter = counter + 1
print("end bot")
