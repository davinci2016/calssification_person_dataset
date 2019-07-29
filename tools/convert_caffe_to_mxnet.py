import os, sys
import shutil

DATA_ROOTFS = '/home/davinci/dnn/data'
PERSON_ROOTFS = '/home/davinci/dnn/data/my_person'
dirList = ['voc0712','coco2017', 'coco2014', 'imagenet2015det', 'combine']
fileList = ['train.txt', 'val.txt', 'test.txt']

outDirList = ['train', 'val', 'test']

for dir in dirList:
    outDir = '%s/mxnet/%s' % (PERSON_ROOTFS, dir)
    if os.path.exists(outDir):
        shutil.rmtree(outDir)
    os.makedirs(outDir)

    for file in fileList:
        subDir = '%s/%s' % (outDir, file.split('.')[0])
        os.makedirs(subDir)
        personSubDir = '%s/%d' % (subDir, 0)
        nonPersonSubDir = '%s/%d' % (subDir, 1)
        os.makedirs(personSubDir)
        os.makedirs(nonPersonSubDir)

        dst = ''
        class_idx = 0
        img_all_name=''
        img_name=''
        filename = os.path.join(PERSON_ROOTFS, dir, file)

        if os.path.exists(filename) == False:
            continue

        for line in open(filename):
            print line.split(' ')[0], int(line.split(' ')[1])
            img_all_name = '%s/%s' %(DATA_ROOTFS, line.split(' ')[0])
            img_name = img_all_name.split('/')[-1]
            class_idx = int(line.split(' ')[1])
            if class_idx == 0:
                dst = '%s/%s' % (personSubDir, img_name)
            else:
                dst = '%s/%s' % (nonPersonSubDir, img_name)
            print '%s -> %s' % (dst, img_all_name)
            os.symlink(img_all_name, dst)


