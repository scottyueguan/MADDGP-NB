#!/bin/sh


exp_name=maddpg_hvt_1v1_custome_agent
model_name=maddpg_hvt_1v1_custome_agent
original_model_name=maddpg_hvt_1v1
scenario=converge/simple_hvt_1v1_random
total_episodes=130000
save_rate=1000
episode_len=100
num_adversaries=1
pred_policy=maddpg
prey_policy=maddpg
save_dir=/Users/scottguan/CONVERGE/MADDGP-NB/MADDPG/data/$model_name/
load_dir=/Users/scottguan/CONVERGE/MADDGP-NB/MADDPG/data/$model_name/
plots_dir=/Users/scottguan/CONVERGE/MADDGP-NB/MADDPG/data/$model_name/plots/
customized_index=0
model_file=$model_name'_208000'

python ../experiments/train_customized_agent.py \
--exp-name $exp_name \
--scenario $scenario \
--good-policy $prey_policy \
--adv-policy $pred_policy \
--num-adversaries $num_adversaries \
--num-episodes $total_episodes \
--max-episode-len $episode_len \
--save-rate $save_rate \
--save-dir $save_dir \
--load-dir $load_dir \
--plots-dir $plots_dir \
--model-file $model_file \
--logging \
--restore \
--testing \
--display \
--customized-index $customized_index

echo Finished...
