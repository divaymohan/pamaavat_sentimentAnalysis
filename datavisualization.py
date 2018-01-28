from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
import pandas as pd
import numpy as np

data = pd.DataFrame()

data = pd.read_csv('padmavat.txt')
data['polarity'] = data

objects = ('negative','positive','neutral')
negcount = 0
poscount = 0
neucount = 0
for item in data['polarity']:
    if(item<0):
        negcount = negcount+1
    elif(item>0):
        poscount=poscount+1
    else:
        neucount=neucount+1
observation = [float(negcount),float(poscount),float(neucount)]


