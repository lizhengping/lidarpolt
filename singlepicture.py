
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import sys

sum=list(range(1024))
acc= np.asarray(sum).reshape([-32, 32]) if np.asarray(sum).ndim <= 1 else np.asarray(sum)

#print(type(acc[1]))
xNum=32
yNum=32
Noise=0
a=list(range(xNum*yNum))
b=[]

pixels_count = [[0 for x in range(0, xNum)] for y in range(0, yNum)]



def readData(filename):
    pixels = [[0 for x in range(0, xNum)] for y in range(0, yNum)]
    file = open(filename, 'r')
    a = file.readlines()
    #a.reverse()
    #for i in range(1024):
    #    a[i]=str(i)+','+str(i)+','+str(i)
    b = []
    for i in range(xNum*yNum):
        b.append(eval("[" + a[i] + "]"))
        #pixel[int(b[i][0] / xNum)][b[i][0] % yNum] = [x / 10000 for x in b[i][0:]]
        pixels[int(b[i][0] / xNum)][b[i][0] % yNum] =b[i]
        count = b[i][1] - Noise
        if count < 0:
            pixels_count[int(b[i][0] / xNum)][b[i][0] % yNum]  = 0
        else:
            pixels_count[int(b[i][0] / xNum)][b[i][0] % yNum]  = count

    for i in range(xNum):
        if i % 2 ==1:
            pixels[i].reverse()
    file.close()
    return pixels


def draw_heatmap(data,xlabels,ylabels):
    cmap = cm.Blues
    figure=plt.figure(figsize=(10,8),facecolor='w')
    ax=figure.add_subplot(1,1,1,position=[0.1,0.15,0.8,0.8])
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.98, top=0.98, wspace=None, hspace=None)
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    vmax=data[0][0]
    vmin=data[0][0]
    for i in data:
        for j in i:
            if j>vmax:
                vmax=j
            if j<vmin:
                vmin=j
    map=ax.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=vmin,vmax=vmax)
    cb=plt.colorbar(mappable=map,cax=None,ax=None,shrink=0.5)
    plt.show()


def plot_heatmap(pixel_Data):
    xlabels = ylabels = list(range(32))
    draw_heatmap(pixel_Data, xlabels, ylabels)
    plt.show()




if __name__ == '__main__' :

    if len(sys.argv) == 4:
        for i in range(1, len(sys.argv)):
            foldname = sys.argv[1]

    else:
        print('parameters error')
        filename = "pixelsTimes0.csv"


    readData(filename)
    plot_heatmap(pixels_count)