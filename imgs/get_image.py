from PIL import ImageTk,Image


def getImageIcon():
    gmail_img = Image.open("imgs/gmail_logo.png")
    width,height = gmail_img.size
    gmail_img = gmail_img.resize((150,100),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(gmail_img)

    return img