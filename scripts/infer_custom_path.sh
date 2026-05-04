#!/bin/bash
set -euo pipefail

export CUDA_VISIBLE_DEVICES=${GPU:-0}
MODEL_PATH=${MODEL_PATH:-}
MODEL_SIZE=${MODEL_SIZE:-large}
INPUT=${INPUT:-assets/test_images}
OUTPUT=${OUTPUT:-results}
INPUT_SIZE=${INPUT_SIZE:-512}

CMD="python3 infer.py --input $INPUT --output $OUTPUT --input_size $INPUT_SIZE --model_size $MODEL_SIZE"
if [ -n "$MODEL_PATH" ]; then
    CMD="$CMD --model_path $MODEL_PATH"
fi

$CMD
