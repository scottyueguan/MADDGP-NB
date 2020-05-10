#!/bin/sh

exp_name=maddpg_hvt_1v1
model_name=maddpg_hvt_1v1
scenario=converge/simple_hvt_1v1_random
total_episodes=200000
save_rate=1000
episode_len=50
num_adversaries=1
pred_policy=maddpg
prey_policy=maddpg
save_dir=/home/asher/Desktop/CONVERGE/data/$model_name/
load_dir=/home/asher/Desktop/CONVERGE/data/$model_name/
plots_dir=/home/asher/Desktop/CONVERGE/data/$model_name/

python ../experiments/train_hvt.py \
--exp-name $exp_name \
--scenario $scenario \
--done-callback \
--good-policy $prey_policy \
--adv-policy $pred_policy \
--num-adversaries $num_adversaries \
--num-episodes $total_episodes \
--max-episode-len $episode_len \
--save-dir $save_dir \
--plots-dir $plots_dir \
--log-loss

echo Finished...
