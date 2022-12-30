f1 = open("oldImage.jpg", "rb")
f2 = open("newImage.jpg", "wb")

data = f1.read()
f2.write(data)