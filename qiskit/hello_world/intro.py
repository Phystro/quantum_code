from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, Aer, execute
import numpy as np


qasm_simulator = Aer.get_backend('qasm_simulator')
stat_simulator = Aer.get_backend('statevector_simulator')

q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.measure(q, c)

job = execute(qc, qasm_simulator)
result = job.result()
counts = result.get_counts(qc)
print(counts)

