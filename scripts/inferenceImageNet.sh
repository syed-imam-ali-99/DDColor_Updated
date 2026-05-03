CUDA_VISIBLE_DEVICES=0 \
python3 infer.py \
	--input /data/swarnim/DATA/swarnim/imagenet/val --output /data/swarnim/DDColor/results/imageNet \
	--model_path modelscope/damo/cv_ddcolor_image-colorization/pytorch_model.pt