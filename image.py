from PIL import Image
import pickle

##vars
file = "save"
sfile = "images/img"
##/vars

save = pickle.load( open( file, "rb" ) )
width = len(save[0])
heigh = len(save[0][0])
count = 0
for i in save:
    img = Image.new( "1" , (width,heigh), "white")
    pixel = img.load()
    for x in range(width):
        for y in range(heigh):
            if i[x][y]:
                pixel[x,y] = (0)
    print("saving...", count)
    img.save((str(sfile) + str(count) + ".png"))
    count += 1
