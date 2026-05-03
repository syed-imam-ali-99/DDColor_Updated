CUDA_VISIBLE_DEVICES=2 \
python3 infer.py \
	--input /data/swarnim/DATA/swarnim/instance/val --output /data/swarnim/DDColor/results/instance \
	--model_path modelscope/damo/cv_ddcolor_image-colorization/pytorch_model.pt