import os
import yaml

_ROOT = os.path.dirname(os.path.abspath(__file__))
_CONFIGS_DIR = os.path.join(_ROOT, 'configs')


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def get_model_config(model_size='large'):
    path = os.path.join(_CONFIGS_DIR, f'model_{model_size}.yaml')
    return load_yaml(path)


def get_paths_config():
    path = os.path.join(_CONFIGS_DIR, 'paths.yaml')
    return load_yaml(path)


def get_model_path(model_size='large'):
    paths = get_paths_config()
    key = f'ddcolor_{model_size}'
    return paths['models'].get(key)
