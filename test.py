import gym

env = gym.make("CartPole-v1")

obs = env.reset()

while True:
    print("current observation:  {}".format(obs))
    a = int(input("input an action [0/1]:  "))
    env.render()
    obs_, r, done, info = env.step(a)
    
    if done:
        print("\n\nrestart!!")
        obs = env.reset()
    else:
        obs = obs_