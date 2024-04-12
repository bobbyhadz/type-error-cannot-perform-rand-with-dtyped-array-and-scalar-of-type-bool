# Cannot perform 'rand\_' with a dtyped [int64] array and scalar of type [bool]

import pandas as pd

df = pd.DataFrame({
    'A': ['Bobby', 'Bobby', 'Carl', 'Dan'],
    'B': [175.1, 180.2, 190.3, 205.4],
    'C': [10, 15, 20, 25],
})

#        A      B   C
# 1  Bobby  180.2  15
print(df.loc[(df.A == 'Bobby') & (df.C > 10)])