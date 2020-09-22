

# csv file

import csv

with open("st.csv", "w", newline = '') as f:
    writer = csv.writer(f, delimiter = ",")

    writer.writerow(["one", "two", "three"])

    writer.writerow(["four", "five", "six"])

    
