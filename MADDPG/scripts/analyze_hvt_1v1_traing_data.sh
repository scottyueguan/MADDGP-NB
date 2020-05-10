#!/bin/bash

###########################################
#               Create plots              #
###########################################

DATA_PATH=/home/rolando/GitLab/CONVERGE/MADDPG_HVT_Data
MODEL=maddpg_hvt_1v1_21

# Call python script
python ../analysis/analyze_hvt_1v1_training_data.py \
--data-path "$DATA_PATH" \
--model $MODEL \
--num-episodes 200000
