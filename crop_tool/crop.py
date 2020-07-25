from PIL import Image
import PIL, sys
import os
list = []
k =0
path = "V:\Coloum"

for (path, dirs, files) in os.walk(path):
    list = files

for i in list:
    ka = "{}\{}".format(path,i)
    print(ka)
    print(i)
    img = Image.open(ka)
    w,h = img.size
    x = 0
    
    while True:
        if x <= 4720: #472*10 means 10 pics each pic height 472
            k = k+1      
            inc = 472+ x
            if inc < h:
                area =(0,0+x,w,inc)
                cropped_img =img.crop(area)
                cropped_img.save("C:\python\Char_C\img{}.jpg".format(k))
                x = x+ 472
            elif inc >= h:
                area =(0,0+x,w,h)
                cropped_img =img.crop(area)
                cropped_img.save("C:\python\Char_C\img{}.jpg".format(k))
                break