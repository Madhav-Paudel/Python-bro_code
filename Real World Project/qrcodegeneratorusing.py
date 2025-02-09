# qr code generator using python 
import qrcode
import qrcode.constants
size=int(input("enter the size of box\n"))

sizeB=int(input("enter the size of border\n"))
data=input("enter the data you want to convert to the qr image\n")
color_fill=input("enter the colour you want at the filling\n")
color_back = input("Enter the color you want for the background\n")


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=size,
    border=sizeB
)

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color=color_fill,back_color=color_back)
image_name=input("enter your image name\n")
img.save(image_name+".png")