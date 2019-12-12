import pytesseract
from PIL import Image

image = Image.open('/Users/ranjithm/amfoss-tasks/cap.png')
string = pytesseract.image_to_string(image)
print("The expression is:", string)
x = eval(string)
print("The result is", x)
