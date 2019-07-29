from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import os, sys
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir='/home/davinci/dnn/data/coco2014'
dataType=[ 'train2014', 'val2014', 'test2014' ]
dataPrefix = 'coco2014'

outDir='/home/davinci/dnn/data/my_person/coco2014'
listFile = [  '/home/davinci/dnn/data/my_person/coco2014/train.txt',
              '/home/davinci/dnn/data/my_person/coco2014/val.txt',
              '/home/davinci/dnn/data/my_person/coco2014/test.txt' ]

for i in range(len(dataType)):
    print 'process data type %s' % dataType[i]
    annFile = '{}/annotations/instances_{}.json'.format(dataDir, dataType[i])
    if (dataType[i] == 'test2014'):
        annFile = '{}/annotations/image_info_{}.json'.format(dataDir, dataType[i])
    # initialize COCO api for instance annotations
    coco=COCO(annFile)

    # display COCO categories and supercategories
    cats = coco.loadCats(coco.getCatIds())
    nms=[cat['name'] for cat in cats]
    print('COCO categories: \n{}\n'.format(' '.join(nms)))

    nms = set([cat['supercategory'] for cat in cats])
    print('COCO supercategories: \n{}'.format(' '.join(nms)))

    # get all images containing given categories, select one at random
    allCatIds = coco.getCatIds();
    personCatIds = coco.getCatIds(catNms=['person']);
    allImgIds = coco.getImgIds();
    personImgIds = coco.getImgIds(catIds=personCatIds );
    nonPersonImgIds = list(set(allImgIds).difference(set(personImgIds)))

    #imgIds = coco.getImgIds(imgIds = [324158])
    #img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
    if(os.path.exists(listFile[i])):
        os.remove(listFile[i])
    f = open(listFile[i], "a+")

    print "Person Part %d " % len(personImgIds)
    for j in range(len(personImgIds)):
        #print j, personImgIds[j]
        img = coco.loadImgs(personImgIds[j])[0]
        #filename = '%s/images/%s/%s' % (dataDir, dataType, img['file_name'])
        item = '%s/%s/%s %d\n' % (dataPrefix, dataType[i], img['file_name'] , 0)
        f.write(item)
    #    I = io.imread('%s/images/%s/%s' % (dataDir, dataType, img['file_name']))
    #    io.imsave('%s/0/%s' % (outDir, img['file_name']), I)

    print "nonPerson Part %d " % len(nonPersonImgIds)
    for j in range(len(nonPersonImgIds)):
        #print i, nonPersonImgIds[j]
        img = coco.loadImgs(nonPersonImgIds[j])[0]
        #filename = '%s/images/%s/%s' % (dataDir, dataType, img['file_name'])
        item = '%s/%s/%s %d\n' % (dataPrefix, dataType[i], img['file_name'] , 1)
        f.write(item)
        #I = io.imread(filename)
        #io.imsave('%s/1/%s' % (outDir, img['file_name']), I)

    f.close()