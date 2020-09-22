

# import csv
# os.path.join

import os
import csv


print(os.getcwd())

os.chdir("C:/Users/culics/Desktop/diplomarbeit/Dateien_Alle")

with open("C:/Users/culics/Desktop/diplomarbeit/Dateien_Alle/Mappe_Neu.csv") as f:
    print(f.read())



