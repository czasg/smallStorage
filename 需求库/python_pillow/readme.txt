# this is no all way
# todo, after the order complete, read the official documentations

from PIL import Image
img = Image.open(path_to_img)
width, height = img.size  -> return size of picture
img = img.thumbnail((wide//2, high//2))  -> half shrinking
img.save(path_to_new_img, save_model)

from PIL import Image, ImageFilter
img = Image.open(path_to_img)
img.filter(ImageFilter.BLUR)
img.save(path_to_new_img, save_model)

from PIL import Image,ImageDraw,ImageFont,ImageFilter
-> new a figure
img = Image.new('RGB', (width,height), (255,255,255))  -> 255 mean a white figure
-> set the font for char
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
-> prepare the environment of drawing figure
draw = ImageDraw.draw(img)
-> drawing the background
draw.point((x, y), fill=(0,0,0))  -> point() to appoint coordinate, color is (0,0,0) which mean black
-> drawing the char in the figure
draw.text((60,10), 'A', font=font, fill=(0,0,0))  -> txt() to set coordinate of char 'A', and font is font, color is (0,0,0) black
-> make the figure blur
img = img.filter(ImageFilter.BLUR)
-> done and save
img.save(path_to_new_img, save_model)


