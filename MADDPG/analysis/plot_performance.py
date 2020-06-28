import matplotlib as mpl
import matplotlib.pyplot as plt
import pickle

rewards_maddpg = pickle.load(open("../data/maddpg_hvt_1v1/maddpg_hvt_1v1_rewards.pkl", 'rb'))
ag_rewards_maddpg = pickle.load(open("../data/maddpg_hvt_1v1/maddpg_hvt_1v1_agrewards.pkl", 'rb'))

rewards_fixed_attacker = pickle.load(open("../data/maddpg_hvt_1v1_custome_agent/maddpg_hvt_1v1_custome_agent_rewards.pkl", 'rb'))
ag_rewards_fixed_attacker = pickle.load(open("../data/maddpg_hvt_1v1_custome_agent/maddpg_hvt_1v1_custome_agent_agrewards.pkl", 'rb'))

attacker_rewards_maddpg = ag_rewards_maddpg[0::2]
defender_rewards_maddpg = ag_rewards_maddpg[1::2]
attacker_rewards_fixed_attacker = ag_rewards_fixed_attacker[0::2]
defender_rewards_fixed_attacker = ag_rewards_fixed_attacker[1::2]


y_axis_label = 'Attacker Reward'
x_axis_label = '# of 1000 Episode Batches'
plt.subplot(121)
plt.plot(attacker_rewards_maddpg, label="MADDPG")
plt.plot(attacker_rewards_fixed_attacker, label="Fixed Defender")
plt.ylabel(y_axis_label)
plt.xlabel(x_axis_label)
plt.title("Attacker Rewards")
plt.legend()

plt.subplot(122)
plt.plot(defender_rewards_maddpg, label="MADDPG")
plt.plot(defender_rewards_fixed_attacker, label="Fixed Defender")
plt.ylabel(y_axis_label)
plt.xlabel(x_axis_label)
plt.title("Defender Rewards")
plt.legend()

plt.show()