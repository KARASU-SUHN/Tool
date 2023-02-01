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
#seaborn plot color
https://qiita.com/SaitoTsutomu/items/c79c9973a92e1e2c77a7
#seaborn boxplot
https://levelup.gitconnected.com/statistics-on-seaborn-plots-with-statannotations-2bfce0394c00

states_palette = sns.color_palette("Set3", n_colors=6)
# RdYlBu_r RdYlGn_r Set3
sns.set(rc={'figure.figsize':(10,7)})
sns.set_theme(style='whitegrid')
ax = sns.boxplot(
    x="year",
    y="Magnet", 
    data=domainM,
    hue="domain",
    showfliers=False,
    palette=states_palette
)
l = plt.legend(loc='upper left', borderaxespad=0)
plt.xticks(rotation=0)
