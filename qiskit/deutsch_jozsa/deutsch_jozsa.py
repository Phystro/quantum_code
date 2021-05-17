#!/usr/bin/env python3

# Problem statement
# a function takes in as input a binary variable x. The function
# returns a binary number for each input value of x

# Case scenarios
# (0, 1) => (0, 0)  always zero # constant
# (0, 1) => (1, 1)  always one  # constant
# (1, 0) => (1, 0)  return x    # balanced
# (1, 0) => (0, 1)  flip x      # balanced

# Problem: how to figure out if function is constant or balanced
#
# Classically,
# you'd have to do 2 evaluations of your function to find
# out if it is constant or balanced
# You have to test out function with inputs of 0 and 1
#
# Quantum,
# implement function in a quantum circuit. All quantum gates are reversible,
# is the function f(x) reversible? NO. f(x) is by default non-reversible.
# 
# Oracle,
# takes an irreversible function turns it into sth reversible to implement on
# a quantum circuit.
# Oracles used in D-J algorithm and Grover's search algorithm.
# Oracles can be written as a matrix.
#
# Since f(x) is irreversible, we make a reversible version of it for our quantum algorithm.
# The reversible version is the Deutsch-Josza oracle U_f
#
# (x, y) => (x, y XOR f(x))
#
# Oracle is reversible:
# y XOR f(x) XOR f(x) = y
#
# We can use CNOT gate to create a XOR gate
# D-J
#   Initiate quantum circuit of two qubits x, y
#   apply X-gate to y
#   apply H-gates to both x and y, creating Superposition
#   apply oracle to x and y
#   apply H-gates to both x and y, creating Interference
#   Measure x. If result is 0, oracle is constant, if it is 1, oracle is balanced.
#
# for n-bit input , classical algorithms is O(2^n), for D-J, it's O(1)
# 
