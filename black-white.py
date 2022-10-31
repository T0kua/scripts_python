from PIL import Image, ImageDraw, ImageColor
im = Image.open('1.jpg', 'r')
width, height = im.size

draw = ImageDraw.Draw(im)

def get(w,h):
	p = im.getpixel((w, h))  
	if (p[0] >= 50) and (p[1] >= 50) and (p[2] >= 50) : 
		return (255,255,255)
	else:
		return (0,0,0)
for i in range(width) :
	for j in range(height) :
		im.putpixel((i,j),get(i,j))
	im.save('2#.jpg')

"""
Внимание, вопрос что делает этот скрипт ?
берет картинку 1.jpg и сохраняет её как черно белую в 2#.jpg 
как оно работает ? 
неважно
"""