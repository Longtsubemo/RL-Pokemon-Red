import gymnasium as gym
from stable_baselines3 import PPO
from environment import PokemonRedEnv

env = PokemonRedEnv("roms/Pokemon Red.gb")

model = PPO("MultiInputPolicy", env, verbose = 0)
model.learn(total_timesteps=25000)
model.save("ppo_red")

del model

model = PPO.load("ppo_red")

obs, info = env.reset()

while True:
    action, _states = model.predict(obs)
    obs, reward, terminated, truncated, info = env.step(action)