from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open(input("Enter the file name: ")))
print("Your QR code value: ", decocdeQR[0].data.decode('ascii'))
