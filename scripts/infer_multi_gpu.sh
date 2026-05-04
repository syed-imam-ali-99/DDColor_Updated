#!/bin/bash
set -euo pipefail

GPUS=${GPUS:-0,1,2}
MODEL_SIZE=${MODEL_SIZE:-large}
INPUT_SIZE=${INPUT_SIZE:-512}

python3 infer_multi_gpu.py --gpus "$GPUS" --model_size "$MODEL_SIZE" --input_size "$INPUT_SIZE"
