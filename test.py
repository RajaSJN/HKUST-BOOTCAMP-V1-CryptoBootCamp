from PIL import Image
import zbarlight
# from src.scripts import utils_ke
import hashlib

file_path = 'qrImg.jpg'
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()

codes = zbarlight.scan_codes(['qrcode'], image)
print('QR codes: %s' % codes)
with open("randomfile.txt", "a") as o:
        o.write('Hello')
        o.write('This text will be added to the file')
test = "3b678beed4876f03618f7bf81f5c6000eb029ec63c8ec8293d1d1020ba66c6e8"
test += "dummy"
# print(utils_key.hash("Soemthing",//1))
# test = hashlib.sha256(str(codes).encode('utf-8')).hexdigest()
print(hashlib.sha256(str(test).encode('utf-8')+bytes(1700)).hexdigest())