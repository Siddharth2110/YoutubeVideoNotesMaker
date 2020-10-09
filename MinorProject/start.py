from flask import Flask, render_template, request, redirect, url_for, flash
import cv2, pafy
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' 

#def new_data(text,text_prev):

def to_append(text,text_prev):
#	text = new_data(text,text_prev)
	filename = 'notes.txt'
	file = open(filename, 'a')
	file.write(text + "\n")
	file.close()


def main_func():
	ct=1
	name = 'kang' + str(ct) + '.jpg'
	print(name)
	check = './' + name
	text_prev=''
	while os.path.isfile(check):
		img = Image.open(name)
		text = pytesseract.image_to_string(img)
		print(text)
		to_append(text,text_prev)
		text_prev = text
		ct=ct+1
		name = 'kang' + str(ct) + '.jpg'
		check = './' + name


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
	if request.method == "POST":
		url = request.form['Link']
		vPafy = pafy.new(url)
		play = vPafy.getbest(preftype="mp4")
		cap = cv2.VideoCapture(play.url)
		i,j=1,1
		while(cap.isOpened()):
			ret, frame = cap.read()
			if ret == False:
				break
			if i%5000 == 0:
				cv2.imwrite('kang'+str(j)+'.jpg',frame)
				j=j+1
			i+=1
		cap.release()
		cv2.destroyAllWindows()
		main_func()
		return redirect(url_for('done'))
	else:
		return render_template('home.html')

@app.route('/done')
def done():
	return render_template('done.html')

if __name__ == '__main__':
    app.run(debug=True)