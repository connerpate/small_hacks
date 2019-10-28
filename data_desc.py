import pandas as pd

def data_desc(data):
    cols = data.columns
    desc = pd.DataFrame()
    for x in cols:
        if (data[x].dtype == 'float64') | (data[x].dtype == 'int64'):
            desc[x] = data[x].describe()
    print("Summary of Numerical Columns:")
    return desc

print("Imported!")
