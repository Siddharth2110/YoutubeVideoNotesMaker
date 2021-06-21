import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#data = pd.read_csv(r'avg_similarity.csv')
#y1=data.ORB_Avg_Similarity.to_list()
#y2=data.Structural_Avg_Similarity.to_list()
#print(y1)
#print(y1.shape)
#print(data.head())
#print(data.index.shape)
data = pd.read_csv(r'extraper.csv')
x = data.Repition_Percentage.to_list()
#plt.plot(data.index.to_list(),y1,label="ORB_similarity")
#plt.plot(data.index.to_list(),y2,label="structural_similarity")
plt.plot(data.index.to_list(),x,label="Repetition_Percentage")
#plt.hist(x, bins=2)
plt.xlabel('Videos')
plt.ylabel('Repetition Percentage')
plt.title('Repetition Percentage Graph')
plt.legend()
plt.show()

