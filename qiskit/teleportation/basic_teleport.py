from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

qr = QuantumRegister(3)
cr = ClassicalRegister(3)

circ = QuantumCircuit(qr, cr)
circ.x(qr[0])
circ.barrier()

# create entanglemnt between q1 and q2
circ.h(qr[1])
circ.cx(qr[1], qr[2])

circ.barrier()
circ.cx(qr[0], qr[1])
circ.h(qr[0])

circ.barrier()
circ.measure([qr[0], qr[1]], [cr[0], cr[1]])

circ.barrier()
circ.cx(qr[1], qr[2])
circ.cz(qr[0], qr[2])

# simulate outcome
circ.barrier()
circ.measure(qr[2], cr[2])
sim = Aer.get_backend('qasm_simulator')
result = execute(circ, backend=sim, shots=1024).result()
counts = result.get_counts()
print(counts)

print(circ)
sim = Aer.get_backend('statevector_simulator')
result = execute(circ, backend=sim).result()
statevector = result.get_statevector()
print(statevector)
