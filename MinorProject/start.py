from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, abort, send_file
import cv2, pafy
import pytesseract
from PIL import Image
import os
from string_matching import compairing_strings

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' 

def to_append(text):
	filename = 'notes'+'.txt'
	file = open(filename, 'a')
	file.write(text+' ')
	file.close()


def convert_image():
    ct=1
    name = 'kang' + str(ct) + '.jpg'
    check = './' + name
    text_prev=''
    while os.path.isfile(check):
        img = Image.open(name)
        current_text = pytesseract.image_to_string(img)
        #to_append(current_text,ct+1000)
        #to_append(current_text,v_ct+100)
		
        text=compairing_strings(text_prev,current_text)
        to_append(text)
        
        text_prev = current_text
        ct=ct+1
        name = 'kang' + str(ct) + '.jpg'
        check = './' + name



def remove_images():
  t=1
  name = 'kang' + str(t) + '.jpg'
  print(name)
  check = './' + name
  while os.path.isfile(check):
    os.remove(name)
    t=t+1
    name = 'kang' + str(t) + '.jpg'
    check = './' + name

def clear_notes():
	name= 'notes.txt'
	check='./'+ name
	while os.path.isfile(check):
		os.remove(name)

@app.route('/', methods=['GET', 'POST'])
def main_page():
	if request.method == "POST":
		url = request.form['Link']
		vPafy = pafy.new(url)
		play = vPafy.getbest(preftype="mp4")
		cap = cv2.VideoCapture(play.url)
		remove_images()
		clear_notes()
		i,j=1,1
		while(cap.isOpened()):
			ret, frame = cap.read()
			if ret == False:
				break
			if i%150 == 0:
				cv2.imwrite('kang'+str(j)+'.jpg',frame)
				j=j+1
			i+=1
		cap.release()
		cv2.destroyAllWindows()
		convert_image()
		return redirect(url_for('done'))
	else:
		return render_template('home.html')

@app.route('/done')
def done():
	path='notes.txt'
	return send_file(path,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)