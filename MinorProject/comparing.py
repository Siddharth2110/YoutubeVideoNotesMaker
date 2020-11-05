from pathlib import Path

def comparing_string(s1, s2):
	ans = ''
	if abs(len(s1)-len(s2))>5 and len(s2)>5:
		 m1 = {}
		 m2 = {}
		 dupletes = set()
		 pos1=pos2=0
		 while(pos1<len(s1)-10 and pos2<len(s2)-10):
		 	for j in range(0,10):
		 		dupletes.add((s1[pos1],s1[pos1+1]))
		 		if m1.get((s1[pos1],s1[pos1+1])):
		 			m1[(s1[pos1],s1[pos1+1])]=m1[(s1[pos1],s1[pos1+1])]+1
		 		else:
		 			m1[(s1[pos1],s1[pos1+1])]=1
		 		pos1+=1
		 		dupletes.add((s2[pos2],s2[pos2+1]))
		 		if m2.get((s2[pos2],s2[pos2+1])):
		 			m2[(s2[pos2],s2[pos2+1])] = m2[(s2[pos2],s2[pos2+1])] + 1
		 		else:
		 			m2[(s2[pos2],s2[pos2+1])]=1
		 		pos2+=1

		 	mismatch=0
		 	for i in dupletes:
		 		a = b = 0
		 		if m1.get(i):
		 			a=m1[i]
		 		if m2.get(i):
		 			b=m2[i]
		 		mismatch+=abs(a-b)
		 	if mismatch>3 and 10*mismatch>pos1+pos2:
		 		break

		 for i in range(pos2,len(s2)):
		 	ans+=s2[i]

	return ans

print("Enter first string: ")
str1 = Path('input.txt').read_text()
str2 = Path('input2.txt').read_text()
print(type(str1))
#print(str2)
print(comparing_string(str1,str2))
