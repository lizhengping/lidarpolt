import singlepicture  #直接全部引用了，注意
import os
import sys
import Tool
import time
from matplotlib import pyplot as plt
from matplotlib import cm


# definition
picture_fold='./photos/'
files=[]
Noise=0
xNum=32
yNum=32



def get_all_files(foldname):
    dst_path = picture_fold+foldname
    ext_name = 'csv'
    front_word='pixelsTime'

    for file in os.listdir(dst_path):
        if file.endswith(ext_name):
            if file.startswith(front_word):
                files.append(picture_fold+foldname+'/'+file)

    return files

def jigsaw(files):
    single_Pic = [[0 for x in range(0, xNum)] for y in range(0, yNum)]
    jTarget, iTarget = Tool.snakelike_list(xPicNum, yPicNum, step=xNum)
    print(jTarget,iTarget)
    for Num in range(len(iTarget)):
        i=iTarget[Num]
        j=jTarget[Num]

        print(files[Num])
        single_Pic=singlepicture.readData(files[Num])
        for iy in range(32):
            for jx in range(32):
                wholepicture_info[i+iy][j+jx]=single_Pic[iy][jx]
                count=single_Pic[iy][jx][1]-Noise
                if count<0:
                    all_pixel_count[i+iy][j+jx]=0
                else:
                    all_pixel_count[i+iy][j+jx]=count
    return wholepicture_info

def out_put_Data(data):
    path = picture_fold + foldname
    out_file = open(path+'/'+foldname+'WholePicture.csv', 'w')
    for i in range(len(data)):
        for j in range(len(data[i])):
          out_file.write(str(i)+','+str(j)+','+str(data[i][j][1:])[1:-1]+'\n')
    out_file.close()

def plot_heatmap(pixel_Data):

    xlabels=['' for i in range(xNum*xPicNum)]
    ylabels=['' for j in range(yNum*yPicNum)]

    for i in range(xPicNum):
        xlabels[i * xNum] = i
    for j in range(yPicNum):
        ylabels[j * yNum] = j

    singlepicture.draw_heatmap(pixel_Data, xlabels, ylabels)
    plt.show(block=False)
    time.sleep(3)
    exit(0)

#readData(filename=)
#pixel

if __name__ == '__main__' :

    if len(sys.argv)==4:
        for i in range(1, len(sys.argv)):
            foldname=sys.argv[1]
            xPicNum=sys.argv[2]
            yPicNum=sys.argv[3]
    else:
        print('parameters error')
        foldname = '2017'
        xPicNum = 3
        yPicNum = 3


    wholepicture_info = [[0 for x in range(0, xNum * xPicNum)] for y in range(0, yNum * yPicNum)]
    all_pixel_count = [[0 for x in range(0, xNum * xPicNum)] for y in range(0, yNum * yPicNum)]

    jigsaw(get_all_files(foldname))
    #plot_heatmap(all_pixel_count)
    out_put_Data(wholepicture_info)

