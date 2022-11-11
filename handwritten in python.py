import pywhatkit as kit
from PIL import Image
Handwritten=input("Enter your text to convert in Handwriting ")
kit.text_to_handwriting(Handwritten,save_to="za.png")
Image.open("za.png")
