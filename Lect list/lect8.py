# работа с изображениями
# python -m pip install Pillow

from PIL import Image

im = Image.open('unnamed.jpg')

w, h = im.size

pixels = im.load()

for i in range(w):
    for j in range(h):
        if (i + j) % 2 == 1:
            pixels[i, j] = (0, 0, 0)

part_im1 = im.crop((0, 0, 200, 200)) # отрезать прямоугольнки
part_im2 = im.crop((300, 0, 500, 200)) # отрезать прямоугольнки

new_im = Image.new(mode = "RGB", size = (200, 400))

part1_pixels = part_im1.load()
part2_pixels = part_im2.load()
new_pixels = new_im.load()

for i in range(part_im1.size[0]):
    for j in range(part_im1.size[1]):
        new_pixels[i, j] = part1_pixels[i, j]
for i in range(part_im2.size[0]):
    for j in range(part_im2.size[1]):
        new_pixels[i, j + 200] = part2_pixels[i, j]    
        
new_im.show()        



