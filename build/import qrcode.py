import qrcode


data = 'Dont forget to subscribe'

img = qrcode.make(data)
 
img.save('C:/Users/Mohammed Hafeez/OneDrive/Desktop/qrcode/myqrcode.png')