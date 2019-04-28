# todo, package all to a class object

from PIL import Image, ImageDraw, ImageFont, ImageFilter

from random import randint


def rndChar():
    return chr(randint(65, 90))  # A->Z: 65->90, a->z: 97->122, ord()


def rndColor():
    return (randint(64, 255),
            randint(64, 255),
            randint(64, 255))


def rndColor2():
    return (randint(32, 127),
            randint(32, 127),
            randint(32, 127))


# 240 x 60
width = 60 * 4
height = 60

img = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)

draw = ImageDraw.Draw(img)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

img = img.filter(ImageFilter.BLUR)
img.save('test3.jpg', 'jpeg')
