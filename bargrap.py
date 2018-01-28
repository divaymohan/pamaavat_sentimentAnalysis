import datavisualization
from matplotlib import pyplot as plt
import numpy as np


y_pos = np.arange(len(datavisualization.objects))
graph= plt.bar(y_pos, datavisualization.observation, align='center', alpha=0.5)
graph[0].set_color('r')
graph[1].set_color('g')
graph[2].set_color('b')
plt.xticks(y_pos, datavisualization.objects)
plt.ylabel('No of Tweet')
plt.title('Polarity of Tweets')
plt.legend((graph[0],graph[1],graph[2]), ('Negative', 'Positive','Neutral'))

plt.show()
