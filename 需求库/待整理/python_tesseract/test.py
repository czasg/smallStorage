from PIL import Image
import pytesseract
#c = Image.open('123.png')
#c = Image.open('123.png')
#c = Image.open('8069.png')
#c = Image.open('8069a.png')
#c = Image.open('abcd1234.png')
c = Image.open('6666_0.png')
#c = c.resize((300,60))
#c.save('11111.png')
#c = Image.open('english.png')
#print(c)
#print(c.size,)

def binarizing(img,threshold):
	"""传入image对象进行灰度、二值处理"""
	img = img.convert("L") # 转灰度
	pixdata = img.load()
	w, h = img.size
	# 遍历所有像素，大于阈值的为黑色
	#threshold = 140 
	for y in range(h):
		for x in range(w):
			if pixdata[x, y] > threshold:
				pixdata[x, y] = 1
			else:
				pixdata[x, y] = 0
	return img
#img = binarizing(c,140)
#img.save('666.png')
text = pytesseract.image_to_string(c)#, lang='eng')
print(text,'1111111111111111')
#print('???')


#c = Image.open('b123.png')
#text = pytesseract.image_to_string(c)#, lang='eng')
#print(text,'222222222')


from PIL import Image,ImageEnhance,ImageFilter  
import sys  
from pytesseract import *
# 二值化  
threshold = 140  
table = []  
for i in range(256):  
    if i < threshold:  
    	table.append(0)  
    else:  
    	table.append(1)  
#由于都是数字  
#对于识别成字母的 采用该表进行修正  
rep={'O':'0',  
    'I':'1','L':'1',  
    'Z':'2',  
    'S':'8'  
    };  
  
def  getverify1(name):        
    #打开图片  
    im = Image.open(name)  
    #转化到灰度图
    imgry = im.convert('L')
    #保存图像
    imgry.save('g'+name)  
    #二值化，采用阈值分割法，threshold为分割点 
    out = imgry.point(table,'1')  
    out.save('b'+name)  
    #识别  
    text = image_to_string(out)  
    print(text)
    #识别对吗  
    #text = text.strip()  
    #text = text.upper();    
    #for r in rep:  
    #	text = text.replace(r,rep[r])   
    #out.save(text+'.jpg')  
    #print (text)  
    #return text  
getverify1('123.png')




# 图片二值化
from PIL import Image
Img = Image.open('g123.png')
 
# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
#Img = img.convert('L')
#Img.save("test1.jpg")
 
# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 100
 
table = []
for i in range(256):
    if i < threshold:
    	table.append(1)
    else:
    	table.append(0)
 
print(table)

# 图片二值化
photo = Img.point(table, '1')
photo.save("test2.png")
