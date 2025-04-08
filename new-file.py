print("Hello World")



for i in range(5):
    m = i**i

    print(m)


import pandas as pd

dataframe_a = { 'A' : [1, 2, 3, 4, 5, 6, 7] , 'B' : [1, 2, 3, 4, 5, 6, 7], 'C' : [1, 2, 3, 4, 5, 6, 7], 'D' : [1, 2, 3, 4, 5, 6, 7] }


df = pd.DataFrame(dataframe_a)

print(df)