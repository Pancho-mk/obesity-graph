import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

county = []
percent = []

#reading csv file and storing the information in 2 empty lists
#open() should be instructed with the path to the file
with open('Illinois_Obesity_By_County.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for row in csv_reader:
		county.append(row['County'])	
		percent.append(row['Percent_1'])	

#making dictionary from 2 lists and ordering it by the value in descending order
dictionary_i = dict(zip(county, percent))
x = Counter(dictionary_i)
ordered_dict = x.most_common()

#unziping the dictonary into 2 seperate lists
county1 = []
percent1 = []

for item in ordered_dict:
	county1.append(item[0])
	percent1.append(item[1])

#converting the string numbers from the second column into floats
percent2 = list(map(float, percent1))

#taking only the Top 5 values from the lists
county1 = county1[:5]
percent2 = percent2[:5]

print(county1)
print(percent2)
#ploting the results
percent2, county1 = zip(*sorted(zip(percent2, county1), reverse=True))
c = range(len(percent2))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(c, percent2)

plt.xticks(c, county1)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.xticks(c, county1)

plt.title("Illinois Obesity By County - Top 5")
plt.xlabel("Counties")
plt.ylabel("Percent of obese people")

plt.show()