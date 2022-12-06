# Find difference between two data frames https://stackoverflow.com/questions/48647534/find-difference-between-two-data-frames
# find elements in df1 that are not in df2
df_1notin2 = df1[~(df1['Name'].isin(df2['Name']) & df1['Age'].isin(df2['Age']))].reset_index(drop=True)


# Locating with characters  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.get_loc.html
df.set_index("col_1",inplace=True)
df.loc[['SearchContent']]


# read csv/txt data
data=pandas.read_csv(‘filename.txt’, sep=’ ‘, header=None, names=[“Column1”, “Column2”])


# Unzip .tar.gz in Linux  https://kinsta.com/knowledgebase/unzip-tar-gz/
#Extract .tar.gz file to current working directory:
tar -xf filename.tar.gz
# Extract .tar.gz file to current working directory and print output:
tar -xvf filename.tar.gz
# Extract .tar.gz file to a different working directory:
tar -xf filename.tar.gz -C /home/user/files
# Extract file1 and directory1 from .tar.gz file to current working directory:
tar -xf filename.tar.gz file1 directory1

#find projects with platform of NPM
npm = pwp[pwp['platform'].fillna(0).str.contains("NPM",na=False)] 

mv example1.txt example2.txt #rename file name in Linux
