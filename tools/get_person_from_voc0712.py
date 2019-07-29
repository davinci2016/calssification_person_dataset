import xml.etree.ElementTree as ET
import os, sys

#DATA_PATH = '/home/davinci/dnn/data/voc/VOCdevkit/VOC0712/JPEGImages'

VOC_PATH='/home/davinci/dnn/data/voc/VOCdevkit/VOC0712'
TARGET_PATH='/home/davinci/dnn/data/my_person/voc0712'
year="VOC0712"
dataPrefix = 'voc/VOCdevkit/VOC0712/JPEGImages'

origin_ann_dir = '%s/%s' % ( VOC_PATH, 'Annotations/')
new_ann_dir = 'Annotations/'

trainListFile = '/home/davinci/dnn/data/my_person/voc0712/train.txt'
valListFile = '/home/davinci/dnn/data/my_person/voc0712/val.txt'

#os.rename('Annotations/', origin_ann_dir)
#os.makedirs(new_ann_dir)

if (os.path.exists(trainListFile)):
    os.remove(trainListFile)

if (os.path.exists(valListFile)):
    os.remove(valListFile)

f_t = open(trainListFile, "a+")
f_v = open(valListFile, "a+")

k = 1
p = 1
np = 1
for dirpaths, dirnames, filenames in os.walk(origin_ann_dir):
    for filename in filenames:
        if os.path.isfile(r'%s%s' %(origin_ann_dir, filename)):
            origin_ann_path = os.path.join(r'%s%s' %(origin_ann_dir, filename))
            tree = ET.parse(origin_ann_path)
            root = tree.getroot()
            i = 0
            j = 0

            for object in root.findall('object'):
                name = str(object.find('name').text)
                if name != "person":
                    i += 1
                j += 1

            filename = tree.find('filename').text
            if i == j: #nonperson
                item = '%s/%s %d\n' % (dataPrefix, filename, 1)
                if (k%10 == 0):
                    f_v.write(item)
                else:
                    f_t.write(item)
                np += 1
            else: #person
                item = '%s/%s %d\n' % (dataPrefix, filename, 0)
                if (k%10 == 0):
                    f_v.write(item)
                else:
                    f_t.write(item)
                p += 1
            k += 1

print 'person:%d nonperson:%d ' % (p, np)

f_t.close()
f_v.close()