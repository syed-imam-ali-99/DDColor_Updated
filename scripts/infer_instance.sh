#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

GPU=${GPU:-0}
INPUT=${INPUT:-$(python3 "$SCRIPT_DIR/read_config.py" data.instance)}
OUTPUT=${OUTPUT:-$(python3 "$SCRIPT_DIR/read_config.py" output.instance)}

GPU=$GPU INPUT=$INPUT OUTPUT=$OUTPUT bash "$SCRIPT_DIR/infer_custom_path.sh"
