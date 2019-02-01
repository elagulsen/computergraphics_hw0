RGB = [0, 0, 0]

f= open("image.ppm", "w+")
f.write("P3 500 500 255 ")

for i in range(500):
    for k in range(500):
        RGB[0], RGB[1] = 255,255
        if i % 10 == 0:
            RGB[0] = (i % 128) + 128
        if k % 10 == 0 or i % 10 == 0:
            RGB[1] = (k % 128) + 128
        RGB[2] = int((RGB[0] + RGB[1]) / 2)
        f.write(str(RGB[0]) + ' ' + str(RGB[1]) + ' ' + str(RGB[2]) + ' ')

f.close()
