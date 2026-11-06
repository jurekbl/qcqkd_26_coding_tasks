import numpy as np
from typing import List, Dict, Tuple
import random
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator


# This exercise has the goal the guide you through an efficient implementation of a simulated key generation in E91
# Some interface is provided, fill out every TODO by replacing None, pass or []!
# Follow the protocol from exercise sheet 5, the name of the variables is this same.
# Do not rename the variables or change the data type of the output.
# No additional imports or packages are necessary.


def create_bell_circuit_e91() -> QuantumCircuit:
  r"""
  Creating a Bell state 1\sqrt{2}(|00>+|11>) in Qiskit
  :return: QuantumCircuit of the form 1\sqrt{2}(|00>+|11>)
  """
  qc = QuantumCircuit(2)
  # TODO: implement the right Bell state

  sv = Statevector(qc)
  print("Bell state " + sv.draw('latex_source') + " initialized")
  return qc


def generate_shots_e91(shots: int) -> List[Tuple[int, int, Dict[str,int]]]:
  """
  Utilizes the single bell state circuit of create_bell_circuit_e91 depending on the 9 different measurements,
  with shots number of shots. Returns an ordered list of the form
  [...[A_i, B_j, {"outcome1": number of outcome1, "outcome2": number of outcome2,...}, [...]]
  where 1<=i,j<=3 and A_i is Alice's and B_j is Bob's basis in the notation of Sheet 5.
  In the Dict each key "outcome" is a measurement outcome of Alice's and Bob's qubits and the
  value is the number of times this outcome occurred in repeated circuit runs ("shots").

  :param shots: number of shots

  :return: ordered list of 9 lists, each nested list has chosen bases in the first 2 entries and dict of the outcomes
  in the third.
  """
  results = []
  bell_qc = create_bell_circuit_e91()  # create Bell state once
  simulator = AerSimulator()  # simulator can also be created once
  for A in range(1, 4):
    for B in range(1, 4):
      # Make a new circuit with 2 qubits and 2 classical bits
      qc = QuantumCircuit(2, 2)
      qc.compose(bell_qc, qubits=[0, 1], inplace=True)
      qc.barrier()
      # TODO: replace each pass with the right Measurement rotations
      if A == 2: # A2 = X
        pass
      if A == 3:  # A3 = Z+X
        pass
      if B == 2: # B2 = Z-X
        pass
      if B == 3: # B3 = Z+X
        pass
      qc.measure(range(2), range(2))
      job = simulator.run(qc, shots=shots)
      counts = job.result().get_counts(qc)
      results.append([A, B, counts])
  return results


def generate_measurements_e91(counts: Dict[str, int]) -> List[int]:
  """
  Samples a single measurement outcome from a counts dictionary obtained from
  a quantum circuit simulation in the E91 protocol.
  Takes a Dict from one of the 9 lists of generate_shots_e91 of the form
  {"outcome1": number of outcome1, "outcome2": number of outcome2,...}.
  The function interprets these counts as a probability distribution
  and randomly samples one outcome according to the observed frequencies.
  Example: counts = {"00": 400, "11": 600}
    Here the total number of shots is 1000. The probabilities are therefore
        P(00) = 400 / 1000 = 0.4 & P(11) = 600 / 1000 = 0.6
    When this function is called, the outcome [0,0] is returned with
    probability 40%, and the outcome [1,1] with probability 60%.

  :param counts: A dictionary mapping measurement outcomes to their counts, as returned by
  Qiskit's `get_counts()`

  :return: A list [a, b] representing a single sampled measurement outcome, where
  a ∈ {0,1} is Alice's measurement result and b ∈ {0,1} is Bob's measurement result.
  """
  # TODO 1: Replace None to convert the keys of counts into a list of integer lists
  # Example: "01" -> [0,1]
  values = None
  total_counts = sum(counts.values())
  probabilities = [count / total_counts for count in counts.values()]
  # TODO 2: Replace [] to sample one outcome according to the probabilities
  bit = []
  return bit


def random_measurement_e91(results: List[Tuple[int, int, Dict[str,int]]]) -> list[int | list[int]]:
  """
  Simulates one E91 measurement round.
  Randomly selects bases A,B ∈ {1,2,3}, retrieves the corresponding counts
  from `results`, and samples a measurement outcome [a,b].

  :param results: List of list [A_i, B_j, {counts}] from the simulator.

  :return: [A, B, [a, b]] with the chosen bases and sampled outcome.
  """
  A = random.randint(1,3)
  B = random.randint(1,3)
  # TODO: fill in the line and replace None by the measurement counts for the chosen bases A, B
  # Hint: search `results` for the entry with matching A and B
  measurement_ab = None
  ab = generate_measurements_e91(measurement_ab)
  return [A,B, ab]


def random_measurement_list_e91(shots:int) -> list[list[int | list[int]]]:
  """
  Simulates multiple rounds of the E91 protocol.
  Randomly selects measurement bases for Alice and Bob each round,
  samples outcomes according to the simulated statistics, and collects the results.

  :param shots: Number of measurement rounds to simulate.

  :return: List of [A, B, [a, b]] for each round with chosen bases and sampled outcome.
  """
  bits = []
  # TODO 1: Replace None to generate the measurement statistics from the simulator
  results = None
  for _ in range(shots):
    # TODO 2: replace pass to perform the random measurement
    pass
  return bits


def key_generation_e91(bits: list[list[int | list[int]]]) -> Tuple[list[int], float]:
  """
  Generates the sifted key and estimates the CHSH parameter S from E91 measurement data.
  Processes a list of measurement rounds [A, B, [a, b]] from random_measurement_list_e91:
    - Sifts the key: keeps outcomes where Alice and Bob chose the same bases (A1,B1 or A3,B3).
    - Computes the CHSH correlation S using the other basis combinations.
    - Prints an error if the key of Alice and Bob do not match.

    :param bits: List of measurement rounds, each [A_basis, B_basis, [Alice_result, Bob_result]].
    :return: Tuple containing
             - key_alice: list of Alice's sifted key bits
             - s: estimated CHSH parameter from the selected rounds
  """
  key_alice, key_bob = [], []
  # TODO 1: Define the logic map for the CHSH calculation
  # (which basis pairs are positive or negative in the S sum)
  logic = None

  # TODO 2: Initialize sums and counters for the correlation calculation
  sums = None
  ctrs = None

  # TODO 3: Iterate over all measurement rounds and update sums/counters or sift keys
  for a_basis, b_basis, (a_res, b_res) in bits:
    pair = (a_basis, b_basis)
    # if pair in [(1,1),(3,3)] add results to key_alice and key_bob
    # else if pair in logic update sums[pair] and ctrs[pair] with (-1)^(a+b)
    pass

  # TODO 4: Compute the CHSH parameter S from sums and counters
  s = None
  if key_alice != key_bob:
    print("Error: Keys don't match!")
  else:
    print("Keys match: Key has been returned!")
  return key_alice, s
