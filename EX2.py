import matplotlib.pyplot as plt
data=[
[31,31,31,31,0,0,0,0,31,31,31],
[31,31,31,0,9,0,9,0,31,31,31],
[31,31,31,0,10,10,9,0,31,0,31],
[0,0,0,0,0,0,9,0,0,24,0],
[0,9,9,10,10,10,9,0,0,23,0],
[0,10,0,0,0,0,0,0,0,23,0],
[0,10,0,0,24,24,23,23,23,24,0],
[0,9,0,0,24,0,0,0,0,0,0],
[31,0,31,0,24,23,23,0,31,31,31],
[31,31,31,0,24,0,24,0,31,31,31],
[31,31,31,0,0,0,0,31,31,31,31],
]
plt.imshow(data, cmap="nipy_spectral")
