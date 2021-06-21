import os
from csv import writer



def perextra(s1 , s2):
    len1 = len(s1)
    len2 = len(s2)
    extra_word=len2-len1
    extra_percentage= (extra_word/len1)*100
    return abs(extra_percentage)


def main():
	ct=1
	name1 = 'textfiles\\originalfiles\\video_' + str(ct) + '.txt'
	name2 = 'textfiles\\outputfiles\\notes' + str(ct) + '.txt'
	check = './' + name1
	while os.path.isfile(check):
		filename1 = name1
		filename2 = name2
		print(name1)
		file1=open(filename1,encoding='utf-8',errors='ignore') 
		#file1 = open(filename1, 'r')
		#file2 = open(filename2, 'r')
		file2=open(filename2,encoding='utf-8',errors='ignore')
		str1 = file1.read()
		str2 = file2.read()
		extraper = perextra(str1,str2)
		file1.close()
		file2.close()

		with open('extraper2.csv', 'a') as f_object: 
			writer_object = writer(f_object,lineterminator='\r') 
			List=[extraper]
			writer_object.writerow(List) 
			f_object.close()

		ct=ct+1
		name1 = 'textfiles\\originalfiles\\video_' + str(ct) + '.txt'
		name2 = 'textfiles\\outputfiles\\notes' + str(ct) + '.txt'
		check = './' + name1




if __name__ == "__main__":
    main()