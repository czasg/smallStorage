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

#  生成图片
img = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象:
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)

# 创建Draw对象:
draw = ImageDraw.Draw(img)

# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊:
img = img.filter(ImageFilter.BLUR)
img.save('test3.jpg', 'jpeg')
