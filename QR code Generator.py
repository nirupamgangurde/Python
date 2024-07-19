import qrcode as qr
img = qr.make("https://github.com/nirupamgangurde")
img.save("Testqr.jpg")