import numpy as np
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# build a 3 qubit quantum register
qr = QuantumRegister(3)
# build a 3 bit classical register
cr = ClassicalRegister(3)
# quantum circuit
qc = QuantumCircuit(qr, cr)


# Applying H-gate to each qubit
for qubit in range(3):
    qc.h(qubit)

#qc.draw()
print(qc)

# Simulate output
# simulator = Aer.get_backend('qasm_simulator')
# result = execute(qc, backend=simulator, shots=1024).result()
# counts = result.get_counts()
# print(counts)
