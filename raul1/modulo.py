import qrcode
data="RAUL CHOQUE 71993926"
imagen=qrcode.make(data)
imagen.save("qr.png")