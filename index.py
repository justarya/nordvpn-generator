import csv
import random
import sys

if __name__ == "__main__":
  if len(sys.argv) == 1:
    total = 10
  else:
    total = sys.argv[1]
  
  with open('data.csv') as f:
    reader = csv.reader(f)
    chosen_row = random.sample(list(reader), int(total))
    for data in chosen_row:
      print(
"""
Username: {}
Password: {}
Expired Date: {}
"""
        .format(*data)
      )