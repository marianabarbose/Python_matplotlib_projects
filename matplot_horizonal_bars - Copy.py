import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('bmh')

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(10):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)


plt.ylabel('Programming languages')
plt.xlabel('Nr of people that uses')
plt.title('Most popular languages')

plt.tight_layout()

plt.show()
