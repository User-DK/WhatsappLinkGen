import pandas as pd 
import numpy as np

df = pd.read_csv('Your_CSV_File.csv')

array = np.array(df)

row, col = array.shape

with open('instrumental.txt', 'w') as file:
    for i in range(row):
        for j in range(col):
            whatsapp_link = 'https://wa.me/91' + str(array[i][j])
            file.write(whatsapp_link + '\n')
