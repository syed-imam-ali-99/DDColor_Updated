#!/bin/bash
set -euo pipefail

MODEL_SIZE=${MODEL_SIZE:-large}
MODEL_PATH=${MODEL_PATH:-}
INPUT_SIZE=${INPUT_SIZE:-512}
GPU=${GPU:-0}

CMD="python3 gradio_app.py --model_size $MODEL_SIZE --input_size $INPUT_SIZE"
if [ -n "$MODEL_PATH" ]; then
    CMD="$CMD --model_path $MODEL_PATH"
fi

CUDA_VISIBLE_DEVICES=$GPU $CMD
