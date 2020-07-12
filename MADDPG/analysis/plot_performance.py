import matplotlib as mpl
import matplotlib.pyplot as plt
import pickle

level_0_agrewards = pickle.load(open("../level_k_performance_data/maddpg_hvt_1v1_agrewards.pkl", 'rb'))

level_1_defender_agrewards = pickle.load(open("../level_k_performance_data/maddpg_hvt_1v1_agrewards_level_1_defender.pkl","rb"))
level_1_attacker_agrewards = pickle.load(open("../level_k_performance_data/maddpg_hvt_1v1_agrewards_level_1_attacker.pkl","rb"))

level_2_defender_agrewards = pickle.load(open("../level_k_performance_data/maddpg_hvt_1v1_level_2_defender_agrewards.pkl","rb"))
level_2_attacker_agrewards = pickle.load(open("../level_k_performance_data/maddpg_hvt_1v1_level_2_attacker_agrewards.pkl","rb"))


level_0_attacker_rewards = level_0_agrewards[0::2]
level_0_defender_rewards = level_0_agrewards[1::2]
level_1_attacker_rewards = level_1_attacker_agrewards[0::2]
level_1_defender_rewards = level_1_defender_agrewards[1::2]
level_2_attacker_rewards = level_2_attacker_agrewards[0::2]
level_2_defender_rewards = level_2_defender_agrewards[1::2]

x_axis_label = '# of 1000 Episode Batches'
plt.subplot(121)
y_axis_label = 'Attacker Reward'
plt.plot(level_0_attacker_rewards, label="MADDPG")
plt.plot(level_1_attacker_rewards, label="Level-1 Attacker")
plt.plot(level_2_attacker_rewards, label="Level-2 Attacker")
plt.ylabel(y_axis_label)
plt.xlabel(x_axis_label)
plt.title("Attacker Rewards")
plt.legend()

plt.subplot(122)
y_axis_label = 'Defender Reward'
plt.plot(level_0_defender_rewards, label="MADDPG")
plt.plot(level_1_defender_rewards, label="Level-1 Defender")
plt.plot(level_2_defender_rewards, label="Level-2 Defender")
plt.ylabel(y_axis_label)
plt.xlabel(x_axis_label)
plt.title("Defender Rewards")
plt.legend()

plt.show()
