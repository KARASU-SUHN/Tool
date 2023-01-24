# Find difference between two data frames https://stackoverflow.com/questions/48647534/find-difference-between-two-data-frames
# find elements in df1 that are not in df2 df1>df2
df_1notin2 = df1[~(df1['Name'].isin(df2['Name']) & df1['Age'].isin(df2['Age']))].reset_index(drop=True)

## find same elements in diff df col
from functools import reduce
list(reduce(set.intersection, map(set, [df1.A, df2.A, df3.A])))

# Locating with characters  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.get_loc.html
df.set_index("col_1",inplace=True)
df.loc[['SearchContent']]

#Check if Exact String Exists in Column
(df['col'].eq('exact_string')).any()
#Check if Partial String Exists in Column
df['col'].str.contains('partial_string').any()


# read csv/txt data
data=pandas.read_csv(‘filename.txt’, sep=’ ‘, header=None, names=[“Column1”, “Column2”])
#if meet some error add:   ';' expected after '"'
(error_bad_lines=False)


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

cat <filepath> #command for open a file in linux

# resize figure
from PIL import Image
image = Image.open('path.jpeg')
new_image = image.resize((240, 320)) #resize
new_image.save('...jpeg')


#merge df by same column name
dfs = [df1, df2, df3, df4..]
c = pd.concat(dfs, join='outer', axis = 0) #0-index 1-column
# merge by different column
from functools import reduce
data_frames = [df1, df2, df3]
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['DATE'],
                                            how='outer'), data_frames)
# if you want to fill the values that don't exist in the lines of merged dataframe simply fill with required strings as
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['DATE'],
                                            how='outer'), data_frames).fillna('void')
#select several columns as a new df
df_new = df[['col1', 'col2']]

#check type of df
df.dtypes
#convert data type as int or other 
df['column name'] = df['column name'].astype(int)
#Extract data based on certain criteria by rows
df = df[df["column"] > 0]
#by columns
df = df[["col_1", "col_2"]]
#rename
df_new = df.rename(columns={'A': 'Col_1'}, index={'ONE': 'Row_1'})
#reset index
df.reset_index()



#contain some specfic symbol  #author=df.loc[df['unix'].str.contains('@')]
df.loc[df['E'].str.contains('oo')]


#Expand pandas dataframe from row-wise to column-wise
#https://stackoverflow.com/questions/68393230/compare-two-pandas-df-columns-with-string-values

## split dataframe
df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10,11], columns=['TEST'])
df_split = np.array_split(df, 3)
# ...you get 3 sub-dataframes:
df_split[0] # 1, 2, 3, 4
df_split[1] # 5, 6, 7, 8
df_split[2] # 9, 10, 11
# With split_dataframe:
df_split2 = split_dataframe(df, chunk_size=3)

#sort pandas dataframe from one column
sorted_df = df.sort_values(by=['Column_name'], ascending=True)


##matplotlib color
https://matplotlib.org/stable/gallery/color/named_colors.html
