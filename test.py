from distutils.command.config import config
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Users\putra\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

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
    if char == 'B' or charr == 'S':
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
        print("cuma 2")
        el = typo(arr[0])
        if el == '+' or el == '*' or el == '-':
            arr.insert(0, '1')
            return arr
        if el == 'v' or el == 'V':
            arr.insert(0, '1')
            arr[1] = '*'
            return arr
        el = typo(arr[1])
        print("el 2", el)
        if el == '+' or el == '*' or el == '-':
            arr.insert(2, '1')
            return arr
        if arr[1] == ']':
            arr.insert(2, '1')
            arr[1] = '-'
            return arr
    elif len(arr) == 3:
        if arr[0] == 'S' and arr[1] == '|' and arr[2] == ']':
            return ['8','-','1']
    elif len(arr) == 4:
        el = typo(arr[0])
        if el == 'S':
            return arr
        if el != '1':
            arr.pop(1)
            return arr
        if arr[0] == '1' and arr[1] == '+' and arr[2] == '/' and arr[3] == '7':
            return ['1','+','7']
    if typo(arr[0]) == '0':
        arr.insert(0, '1')
        return arr
    return arr

def captcha():
    #screenshot
    img = Image.open('1+7.png')

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
    output = pytesseract.image_to_string(img, config=cong)
    print(list(output))
    img.show()

    #calculate
    print("old list:", list(output)) 
    captchaArr = checkArr(list(output))
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


print("start test")
captcha()
