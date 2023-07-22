import qrcode
from resizeimage import resizeimage

def Generate(text):
    data=text
    qr=qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(data)
    qr.make(fit=True)
    image=qr.make_image(fill='black',back_color='white')
    image=resizeimage.resize_cover(image,[250,250])
    image.save("static/QRIMAGE.png")
    