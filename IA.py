import torch
import torch.nn as nn
from torchsummary import summary

# Definir el modelo de red neuronal
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28*28, 128)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# Crear una instancia del modelo
modelo = NeuralNetwork()

# Imprimir la arquitectura del modelo de manera visual
summary(modelo, (1, 28, 28))
