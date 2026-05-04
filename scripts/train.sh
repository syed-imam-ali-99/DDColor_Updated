#!/bin/bash
set -euo pipefail

GPUS=${GPUS:-0,1,2,3}
NUM_GPUS=${NUM_GPUS:-4}
PORT=${PORT:-3721}
CONFIG=${CONFIG:-options/train/train_ddcolor.yml}

CUDA_VISIBLE_DEVICES=$GPUS \
python3 -m torch.distributed.launch \
    --nproc_per_node=$NUM_GPUS \
    --master_port=$PORT \
    basicsr/train.py \
    -opt $CONFIG \
    --auto_resume \
    --launcher pytorch
