import os
import pandas as pd
import csv
os.chdir('..')
os.chdir('resources')

# for root, dirs, files in os.walk(os.getcwd()):
#     print(f" Root is: {root} have directories: {len(dirs)} and files: {len(files)}")
print(os.getcwd())
IMG_PATH = os.path.join(os.getcwd(), "train/images")
LABEL_PATH = os.path.join(os.getcwd(), "train/labels")

with open("train.csv", "w") as f:
    writer = csv.writer(f)
    for i in range(len(os.listdir(IMG_PATH))):
        img_name = os.listdir(IMG_PATH)[i]
        label_name = os.listdir(LABEL_PATH)[i]
        writer.writerow([img_name, label_name])

# data = pd.read_csv("test.csv")
# print(data.iloc[-1, 0])

