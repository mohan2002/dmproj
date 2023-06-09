# -*- coding: utf-8 -*-
"""coursera-course-recommendation-engine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U5zB41vc3BQPXAc1gj1GQwMx3SV6BGvq

# Coursera Course Recommendation Engine and Visualization📚

## 1. Importing necessary libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
sns.set_style('darkgrid')
plt.style.use('fivethirtyeight')
print("The necessary packages are included successfully!")
import pickle


"""## 2. Importing the dataset"""

df = pd.read_csv('Coursera.csv')
df.head()

def datainjson():
    json_data = df.head(100).to_json(orient='records')
    return json_data

print(datainjson())


pickle_out = open('predictor.pkl','wb')
pickle.dump(datainjson(),pickle_out)
pickle_out.close()


