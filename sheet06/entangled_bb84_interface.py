import numpy as np
from typing import Tuple
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator


# This exercise has the goal to guide you through an implementation of the entangled BB84 protocol
# An attack and error correction is included
# We test the code in the end using the linear Hamming code, which can only correct one error
# Some interface is provided, fill out every TODO by following the docstring and replacing None or pass!
# Follow the protocol from the lecture notes, the name of the variables is this same.
# Do not rename the variables or change the data type of the output.
# No additional imports or packages are necessary.


def create_bell_pairs_entangled_bb84(n: int) -> QuantumCircuit:
    """
    Initialize 2n Bell pairs (|Psi+>^{⊗2n}) for Alice and Bob.
    Alice: qubits 0,...,2n-1, Bob: qubits 2n,...,4n-1.
    :param n: half of the number of qubits.
    :return: QuantumCircuit of bell pairs for Alice and Bob.
    """
    qc = QuantumCircuit(4*n)
    # TODO: init the right bell pairs
    return qc


def alice_send_entangled_bb84(qc: QuantumCircuit) -> Tuple[QuantumCircuit, np.ndarray]:
    """
    Alice selects a random 2n-bit string and applies H^{b_i} to her qubits (i.e. the first half
    of the qubits of the QuantumCircuit qc) where b_i = 1.
    :param qc: QuantumCircuit with 4n qubits (0,..,2n-1 for Alice, 2n,...,4n-1 for Bob).
    :return: Tuple containing the QuantumCircuit and b.
    """
    n = qc.num_qubits // 4
    b = np.random.randint(0, 2, 2 * n)
    # TODO: apply the gate accordingly
    return qc, b


def attack_entangled_bb84(qc: QuantumCircuit, t:int) -> QuantumCircuit:
    """
    Simulating an attack where t qubits in a QuantumCircuit get attacked randomly by applying either X or Z
    to one of Bob's qubits (i.e. the second half of the qubits in the QuantumCircuit qc).
    :param qc: QuantumCircuit to attack with 4n qubits (0,..,2n-1 for Alice, 2n,...,4n-1 for Bob).
    :param t: number of attacked qubits.
    :return: QuantumCircuit including t attacked qubits.
    """
    # TODO: apply X or Z randomly t times at Bobs qubits and print which qubits are attacked with which gate.
    return qc


def bob_apply_h_entangled_bb84(qc: QuantumCircuit, b:np.ndarray) -> QuantumCircuit:
    """
    Bob applies H^{b_i} to his qubits where b_i = 1.
    :param qc: QuantumCircuit with 4n qubits (0,..,2n-1 for Alice, 2n,...,4n-1 for Bob).
    :param b: Array where to apply H^{b_i} to qubits where b_i = 1, sent by Alice from alice_send_entangled_bb84.
    :return: Tuple containing the QuantumCircuit and b.
    """
    # TODO: apply the gate accordingly
    return qc


def select_n_elements(arr: np.ndarray, n:int) -> np.ndarray:
    """
    Select n elements randomly from a numpy array.
    :param arr: array to select from.
    :param n: number of elements to select.
    :return: array with n random elements.
    """
    # TODO
    return None


def measure_entangled_bb84(qc: QuantumCircuit) -> Tuple[np.ndarray,np.ndarray,np.ndarray]:
    """
    The measurement of Alice and Bob of their Bell states at n randomly selected indices after a potential attack.
    :param qc: The potentially attacked QuantumCircuit.
    :return: A tuple containing Alice's measurement, Bob's measurement and the indices of their random check bits.
    """
    # TODO: use select_n_elements and let Alice and Bob measure their qubits as these indices (their "check bits").
    #  Store the result in a classical register.
    #  Observe Alice's indices + 2 * n = Bob's indices
    # TODO: print a statement at which indices they measure.

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    counts = job.result().get_counts(qc)
    bitstring = list(counts.keys())[0]
    # ---- WATCH OUT THAT THE ORDER OF REGISTERS IS REVERSED -----
    bob_str, alice_str = bitstring.split() # if you initialize Bob's register first, switch to alice_str, bob_str = ...
    # ---- REVERSE ORDER OF BITSTRINGS AS WELL ----
    alice_bits = np.array([int(b) for b in alice_str[::-1]])
    bob_bits = np.array([int(b) for b in bob_str[::-1]])
    # TODO: Print a statement if their measurements differ and on how many indices.
    #  This way we simulate the abort, if they already differ at more indices than the code can correct -> abort.

    # TODO: replace none by the selected indices
    return alice_bits, bob_bits, None


def calculate_syndromes_entangled_bb84(qc: QuantumCircuit, H: np.array, check_bits: np.ndarray) \
        -> Tuple[np.ndarray, np.ndarray]:
    """
    Apply Steane stabilizers with respect to a matrix H to a QuantumCircuit and calculate the syndromes of Alice and Bob.
    :param check_bits: randomly selected indices to check.
    :param qc: The attacked Quantum Circuit.
    :param H: The parity check matrix of the used linear code for the protocol.
    :return: Tuple of the syndromes of Alice and Bob.
    """
    # TODO: initialize the indices for check bits for Alice and Bob
    #  Initialize an array for the indices where to apply stabilizers (the indices which are NOT part of the check bits)

    # TODO: initialize Ancillas for the the qubits where we apply the stabilizers.
    # TODO: initialize classical registers to measure the syndromes.
    #  It makes sense for testing to label the registers at this point.

    # ---- Z-type stabilizers ----
    # TODO: For the parity-check matrix H, entangle the corresponding data qubits with their respective ancillas to
    #  extract the Z-parity (bit-flip) information.
    # TODO: Measure the ancilla registers to project the data qubits into a stabilizer eigenstate.
    #  Store the resulting syndrome in the respective classical register.

    # --- X-type stabilizers ---
    # TODO: For the parity-check matrix H, entangle the corresponding data qubits with their respective ancillas to
    #  extract the X-parity (phase-flip) information.
    # TODO: Measure the ancilla registers to project the data qubits into a stabilizer eigenstate.
    #  Store the resulting syndrome in the respective classical register.

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    counts = job.result().get_counts(qc)
    bitstring = list(counts.keys())[0]
    register_values = bitstring.split()
    # TODO: read off the right syndromes from the register_values.
    #  ---- WATCH OUT that the order of the register names the reversed order of counts. ----
    s_a_string = None
    s_b_string = None
    # ---- REVERSE ORDER OF BITSTRINGS AS WELL ----
    s_a = np.array([int(b) for b in s_a_string[::-1]])
    s_b = np.array([int(b) for b in s_b_string[::-1]])
    return s_a, s_b


