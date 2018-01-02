# qrcodeTest.py

import qrcode
from PIL import Image

class qrGenerator():
	def  __init__(self, first_name, last_name, job_title,email,phone, website_url, git_url):
		self.first_name 	= first_name 
		self.last_name		= last_name
		self.full_name		= first_name+" "+last_name
		self.job_title 		= job_title
		self.website_url	= website_url
		self.git_url		= git_url
		self.email			= email
		self.phone			= phone
		qrobj				=	qrcode.QRCode(
										   version=1,
										   error_correction=qrcode.constants.ERROR_CORRECT_L,
										   box_size=10,
										   border=4,
										)
		self.qrs 			= qrobj

	def createQr(self):
		print("Start generating QR Code .")

		qr_data = [self.full_name+"\n", self.job_title+"\n", self.email+"\n", self.phone+"\n", self.website_url+"\n", self.git_url+"\n"]
		for items in qr_data:
			self.qrs.add_data(items)

		self.qrs.make(fit=True)

	def generateImage(self):
		print("Start Generating Image .")
		image = self.qrs.make_image()
		print("Saving %s" % self.first_name+".png")
		image.save(self.first_name+".png")
		image.close()
		print("Image %s" % self.first_name+".png" + " was created .")

	def showQr(self):
		qrImage = Image.open(self.first_name+'.png')
		qrImage.show()