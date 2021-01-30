from qiskit import *
from qiskit.tools.visualization import *

# build 2 qubit quantum register
qr = QuantumRegister(2)

# build 2 classical bit classical register
cr = ClassicalRegister(2)

# build the quantum circuit
circuit = QuantumCircuit(qr, cr)

# drawing the circuit
# matplotlib inlines
# circuit.draw(output='mpl')


circuit.h(qr[0])
circuit.cx(qr[0], qr[1])
circuit.measure(qr, cr)

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend=simulator).result()

plot_histogram(result.get_counts(circuit))

circuit.draw(filename="my.txt")
