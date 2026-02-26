from typing import List
from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
import random


def random_bitstring(length: int) -> List[int]:
    """
    Generate a random binary string of length `length`.
    :param length: length of output
    :return: list of random bits of length `length`.
    """


def alice_qubit_b92(a: List[int]) -> QuantumCircuit:
    """
    Prepare Alice's qubits
    :param a: Alice's random bits
    :return: Alice's qubits according to B92
    """


def bob_measure_b92(qc: QuantumCircuit) -> List[List[int]]:
    """
    Prepare Bob's bits from Alice's qubits.
    :param qc: Alice's qubits
    :return: A list (of lists of bits), one Bob's random bits, one entry is b according to B92 measurement.
    """


def bit_discard_b92(a: List[int], a_prime: List[int], b: List[int]) -> List[List[int]]:
    """
    Discard all elements in Alice's and Bob's random bits according to B92.
    :param a: Alice's random bits
    :param a_prime: Bob's random bits
    :param b: Bob's measurement
    :return: reduced lists of Alice and Bob
    """
