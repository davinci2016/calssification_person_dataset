import xml.etree.ElementTree as ET
import os, sys

TRAIN_DATA_PATH = 'ImageNet2015/ILSVRC2015/Data/DET/train'
VAL_DATA_PATH = 'ImageNet2015/ILSVRC2015/Data/DET/val'

IMGNET_TRAIN_PATH = '/home/davinci/dnn/data/ImageNet2015/ILSVRC2015/Annotations/DET/train'
IMGNET_VAL_PATH = '/home/davinci/dnn/data/ImageNet2015/ILSVRC2015/Annotations/DET/val'
TARGET_PATH = '/home/davinci/dnn/data/my_person/imagenet2015det'

trainListFile = '/home/davinci/dnn/data/my_person/imagenet2015det/train.txt'
valListFile = '/home/davinci/dnn/data/my_person/imagenet2015det/val.txt'

#os.rename('Annotations/', origin_ann_dir)
#os.makedirs(new_ann_dir)

if os.path.exists(trainListFile):
    os.remove(trainListFile)

if os.path.exists(valListFile):
    os.remove(valListFile)

f_t = open(trainListFile, "a+")
f_v = open(valListFile, "a+")


def scan_dir(dir, sub_dir, flags, data_dir):
    if not hasattr(scan_dir, 'npc'):
        scan_dir.npc = 0
    if not hasattr(scan_dir, 'np'):
        scan_dir.np = 1
    if not hasattr(scan_dir, 'p'):
        scan_dir.p = 1

    pdir = '%s/%s' % (dir, sub_dir)
    if sub_dir == []:
        pdir = '%s' % dir

    for dirpaths, dirnames, filenames in os.walk(pdir):
        for filename in filenames:
            scan_file = '%s/%s' % (dirpaths, filename)
            print scan_file
            if os.path.isfile(scan_file):
                origin_ann_path = os.path.join(scan_file)
                tree = ET.parse(origin_ann_path)
                root = tree.getroot()
                i = 0
                j = 0

                for object in root.findall('object'):
                    name = str(object.find('name').text)
                    if name != "n00007846":
                        i += 1
                    j += 1

                filename = tree.find('filename').text
                folder = tree.find('folder').text
                if i == j:  # nonperson
                    scan_dir.npc += 1
                    item = '%s/%s/%s.JPEG %d\n' % (data_dir, folder, filename, 1)
                    if pdir == dirpaths:
                        item = '%s/%s/%s.JPEG %d\n' % (data_dir, folder, filename, 1)
                    else:
                        item = '%s/%s/%s/%s.JPEG %d\n' % (data_dir, sub_dir, folder, filename, 1)

                    if scan_dir.npc%10 != 0:
                        continue

                    if flags == 0:
                        f_t.write(item)
                    else:
                        f_v.write(item)
                    scan_dir.np += 1
                else:  # person
                    item = '%s/%s/%s.JPEG %d\n' % (data_dir, folder, filename, 0)
                    if pdir == dirpaths:
                        item = '%s/%s/%s.JPEG %d\n' % (data_dir, folder, filename, 0)
                    else:
                        item = '%s/%s/%s/%s.JPEG %d\n' % (data_dir, sub_dir, folder, filename, 0)
                    if flags == 0:
                        f_t.write(item)
                    else:
                        f_v.write(item)
                    scan_dir.p += 1


def scan_val_dir(dir, flags, data_dir):
    if not hasattr(scan_val_dir, 'npc'):
        scan_val_dir.npc = 0
    if not hasattr(scan_val_dir, 'np'):
        scan_val_dir.np = 1
    if not hasattr(scan_val_dir, 'p'):
        scan_val_dir.p = 1

    for dirpaths, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            scan_file = '%s/%s' % (dirpaths, filename)
            print scan_file
            if os.path.isfile(scan_file):
                origin_ann_path = os.path.join(scan_file)
                tree = ET.parse(origin_ann_path)
                root = tree.getroot()
                i = 0
                j = 0

                for object in root.findall('object'):
                    name = str(object.find('name').text)
                    if name != "n00007846":
                        i += 1
                    j += 1

                filename = tree.find('filename').text
                folder = tree.find('folder').text
                if i == j:  # nonperson
                    scan_val_dir.npc += 1
                    item = '%s/%s.JPEG %d\n' % (data_dir, filename, 1)
                    if dir == dirpaths:
                        item = '%s/%s.JPEG %d\n' % (data_dir, filename, 1)
                    else:
                        item = '%s/%s/%s.JPEG %d\n' % (data_dir, sub_dir, filename, 1)

                    if scan_val_dir.npc%10 != 0:
                        continue

                    if flags == 0:
                        f_t.write(item)
                    else:
                        f_v.write(item)
                    scan_val_dir.np += 1
                else:  # person
                    item = '%s/%s.JPEG %d\n' % (data_dir, filename, 0)
                    if dir == dirpaths:
                        item = '%s/%s.JPEG %d\n' % (data_dir, filename, 0)
                    else:
                        item = '%s/%s/%s.JPEG %d\n' % (data_dir, sub_dir, filename, 0)
                    if flags == 0:
                        f_t.write(item)
                    else:
                        f_v.write(item)
                    scan_val_dir.p += 1


sub_all_dir = os.listdir(IMGNET_TRAIN_PATH)
for sub_dir in sub_all_dir:
    scan_dir(IMGNET_TRAIN_PATH, sub_dir, 0, TRAIN_DATA_PATH)

scan_val_dir(IMGNET_VAL_PATH, 1, VAL_DATA_PATH)

print 'train person:%d nonperson:%d ' % (scan_dir.p, scan_dir.np)
print 'val person:%d nonperson:%d ' % (scan_val_dir.p, scan_val_dir.np)

f_t.close()
f_v.close()