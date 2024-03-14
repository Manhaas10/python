import requests

#for downloading opening another file
image_link=requests.get('https://w0.peakpx.com/wallpaper/27/938/HD-wallpaper-one-piece-the-king-of-hell.jpg')
f=open("zoro.jpg","wb")
f.write(image_link.content)
f.close()