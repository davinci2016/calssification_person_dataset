#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/my_person
DATA=data/my_person
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/coco2017_train_lmdb \
  $DATA/coco2017_mean.binaryproto

echo "Done."
