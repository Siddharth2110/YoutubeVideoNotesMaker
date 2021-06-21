from skimage.metrics import structural_similarity
import cv2
import os
from csv import writer
import time

#Works well with images of different dimensions
def orb_sim(img1, img2):
  # SIFT is no longer available in cv2 so using ORB
  orb = cv2.ORB_create()

  # detect keypoints and descriptors
  kp_a, desc_a = orb.detectAndCompute(img1, None)
  kp_b, desc_b = orb.detectAndCompute(img2, None)

  # define the bruteforce matcher object
  bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
  #perform matches. 
  matches = bf.match(desc_a, desc_b)
  #Look for similar regions with distance < 50. Goes from 0 to 100 so pick a number between.
  similar_regions = [i for i in matches if i.distance < 50]  
  if len(matches) == 0:
    return 0
  return len(similar_regions) / len(matches)


#Needs images to be same dimensions
def structural_sim(img1, img2):

  sim, diff = structural_similarity(img1, img2, full=True)
  return sim

def calculate_sim():
  ct=1
  name = 'kang' + str(ct) + '.jpg'
  print(name)
  check = './' + name
  ct=ct+1
  img_prev='kang' + str(ct) + '.jpg'
  check = './' + name
  avg_sim_orb=0
  avg_sim_ssim=0
  while os.path.isfile(check):
    img = cv2.imread(name,0)
    img2= cv2.imread(img_prev, 0)
  
    orb_similarity = orb_sim(img, img2)  #1.0 means identical. Lower = not orb_similarity
    print("Similarity using ORB is: ", orb_similarity)
    avg_sim_orb = avg_sim_orb + orb_similarity

    ssim = structural_sim(img, img2) #1.0 means identical. Lower = not similar
    print("Similarity using SSIM is: ", ssim)
    avg_sim_ssim = avg_sim_ssim + ssim 

    ct=ct+1
    img_prev=name
    name = 'kang' + str(ct) + '.jpg'
    check = './' + name

  avg_sim_ssim = avg_sim_ssim/(ct-2)
  avg_sim_orb = avg_sim_orb/(ct-2)
  print("avg orb similarity: ", avg_sim_orb)
  print("avg ssim similarity: ", avg_sim_ssim)
  List=[avg_sim_orb,avg_sim_ssim]
  with open('avg_similarity_2.csv', 'a') as f_object: 
      writer_object = writer(f_object,lineterminator='\r') 
      writer_object.writerow(List) 
  
      f_object.close()

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

def main_func():
  cnt=1
  while cnt<7:
    remove_images()
    name = 'videos\\Image_Videos\\video_' + str(cnt) + '.mp4'
    print(name)
    j,i = 1,1
    cam = cv2.VideoCapture(name)
    while (cam.isOpened()):
      ret, frame = cam.read()
      if ret == False:
        break
      if i%150 == 0:
        print(j)
        cv2.imwrite('kang'+str(j)+'.jpg',frame)
        j=j+1
      i+=1

    cam.release()
    cv2.destroyAllWindows()
    calculate_sim()
    cnt=cnt+1
    

main_func()

