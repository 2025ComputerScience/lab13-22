import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #直接指定tesseract的主程式位置

image = Image.open("Q2.png") #打開寫字的圖檔

text = pytesseract.image_to_string(image, lang='eng', config='--psm 10') #語系改成英文 單一字元模式

print("OCR 辨識結果:") 
print("-" * 40)
print(text) #輸出辨識結果