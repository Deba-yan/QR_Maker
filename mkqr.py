import qrcode

print("Enter the link : ")
text = input()
qr=qrcode.make(text)
print("Enter the Name of the image through which you want to save the QR code : ")
name = input()
qr.save(name + ".png")
print("succesfully saved the QR code in the current directory with the name " + name + ".png")
