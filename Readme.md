# Pokémon Red RL 🕹️

**Training an AI agent to play Pokémon Red using Reinforcement Learning.**

This project explores building an autonomous Pokémon Red player using Reinforcement Learning (RL). The goal is to train an AI agent to understand its game environment, make decisions, and progressively learn how to navigate and play Pokémon Red.

The project uses **PyBoy** to emulate Pokémon Red, **Gymnasium** to create a custom RL environment, and **Proximal Policy Optimization (PPO)** to train the agent.

> 🚧 **Status: Early Development**
>
> The custom environment can retrieve game observations and execute agent actions. The next milestones involve improving observations, designing rewards, and integrating PPO training.

## 🎯 Project Goals

- Build a custom Gymnasium environment for Pokémon Red.
- Extract meaningful information from the game.
- Enable an AI agent to observe and interact with the game.
- Train an agent using PPO.
- Develop progressively more capable gameplay behavior.
- Experiment with reinforcement learning in a real game environment.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyBoy | Game Boy emulator |
| Gymnasium | Custom RL environment |
| Stable-Baselines3 | PPO implementation |
| PyTorch | Deep learning framework |
| NumPy | Observation and numerical processing |

## 🧠 How It Works

The project follows a standard reinforcement learning interaction loop:

1. **Observation:** The agent receives information about the current game state.
2. **Action:** The agent selects an action based on its policy.
3. **Environment:** The custom Gymnasium environment executes the action through PyBoy.
4. **Feedback:** The environment returns a new observation, reward, and episode status.
5. **Learning:** PPO uses collected experience to improve the agent's policy.

```text
       Pokémon Red ROM
              |
              v
        PyBoy Emulator
              |
              v
      Gymnasium Environment
              |
              v
        Game Observation
              |
              v
          PPO Agent
              |
              v
        Selected Action
              |
              v
      PyBoy Button Input
              |
              v
        Updated Game State
```

## 👁️ Current Observations

The environment currently retrieves three categories of information:

| Observation | Description |
|---|---|
| Collision Map | Identifies walkable and blocked areas |
| Game Area | Provides the visible game tile data |
| Player State | Tracks player coordinates, map ID, and facing direction |

The observation system is being developed to give the agent enough information to understand its surroundings and make meaningful decisions.

## 🎮 Current Action Space

The initial action space contains four directional actions:

- Up
- Down
- Left
- Right

These actions allow the agent to begin learning basic navigation.

## 🗺️ Development Roadmap

- [x] Set up PyBoy and load Pokémon Red.
- [x] Create a custom Gymnasium environment.
- [x] Retrieve collision information.
- [x] Retrieve visible game-area data.
- [x] Retrieve player position and facing direction.
- [x] Define an initial directional action space.
- [x] Execute actions through the environment.
- [x] Improve environment observations.
- [x] Design a meaningful reward function.
- [ ] Integrate Stable-Baselines3 PPO.
- [ ] Train the first navigation agent.
- [ ] Evaluate and improve agent performance.
- [ ] Expand toward more complex gameplay.

## 📁 Project Structure

```text
pokemon-red-rl/
│
├── roms/                 # Local ROM files (not committed)
│
├── environment.py        # Custom Gymnasium environment
├── observation.py        # Game observation extraction
├── gameinitial.py        # Game startup and continue logic
├── input.py              # Input helpers
├── playerinfo.py         # Player information and debugging
├── main.py               # Main entry point / experiments
├── test.py               # Environment testing
│
├── requirements.txt
└── README.md
```

*The structure may evolve as the project develops.*

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Longtsubemo/RL-Pokemon-Red.git
cd RL-Pokemon-Red
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the ROM

Place your legally obtained Pokémon Red ROM in:

```text
roms/Pokemon Red.gb
```

**Note:** ROM files are not included in this repository.

### 5. Run the environment

```bash
python environment.py
```

Refer to the project source as development continues, since the startup and training workflows are still evolving.

## 📚 References and Documentation

- [PyBoy Documentation](https://docs.pyboy.dk/)
- [Gymnasium Documentation](https://gymnasium.farama.org/)
- [Gymnasium Custom Environment Tutorial](https://gymnasium.farama.org/introduction/create_custom_env/)
- [Stable-Baselines3 Documentation](https://stable-baselines3.readthedocs.io/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [Pokémon Red Disassembly](https://github.com/pret/pokered)

## 🔬 Development Approach

This project is being developed incrementally.

Rather than attempting to train an agent to complete the entire game immediately, development starts with understanding the environment and learning basic navigation.

The intention is to build a reliable observation and action pipeline before introducing more complex reinforcement learning behavior.

## 👨‍💻 Author

**Longtsubemo Ngullie**

- [GitHub](https://github.com/Longtsubemo)
- [LinkedIn](https://www.linkedin.com/in/longtsubemo-ngullie-b722662a8)

---

*An experiment in teaching an AI to play Pokémon Red, one action at a time.*