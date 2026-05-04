import os
import sys
import cv2
import signal
import argparse
import threading
from tqdm import tqdm

from infer import ImageColorizationPipeline
from config_utils import get_paths_config, get_model_path

stop_event = threading.Event()


def run_inference(colorizer, name, input_dir, output_dir, gpu_id, position):
    os.makedirs(output_dir, exist_ok=True)
    file_list = os.listdir(input_dir)

    pbar = tqdm(file_list, desc=f'{name} (GPU {gpu_id})', position=position, leave=True)
    for file_name in pbar:
        if stop_event.is_set():
            pbar.close()
            return
        img_path = os.path.join(input_dir, file_name)
        img = cv2.imread(img_path)
        if img is not None:
            image_out = colorizer.process(img)
            cv2.imwrite(os.path.join(output_dir, file_name), image_out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_size', type=str, default='large', choices=['large', 'tiny'])
    parser.add_argument('--model_path', type=str, default=None)
    parser.add_argument('--input_size', type=int, default=512)
    parser.add_argument('--gpus', type=str, default='0,1,2', help='Comma-separated GPU IDs for coco,imagenet,instance')
    args = parser.parse_args()

    model_path = args.model_path or get_model_path(args.model_size)
    gpu_ids = [int(g) for g in args.gpus.split(',')]
    paths = get_paths_config()

    datasets = [
        ('COCO', paths['data']['coco'], paths['output']['coco']),
        ('ImageNet', paths['data']['imagenet'], paths['output']['imagenet']),
        ('Instance', paths['data']['instance'], paths['output']['instance']),
    ]

    print('Loading models...')
    colorizers = []
    for i, (name, _, _) in enumerate(datasets):
        device = f'cuda:{gpu_ids[i]}'
        print(f'  {name} -> {device}')
        colorizer = ImageColorizationPipeline(
            model_path=model_path, input_size=args.input_size,
            model_size=args.model_size, device=device, verbose=False,
        )
        colorizers.append(colorizer)
    print('Starting inference...\n')

    def handle_sigint(sig, frame):
        print('\n' * (len(datasets) + 1) + 'Stopping all inference jobs...')
        stop_event.set()

    signal.signal(signal.SIGINT, handle_sigint)

    threads = []
    for i, (name, input_dir, output_dir) in enumerate(datasets):
        t = threading.Thread(
            target=run_inference,
            args=(colorizers[i], name, input_dir, output_dir, gpu_ids[i], i),
            daemon=True,
        )
        threads.append(t)
        t.start()

    for t in threads:
        while t.is_alive():
            t.join(timeout=0.5)

    if stop_event.is_set():
        print('All jobs stopped.')
        sys.exit(1)
    else:
        print('\n' * len(datasets) + 'All inference jobs complete.')


if __name__ == '__main__':
    main()
