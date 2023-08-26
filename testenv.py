# import pymahjong
# pymahjong.test()

import pymahjong
import numpy as np

env = pymahjong.SingleAgentMahjongEnv(opponent_agent="random")  # the 3 opponents play randomly

obs = env.reset()  # get the obsevation at the first step of a game

print(env.env.oracle_observation_space.sample())
# while True:
#     valid_actions = env.get_valid_actions()  # e.g., [0, 3, 4, 20, 21]
#
#     a = np.random.choice(valid_actions)  # make decision among valid actions
#
#     obs, reward, done, _ = env.step(a)  # reward is zero unless the game is over (done = True).
#
#     print(f"{obs}\n{reward}\n{done}\n{_}")
#     # oracle_obs = env.get_oracle_obs()  # if you need oracle observation
#     # full_obs = env.get_full_obs()  # full_obs = concat((obs, oracle_obs), axis=0)
#
#     if done:
#         print("agent payoff = {}".format(reward))
#         break