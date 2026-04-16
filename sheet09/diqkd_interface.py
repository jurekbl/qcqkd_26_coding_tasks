import numpy as np
from typing import Tuple, Any
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error


# This exercise has the goal to guide you through a simulation of device independent abort criteria
# We include the add noise function from qiskit
# The running time of the noise simulation is bad, so we only test on 2 qubits with multiple shots
# Some interface is provided, fill out every TODO by following the docstring and replacing None or pass!
# Follow the protocol from the lecture notes, the name of the variables is this same.
# Do not rename the variables or change the data type of the output.
# No additional imports or packages are necessary.



def source_noisy_diqkd(p: float) -> Tuple[QuantumCircuit, NoiseModel]:
    """
    Initialize a 2-qubit Bell state |Phi+> with depolarizing noise.
    :param p: Depolarizing probability (0 <= p <= 1)
    :return: Tuple containing (QuantumCircuit, NoiseModel to be used in simulation)
    """
    # TODO
    # be careful which qubits are attacked in the noise model, double attacks result in a lower CHSH
    return None


def measure_noisy_diqkd(qc: QuantumCircuit, noise: NoiseModel, shots: int) -> Tuple[np.ndarray, np.ndarray, dict]:
    """
    Measures a quantumcircuit with noise in each basis combination. The quantumcircuit is initialized once
    per basis combination, each basis will be used once for 'shots' amount of shots and not picked randomly.
    Return the raw keys, i.e. the ordered measures in the computational basis (A0,B1),
    and a dict of counts of the measures in the other basis combinations.
    :param qc: noisy quantumcircuit.
    :param noise: noise model to be used in simulation.
    :return: Tuple containing Alice's and Bob's raw keys and
    a dict with keys (i,j) for chosen basis 0<i,j<=2 and values counts of measurement w.r.t that basis choice.
    """
    basis = np.array([(0, 1), (1, 1), (2, 1), (1, 2), (2, 2)])
    results_dict = {}
    simulator = AerSimulator()
    for basis_alice, basis_bob in basis:
        #TODO: apply the right gates to measure in the right basis

        #TODO: we need the ordered measures only in the computational basis:
        # to safe compiling time make sure memory is only on when measuring in that basis

        #TODO: measure the counts in the other basis and safe them in the dict
        pass
    return None


def compute_q_noisy_diqkd(alice_raw_key: np.ndarray, bob_raw_key: np.ndarray) -> float:
    """
    Simulates the computation of the amount of mismatching indices in a public channel.
    Takes both raw keys and computes the percent of mismatching indices at randomly chosen 50% of the entries.
    :param alice_raw_key: Alice's raw key.
    :param bob_raw_key: Bob's raw key.
    :return: amount of mismatching indices.
    """
    #TODO
    return None


def compute_s_noisy_diqkd(measures: dict) -> float:
    """
    Takes a dict of all measurements w.r.t. basis A1,A2,B1 and B2 and computes the amount of mismatches in
    the computational basis and the CHSH bound for w.r.t. to A1, A2, B1, B2.
    :param measures: dict of all measurements.
    :return: Tuple of form (mean of #mismatches/#qubits in computational basis, CHSH estimation).
    """
    #TODO
    return None


"""
----- TESTING --------
- with efficient implementation 1 million shots should compile in a few seconds
- you should see q is roughly p/2 and s goes from around 1.4 to around 2.8 when p goes from 0.5 to 0 

p = 0.1
qc, noise = source_noisy_diqkd(p)
a, b, dict = measure_noisy_diqkd(qc, noise, 1000000)
q = compute_q_noisy_diqkd(a,b)
s = compute_s_noisy_diqkd(dict)
print(q)
print(s)
"""