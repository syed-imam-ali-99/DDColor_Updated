#!/bin/bash
set -euo pipefail

MODEL_PATH=${MODEL_PATH:?Usage: MODEL_PATH=path/to/model.pt bash scripts/export_onnx.sh}
MODEL_SIZE=${MODEL_SIZE:-tiny}
INPUT_SIZE=${INPUT_SIZE:-512}
EXPORT_PATH=${EXPORT_PATH:-model.onnx}
OPSET=${OPSET:-12}

python3 export.py \
    --model_path "$MODEL_PATH" \
    --model_size "$MODEL_SIZE" \
    --input_size "$INPUT_SIZE" \
    --export_path "$EXPORT_PATH" \
    --opset "$OPSET"
