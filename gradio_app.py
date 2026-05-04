import argparse
import cv2
import numpy as np
import os
import torch
import torch.nn.functional as F

import gradio as gr
from gradio_imageslider import ImageSlider
import uuid
from PIL import Image

from infer import ImageColorizationPipeline
from config_utils import get_model_path

parser = argparse.ArgumentParser()
parser.add_argument('--model_path', type=str, default=None, help='Path to model weights (defaults to config)')
parser.add_argument('--model_size', type=str, default='large', choices=['large', 'tiny'])
parser.add_argument('--input_size', type=int, default=512)
args = parser.parse_args()

model_path = args.model_path or get_model_path(args.model_size)

colorizer = ImageColorizationPipeline(model_path=model_path,
                                      input_size=args.input_size,
                                      model_size=args.model_size)


# Create inference function for gradio app
def colorize(img):
  image_out = colorizer.process(img)
  # Generate a unique filename using UUID
  unique_imgfilename = str(uuid.uuid4()) + '.png'
  cv2.imwrite(unique_imgfilename, image_out)
  return (img, unique_imgfilename)


# Gradio demo using the Image-Slider custom component
with gr.Blocks() as demo:
  with gr.Row():
    with gr.Column():
      bw_image = gr.Image(label='Black and White Input Image')
      btn = gr.Button('Convert using DDColor')
    with gr.Column():
      col_image_slider = ImageSlider(position=0.5,
                                     label='Colored Image with Slider-view')

  btn.click(colorize, bw_image, col_image_slider)
demo.launch()