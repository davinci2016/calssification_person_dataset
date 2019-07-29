import os, sys
import shutil

ROOTFS = '/home/davinci/dnn/data/my_person'
dirList = ['voc0712','coco2017', 'coco2014', 'imagenet2015det']
fileList = ['train.txt', 'val.txt']


outdir = '%s/combine' % ROOTFS
trainFilePath= '%s/train.txt' % outdir
valFilePath= '%s/val.txt' % outdir

if os.path.exists(outdir):
    #os.removedirs(outdir)
    shutil.rmtree(outdir)

os.makedirs(outdir)

f_train = open(trainFilePath, 'w')
f_val = open(valFilePath, 'w')

fileDict = {fileList[0]: f_train, fileList[1]: f_val}

for dir in dirList:
    for file in fileList:
        for line in open('%s/%s/%s' % (ROOTFS, dir, file)):
            fileDict[file].writelines(line)

f_train.close()
f_val.close()

