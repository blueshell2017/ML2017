from PIL import Image

im = Image.open("westbrook.jpg")
pix = im.load()
x,y = im.size[0],im.size[1]
newim = Image.new("RGB",(x,y))
for i in range(x):
    for j in range(y):
        newim.putpixel([i,j],tuple([int(x/2) for x  in pix[i, j]]))

newim.show()
newim.save("A2.jpg")
