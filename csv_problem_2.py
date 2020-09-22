

# ask question and save to file

import csv

answer = input("Add something:")

with open("fav_color.txt", "w") as f:
    f.write(answer)
