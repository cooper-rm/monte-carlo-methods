# Lab 3: Monte Carlo Methods
## MSDS 684 — Reinforcement Learning
### Morgan Cooper

## Overview
This project implements first-visit Monte Carlo control with epsilon-greedy policies to train an RL agent to play Blackjack. The agent learns entirely from experience (model-free) using Gymnasium's Blackjack-v1 environment with Sutton & Barto rules.

## Repository Structure
```
├── lab3_monte_carlo.ipynb    # Main notebook with all implementation
├── generate_report.py        # LaTeX report generation script
├── Cooper_Morgan_Lab3.pdf    # Final report
├── figures/                  # Saved visualizations
│   ├── value_function_3d.png
│   ├── learned_policy.png
│   ├── learned_policy_1_5M.png
│   ├── basic_strategy.png
│   ├── basic_strategy_1_5M.png
│   ├── learning_curve.png
│   ├── epsilon_comparison_500k.png
│   ├── epsilon_comparison_1_5M.png
│   └── epsilon_comparison_all.png
└── context/                  # Lab materials (gitignored)
```

## Key Results
- Agent learns a near-optimal Blackjack policy after 500k episodes
- Policy closely matches basic Blackjack strategy; nearly perfect after 1.5M episodes
- Epsilon decay schedules outperform constant epsilon values
- Exponential decay achieves the best performance at 500k episodes
- Extended training shows diminishing returns — scheduling epsilon matters more than episode count

## How to Run
1. Install dependencies: `pip install gymnasium numpy matplotlib`
2. Run the notebook: `jupyter notebook lab3_monte_carlo.ipynb`
3. Generate the report: `python generate_report.py`

## References
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. Chapter 5.