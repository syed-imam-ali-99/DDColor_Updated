CUDA_VISIBLE_DEVICES=3 \
python3 infer.py \
	--input /data/swarnim/DATA/swarnim/coco_bg --output /data/swarnim/DDColor/results/coco_bg \
	--model_path modelscope/damo/cv_ddcolor_image-colorization/pytorch_model.pt