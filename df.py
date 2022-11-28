# Find difference between two data frames https://stackoverflow.com/questions/48647534/find-difference-between-two-data-frames
# find elements in df1 that are not in df2
df_1notin2 = df1[~(df1['Name'].isin(df2['Name']) & df1['Age'].isin(df2['Age']))].reset_index(drop=True)


# Locating with characters  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.get_loc.html
df.set_index("col_1",inplace=True)
df.loc[['SearchContent']]


# read csv/txt data
data=pandas.read_csv(‘filename.txt’, sep=’ ‘, header=None, names=[“Column1”, “Column2”])
