import matplotlib.pyplot as plt
import numpy as np

#create scatter plot
plt.scatter(df.x, df.y)

#add horizontal line at mean value of y
plt.axhline(y=np.nanmean(df.y), color='red', linestyle='--', linewidth=3, label='Avg')

#add vertcal line at median value of y
plt.axvline(x=np.nanmedian(df.y), color='red', linestyle='--', linewidth=3, label='Avg')


##matplotlib color
https://matplotlib.org/stable/gallery/color/named_colors.html
https://www.colordic.org/
