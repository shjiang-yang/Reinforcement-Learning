#!/usr/bin/env python
# coding: utf-8

from DQN import DQN_AGENT
import gym

env = gym.make('MountainCar-v0')


agent = DQN_AGENT(action_space_n=env.action_space.n,
                  action_space_dim=1,
                  observation_space_dim=env.observation_space.shape[0],
                  experience_pool_size=2000)

episode = 0
test_per_episode = 20
test_episodes = 10

step = 0

while True:
    # training
    obs = env.reset()
    done = False

    while not done:
        action = agent.get_action(obs)
        obs_, reward, done, info = env.step(action)

        reward = max(obs_[0] + 0.2, 0.0) * 10.0 + abs(obs_[1]) * 100.0 - 1.0

        ready = agent.add_experience(obs, action, reward, obs_, done)

        if ready and step % 20 == 0:
            agent.learning()

        obs = obs_
        step += 1

        print("agent status:  {}".format(agent.status_info))

    episode += 1

    # test
    if episode % test_per_episode == 0 and ready:
        total_reward = 0.0

        print("\n------------------ evaluating -----------------")
        for _ in range(test_episodes):
            observation = env.reset()
            done = False
            while not done:
                action = agent.get_action(observation, epsilon_greedy=False)
                env.render()
                observation_, reward, done, info = env.step(action)

                reward = max(obs_[0] + 0.2, 0.0) * 10.0 + abs(obs_[1]) * 100.0 - 1.0

                observation = observation_
                total_reward += reward

        agent.status_info["evaluation_scores"] = total_reward / test_episodes


env.close()
