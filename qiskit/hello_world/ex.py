import qiskit
from qiskit import IBMQ

IBMQ.save_account("dd92ca5806397511df80306103f356a84ee3bf737b5bc951c57a46b9d326db4bd5ff201fe9e375780c95b862d83969d9c96f528c0706d45f5b4a8026ee43fcf3")

IBMQ.load_account()


print( qiskit.__qiskit_version__ )
