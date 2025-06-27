from qiskit.circuit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Crear circuito cuántico de 1 qubit y 1 bit clásico
circuito = QuantumCircuit(1, 1)
circuito.h(0)         # Compuerta Hadamard: pone en superposición
circuito.measure(0, 0)  # Medir qubit

# Mostrar el circuito en texto
print("Circuito cuántico:")
print(circuito.draw())

# Simular con Aer's Sampler
sampler = Sampler()
result = sampler.run(circuito, shots=1000).result()

# Contar resultados
counts = result.quasi_dists[0]
rounded_counts = {str(k): round(v * 1000) for k, v in counts.items()}  # Redondeamos a aproximado

# Mostrar resultados
print("Resultados de la medición:")
print(rounded_counts)
plot_histogram(rounded_counts)
plt.show()

