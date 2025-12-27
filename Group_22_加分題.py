import pytesseract
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #直接指定tesseract的主程式位置

img_path = "bonus.png" 
img = cv2.imread(img_path) #打開寫字的圖檔 且將像素資料轉為陣列

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #將彩色影像轉為灰階影像
gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1] #將影像二值化 像素值>150就視為白 像素值小於150視為黑

text = pytesseract.image_to_string(gray, lang="chi_tra+eng", config='--psm 6') #使用灰階及二值化後的圖 語系改成中文及英文 文字區塊模式

print("加分題 OCR 辨識結果：")
print("-" * 40)
print(text) #輸出辨識結果