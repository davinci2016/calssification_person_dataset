#!/usr/bin/env bash
VOC_PATH=/home/davinci/dnn/data/voc/VOCdevkit/VOC0712
TARGET_PATH=/home/davinci/dnn/data/my_person/voc0712
year="VOC0712"

mkdir $TARGET_PATH
mkdir $TARGET_PATH/Annotations/
mkdir $TARGET_PATH/JPEGImages/

cd $VOC_PATH/Annotations/
grep -H -R "<name>person</name>" > $TARGET_PATH/temp.txt

cd $TARGET_PATH

cat temp.txt | sort | uniq > $year.txt
find -name $year.txt | xargs perl -pi -e 's|.xml:\t\t<name>person</name>||g'
#cat $year.txt | xargs -i cp $VOC_PATH/Annotations/{}.xml $TARGET_PATH/Annotations/
#cat $year.txt | xargs -i cp $VOC_PATH/JPEGImages/{}.jpg $TARGET_PATH/JPEGImages/
#rm temp.txt
