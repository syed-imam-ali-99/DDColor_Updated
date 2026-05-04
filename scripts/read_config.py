import sys
import os
import yaml

config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'configs', 'paths.yaml')
with open(config_path) as f:
    config = yaml.safe_load(f)

keys = sys.argv[1].split('.')
val = config
for k in keys:
    val = val[k]
print(val)
