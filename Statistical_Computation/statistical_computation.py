import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

print(" ")
print("Modules Loaded")
print(" ")

ds = pd.read_csv('./movies_metadata.csv')

print("")
print("Data Loaded")
print("")

print("Data Shape")
print(ds.shape)

print("Data Tail")
print(ds.tail(n = 5))


cols = ds.columns
print("Types of columns")
print(type(cols))

print('--------------')

for ix, k in enumerate(cols):
    print(ix, k)


movie_titles = ds.get('original_title')
print("Movies Titles Type, Shape and Titles")
print(type(movie_titles))
print(movie_titles.shape)
print(movie_titles)

len_titles = []
for ix in movie_titles:
    len_movie = len(ix)
    len_titles.append(len_movie)

print("Print Type of Titles and Length")
print(type(len_titles))
print(len(len_titles))

len_titles = np.array(len_titles)
print(type(len_titles))
print('--------------')
print(len_titles.max())
print(len_titles.min())
print(len_titles.mean())

freq = dict()

for ix in len_titles:
    if ix in freq.keys():
        freq[ix] += 1
    else:
        freq[ix] = 1

print(freq)
print("------------")
print('Keys')
print(freq.keys())
print('------------')
print('Values')
print(freq.values())

print(len(freq.keys()))
print(len(freq.values()))

plt.figure(0)
plt.plot(freq.keys(), freq.values())
plt.show()

# Mean or Expectation - mu
m = 0
for ix in len_titles:
    m += ix
mu = m / float(len(len_titles))
print(mu)

# Varience
m2 = 0
for ix in len_titles:
    m2 += (ix - mu) ** 2
var = m2/ float(len(len_titles))
print(var)


print(len_titles.var())
print(len_titles.std())

std = np.sqrt(var)
print(std)
