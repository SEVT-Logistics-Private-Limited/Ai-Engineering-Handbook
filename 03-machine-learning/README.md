# 03 — Machine Learning

## Foundations
Machine learning methods use data to learn patterns or decision rules rather than relying only on manually written rules.

## Learning paradigms
- **Supervised learning:** examples include inputs and target labels.
- **Unsupervised learning:** discovers structure in data without target labels.
- **Self-supervised learning:** creates learning targets from the data itself.
- **Reinforcement learning:** an agent learns through actions, rewards and interaction.

## Core concepts
- Dataset, sample, feature, label and target
- Model, parameter, prediction and loss function
- Training, validation and test sets
- Regression, classification and clustering
- Overfitting, underfitting and generalization
- Regularization and data leakage
- Metrics: accuracy, precision, recall, F1, ROC-AUC, MAE and RMSE (choose based on task)
- Error analysis, baselines and reproducibility

## Typical supervised-learning workflow
Problem definition → data collection → cleaning and exploration → split data → train baseline → evaluate on validation data → tune → final test evaluation → deploy and monitor.

## Important caution
A high score on one metric does not automatically mean a model is useful. Select metrics based on the cost of different errors, class balance, deployment context and user needs.
