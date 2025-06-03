import qrcode

img = qrcode.make("https://nus.syd1.qualtrics.com/jfe/form/SV_cJghQSpZqPP6VNA")
img.save("qr.png", "PNG")