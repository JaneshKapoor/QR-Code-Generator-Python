#Importing the random and qrcode modules
import random
import qrcode
####Made by Janesh Kapoor(2021466) Vidur Goel(2021364) Yajat Gupta (2021366)####


print("-----------------Welcome to CodeQR-----------------")
#Implementing Classes
class QR:
    def __init__(self,store):
        self.store = store
    def default(self):
    #Using default settings
        makeQR = qrcode.make(self.store)
        makeQR.save("QRcode.png")
    def custom(self,bsize,brdr,fcolor,bcolor):
    #Using Custom settings
        features = qrcode.QRCode(version=1,box_size=bsize,border=brdr)
        features.add_data(self.store)
        makeQR = features.make_image(fill_color=fcolor,back_color=bcolor)
        makeQR.save("QRcode.png")
    def authenticate():
    #Creating Authenticator system
        r = random.randrange(1000,10000)
        makeQR = qrcode.make(str(r))
        makeQR.save("QRcode.png")
        io = input("Enter the four digit code recieved : ")
        if (io == str(r)):
            print("User verified successfully!!!")
        else:
            print("Oops!!! Wrong code")


print("Enter choice 1 for QR code with default settings")
print("Enter Choice 2 for QR code with custom settings")
print("Enter choice 3 for Authenticating QR code")
choice = int(input("Enter choice : "))
if (choice == 1):
    stringlink = input("Enter the string/link to be encoded in your QR code : ")
    QRcaller = QR(stringlink)
    QRcaller.default()
    print("!!!Successfully Created QR Code!!!")
elif(choice == 2):
    stringlink = input("Enter the string/link to be encoded in your QR code : ")
    bsize = int(input("Enter size of the QR box : "))
    brdr = int(input("Enter border value : "))
    fcolor = input("Enter fill color of QR Code : ")
    bcolor = input("Enter back color of QR Code : ")
    QRcaller = QR(stringlink)
    QRcaller.custom(bsize,brdr,fcolor,bcolor)
    print("!!!Successfully Created QR Code!!!")
elif(choice == 3):
    QR.authenticate()
print("--------------Thanks for using CodeQR--------------")