""" ---- NOTE: BRUTE-FORCE MINIMUM WEIGHT DECODING: ---
- Solving the equation He = s has non unique solutions. 
- The error e giving the correction is the minimum weight of these solutions.
- Finding the minimum weight solution is NP-Hard.
- For non-degenerate codes (like Hamming) every syndrome has a unique correction:
->  Alternatively implement a dictionary which syndrome gives which correction (also done by testing possible errors)

- Real-world decoders can handle Degeneracy. Here different error patterns are logically equivalent—
  by finding the most likely error class rather than just the shortest vector. 
  
- We use the brute force min weight calculation, it is arguably less tedious to code and works for small t. 
- The code here is provided.
"""


def solve_syndrome(H: np.array, s: np.ndarray) -> np.ndarray:
    """
    Brute forces the shortest error vector e such that He = s. Not feasible for large n.
    :param H: matrix H.
    :param s: vector s.
    :return: solution vector e.
    """
    num_stabilizers, num_qubits = H.shape
    if np.all(s == 0):
        return np.zeros(num_qubits, dtype=int)

    for i in range(num_qubits):
        if np.array_equal(H[:, i], s):
            e = np.zeros(num_qubits, dtype=int)
            e[i] = 1
            return e

    for i in range(num_qubits):
        for j in range(i + 1, num_qubits):
            if np.array_equal((H[:, i] ^ H[:, j]), s):
                e = np.zeros(num_qubits, dtype=int)
                e[i] = 1
                e[j] = 1
                return e

    return np.zeros(num_qubits, dtype=int)


def calculate_error_entangled_bb85(s_a: np.ndarray, s_b: np.ndarray, H: np.array) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate the error rates e according to He = s (mod 2).
    :param s_a: Alice's syndrome.
    :param s_b: Bob's syndrome.
    :param H: Parity matrix H.
    :return: A tuple [e_x, e_z], with e_x the first #rows(H) entries of e and e_z the second #rows(H) entries of e.
    """
    s = (s_a + s_b) % 2
    num_stab = len(H[0])
    s_x = s[:num_stab] # entries for X
    s_z = s[num_stab:] #entries for Z
    e_x = solve_syndrome(H, s_x)
    e_z = solve_syndrome(H, s_z)
    return e_x, e_z


def apply_corrections_entangled_bb84(qc: QuantumCircuit, e_x: np.ndarray, e_z:np.ndarray, check_bits: np.ndarray):
    """
    Applies corrections according to error rates.
    :param qc: QuantumCircuit
    :param e_x: error rate in X basis.
    :param e_z: error rate in Z basis.
    :param check_bits: bits Alice and Bob randomly selected to check.
    :return:
    """
    n = len(check_bits)
    # TODO: Bob applies the error corrections to his non-check bits.
    #  The binary vectors e_x and e_z tell where to apply X and Z.


    reg_alice = ClassicalRegister(n, 'key_alice')
    reg_bob = ClassicalRegister(n, 'key_bob')
    qc.add_register(reg_alice)
    qc.add_register(reg_bob)

    # TODO: measure the qubits of Alice and Bob at the non-check bits.


    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    counts = job.result().get_counts(qc)
    bitstring = list(counts.keys())[0]
    register_values = bitstring.split()
    alice_final = register_values[1] # initialized first, second entry in register_values
    bob_final = register_values[0] # initialized last, first entry in register_values
    print(f"Alice Key: {alice_final}")
    print(f"Bob Key:   {bob_final}")
    if alice_final == bob_final:
        print("SUCCESS: Correction was successful! Alice and Bob have the same key.")

"""
---- USE THE FOLLOWING CODE FOR TESTING WITH THE HAMMING CODE ----

qc = create_bell_pairs_entangled_bb84(7)
send = alice_send_entangled_bb84(qc)
qc = send[0]
b = send[1]
attacked = attack_entangled_bb84(qc, 1)
bob_qc = bob_apply_h_entangled_bb84(attacked, b)

a_bits, b_bits, selected_indices = measure_entangled_bb84(bob_qc)
print("Alice bits are:", a_bits)
print("Bobs bits are:", b_bits)

H = np.array([
    [1,1,1,0,1,0,0],
    [1,1,0,1,0,1,0],
    [1,0,1,1,0,0,1]
])

s_a, s_b = calculate_syndromes_entangled_bb84(qc, H, selected_indices)
print("Syndromes are",s_a, s_b)
s_x = s_a[:3]
s_z = s_a[3:]
e_x, e_z = calculate_error_entangled_bb85(s_a, s_b, H)
print("Error corrections are:", e_x, e_z)
apply_corrections_entangled_bb84(qc, e_x, e_z, selected_indices)

"""