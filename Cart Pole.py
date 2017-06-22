import gym

env = gym.make('CartPole-v0')
for i_episode in range(20):
    observarion = env.reset()
    for t in range(1000):
        env.render()
        print(observarion)
        action = env.action_space.sample()
        observarion, reward, done, info = env.step(action)
        if done:
            print("episode finished after {} timesteps")
            break
        
