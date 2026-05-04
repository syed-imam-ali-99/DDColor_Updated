#!/bin/bash
set -euo pipefail

DATA_PATH=${1:?Usage: bash scripts/prepare_data.sh <data_path> <output_name>}
OUTPUT_NAME=${2:?Usage: bash scripts/prepare_data.sh <data_path> <output_name>}

python3 data_list/get_meta_file.py \
    --data-path "$DATA_PATH" \
    --output-name "$OUTPUT_NAME"
