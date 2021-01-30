import cirq

circuit = cirq.Circuit()

# define two qubits
( q0, q1 ) = cirq.LineQubit.range(2)

# perform quantum gates on the qubits
qlist = circuit.append( [cirq.H(q0), cirq.CNOT(q0, q1)] )

# measure the the circuit bits
clist = circuit.append( [cirq.measure(q0), cirq.measure(q1)] )

# perform simulation of the circuit
sim = cirq.Simulator()
results = sim.run(circuit, repetitions=10)

# print("quantum circuit: {}".format(qlist))
# print("classical circuit: {}".format(clist))

# draw circuit
print(circuit)
print(results)

