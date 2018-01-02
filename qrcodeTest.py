# qrcodeTest.py

import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = ["Miroslav Vasilev", "Python Developer" ,  "http://www.qello.com", "https://github.com/vmiroslav"]

for item in data:
	qr.add_data(item+"\n")


qr.make(fit=True)

img  = qr.make_image()
file_name = "miro-qr.png"
print('Saving %s' % file_name)
image_file = open(file_name, "w")
img.save(file_name)
image_file.close()
