import os
import shutil
import pandas as pd

# Read train.csv file
df = pd.read_csv('Dataset/train_data.csv')

# Create two folders to store images with 0 and 1 prediction
os.makedirs('Data/No Pnuemothorax', exist_ok=True)
os.makedirs('Data/Pnuemothorax', exist_ok=True)

# Iterate over each row of the dataframe and move the corresponding image to the corresponding folder
for index, row in df.iterrows():
    file_name = row['file_name']
    target = row['target']
    
    if target == 0:
        shutil.move(os.path.join('Dataset', file_name), os.path.join('No Pnuemothorax', file_name))
    elif target == 1:
        shutil.move(os.path.join('Dataset',file_name), os.path.join('Pnuemothorax', file_name))
