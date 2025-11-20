import pandas as pd


def parse_data():
    df = 'dummy dataframe'

    ### read data
    fpath = 'Dataset.csv'
    df = pd.read_csv( fpath, sep=';' )
    
    
    ### process data
    df = df[  ['Y house price of unit area', 'X2 house age', 'X3 distance to the nearest MRT station', 'X5 latitude', 'X6 longitude']  ]
    df = df.rename( columns={'Y house price of unit area':'price', 'X2 house age':'age', 'X3 distance to the nearest MRT station':'mrt', 'X5 latitude':'latitude', 'X6 longitude':'longitude'} )

    return df