import matplotlib.pyplot as plt
import random 
from tkinter import *
r=Tk()
r.geometry("250x100")
r.title("matplotlib.pyplot Color Map finder")
cmap=['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
data1=[
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 ],
     [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 ],
     [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 ],
     [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 ],
     [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 ],
     
     
     
      ]

labelcmap=Label(r)
def randomcmap():
    randomx=random.randint(0,165)
    plt.imshow(data1, cmap=str(cmap[randomx]))
    plt.show(r)
    labelcmap["text"]=("You are using the " + str(cmap[randomx]) + " Color Map.")
cmapname=Button(r, text="Generate Color Map", command=randomcmap)
labelcmap.place(relx=0.05, rely=0.1)
cmapname.place(relx=0.15, rely=0.4)
r.mainloop()