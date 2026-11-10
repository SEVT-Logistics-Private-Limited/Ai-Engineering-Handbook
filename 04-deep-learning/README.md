# 04 — Deep Learning

## Learning path
1. Scalars, vectors, matrices and tensors
2. Neurons, weights, biases and layers
3. Forward propagation
4. Activation functions
5. Loss functions
6. Gradients and the chain rule
7. Backpropagation
8. Gradient descent and optimizers (SGD, Adam and variants)
9. Learning rate, batch size, epochs and initialization
10. Regularization, dropout and normalization
11. Convolutional neural networks
12. Recurrent networks and sequence models
13. Attention and Transformers
14. Training stability, GPU computation and checkpointing

## Neural network training loop
Input batch → forward pass → prediction → loss calculation → backpropagation → optimizer update → repeat across batches and epochs.

During ordinary inference, the model performs the forward computation using learned parameters; it does not update those parameters.

## Practical labs
- Implement a single neuron with NumPy.
- Train a small classifier with PyTorch.
- Print tensor shapes at each layer.
- Plot training and validation loss.
- Compare optimizers on the same task.
- Save and reload a model checkpoint.
