# 学会调用Gym中的env
import gym
import random

env_name = 'CartPole-v0'
env = gym.make(env_name)
a_space = range(env.action_space.n)
num_episode = 20
max_render = 100


def test_env():
    for i_episode in range(num_episode):
        state = env.reset()
        for t in range(max_render):
            env.render()
            action = random.choice(a_space)
            state_, reward, done, info = env.step(action)
            print("{0}  |  {1}  |  {2}  |  {3}"
                  .format(state, action, reward, state_))
            if done:
                print("episode finished after {} timesteps".format(t+1))
                break
    env.close()


if __name__ == '__main__':
    test_env()
