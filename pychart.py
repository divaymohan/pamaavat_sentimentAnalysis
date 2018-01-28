import datavisualization
from matplotlib import pyplot as plt

plt.figure()
observation=datavisualization.observation
labels = ['dislike','like','neutral']
plt.pie(observation,labels=labels,autopct='%.2f')
plt.title('padmaavat popularity')
plt.show()