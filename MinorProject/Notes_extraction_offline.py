import cv2
import pytesseract
from PIL import Image
import os
#from compare import compairing_strings
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' 
print('ee')



class compare_object:
    def __init__(self):
        self.uni = dict()
        self.uni['str']=0
        self.di = dict()
        self.di['str','str']=0;
        self.tri = dict()
        self.tri['str','str','str']=0


def match_with_pos(pos,ss1,ss2):

    s1=""
    s2=""

    for i in ss1:
        if(i.isalnum() or i=='.' or i==',' or i=='!' or i==' ' or i=='-'):
            s1=s1+i


    for i in ss2:
        if(i.isalnum() or i=='.' or i==',' or i=='!' or i==' ' or i=='-'):
            s2=s2+i


    ob1=compare_object()
    ob2=compare_object()
    
    if(pos+50<len(s1) and len(s2)>=50):
        
        for i in range(50):
            if(s2[i] in ob2.uni):
                ob2.uni[s2[i]]=ob2.uni[s2[i]]+1
            else:
                ob2.uni[s2[i]]=1
            
            if(i<49):
                if((s2[i],s2[i+1]) in ob2.di ):
                    ob2.di[s2[i],s2[i+1]]=ob2.di[s2[i],s2[i+1]]+1
                else:
                    ob2.di[s2[i],s2[i+1]]=1
                
                if(i<48):
                    
                    if((s2[i],s2[i+1],s2[i+2]) in ob2.tri):
                        ob2.tri[s2[i],s2[i+1],s2[i+2]]=ob2.tri[s2[i],s2[i+1],s2[i+2]]+1
                    else:
                        ob2.tri[s2[i],s2[i+1],s2[i+2]]=1
                
        
                
        for xx in range(50):
            i=xx+pos
            if(s1[i] in ob1.uni):
                ob1.uni[s1[i]]=ob1.uni[s1[i]]+1
            else:
                ob1.uni[s1[i]]=1
                
            if(xx<49):
                if((s1[i],s1[i+1]) in ob1.di):
                    ob1.di[s1[i],s1[i+1]]=ob1.di[s1[i],s1[i+1]]+1
                else:
                    ob1.di[s1[i],s1[i+1]]=1
                
                if(xx<48):
                    
                    if((s1[i],s1[i+1],s1[i+2]) in ob1.tri):
                        ob1.tri[s1[i],s1[i+1],s1[i+2]]=ob1.tri[s1[i],s1[i+1],s1[i+2]]+1
                    else:
                        ob1.tri[s1[i],s1[i+1],s1[i+2]]=1
                        
                        
        points=0
        
        keywords_count=0
        for key in ob2.uni:
            if(key in ob1.uni):
                points=points+ob1.uni[key]
                
        
        
        
        for key in ob2.di:
            if(key in ob1.di):
                points=points + 2*ob1.di[key]
                
                
        for key in ob2.tri:
            if(key in ob1.tri):
                points=points + 3*ob1.tri[key]
                
        return points
    
    else:
        return 0
                
def finalresult(s1,s2):
    ans=""
    m1=dict()
    m1['str','str']=0
    m2=dict()
    m2['str','str']=0
    dupletes=set()
    pos1=0
    pos2=0
    while(pos1<len(s1)-10 and pos2<len(s2)-10):
        
        for j in range(10):
            dupletes.add((s1[pos1],s1[pos1+1]))
            if (s1[pos1],s1[pos1+1]) in m1:
                m1[s1[pos1],s1[pos1+1]]=m1[s1[pos1],s1[pos1+1]]+1
            else:
                m1[s1[pos1],s1[pos1+1]]=1
                
            dupletes.add((s2[pos2],s2[pos2+1]))
            if (s2[pos2],s2[pos2+1]) in m2:
                m2[s2[pos2],s2[pos2+1]]=m2[s2[pos2],s2[pos2+1]]+1
            else:
                m2[s2[pos2],s2[pos2+1]]=1
            
            pos1=pos1+1
            pos2=pos2+1
        
        mismatch=0
        for key in dupletes:
            if key not in m1:
                m1[key]=0
            if key not in m2:
                m2[key]=0
            mismatch=mismatch+abs(m1[key]-m2[key])
        if mismatch>3 and 10*mismatch>(pos1+pos2):
            break
    
    return s2[pos2:]
            


def compairing_strings(ss1,ss2):

    s1=""
    s2=""

    for i in ss1:
        if(i.isalnum() or i=='.' or i==',' or i=='!' or i==' ' or i=='-'):
            s1=s1+i


    for i in ss2:
        if(i.isalnum() or i=='.' or i==',' or i=='!' or i==' ' or i=='-'):
            s2=s2+i

    ans=s2
    val=1
    pos=-1
    for i in range(len(s1)-50):
        if(match_with_pos(i,s1,s2)>val):
            val=match_with_pos(i,s1,s2)
            pos=i
           
    if (pos!=-1):
        return finalresult(s1[pos:],s2)
    
    return ans



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

def to_append(text,v_ct):
	filename = 'notes' + str(v_ct)+'.txt'
	file = open(filename, 'a')
	file.write(text+' ')
	file.close()


def convert_image(v_ct):
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
        to_append(text,v_ct)
        
        text_prev = current_text
        ct=ct+1
        name = 'kang' + str(ct) + '.jpg'
        check = './' + name

def main_func():
  cnt=1
  while cnt<46:
    remove_images()
    name = 'videos\\No_Image_Videos\\video_' + str(cnt) + '.mp4'
    #print(name)
    j,i = 1,1
    cam = cv2.VideoCapture(name)
    print(name)
    while (cam.isOpened()):
      ret, frame = cam.read()
      if ret == False:
        break
      if i%150 == 0:
        cv2.imwrite('kang'+str(j)+'.jpg',frame)
        j=j+1
      i+=1

    cam.release()
    cv2.destroyAllWindows()
    convert_image(cnt)
    cnt=cnt+1

print('function begins____')
main_func()