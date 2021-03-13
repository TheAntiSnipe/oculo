import cv2
import pytesseract
import requests
import shutil
import re

isWebEntity = input("Is the image on the web? (Y/N): ")

if(isWebEntity == 'Y' or isWebEntity == 'y'):
    enteredUrl = input("Enter image hyperlink: ")

    image = requests.get(
        enteredUrl,
        stream=True,
        headers={"User-agent": "Mozilla/5.0"},
    )

    if image.status_code == 200:
        with open("img.png", 'wb') as f:
            image.raw.decode_content = True
            shutil.copyfileobj(image.raw, f)

    imageData = cv2.imread(r'img.png')

else:
    enteredFilepath = input("Enter the filepath of the image you want to read: ")
    imageData = cv2.imread(fr'{enteredFilepath}')

imageDataRGB = cv2.cvtColor(imageData,cv2.COLOR_BGR2RGB)
imageToText = pytesseract.image_to_string(imageDataRGB)
re.sub(r'^$\n', '', imageToText, flags=re.MULTILINE)
print(imageToText)