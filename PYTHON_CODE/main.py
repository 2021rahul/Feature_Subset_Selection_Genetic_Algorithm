#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:12:46 2017

@author: rahul
"""

import config
import quantum_diff_evol


def elitist_quantum_diff_evol():

    print("Initializing population")
    pop_qubits = quantum_diff_evol.pop_init()

    print("Observing population")
    pop_obs_qubits = quantum_diff_evol.pop_observe(pop_qubits)

    print("Calculating Initial Accuracy")
    qubits_accuracy, qubits_cross_val_score = quantum_diff_evol.pop_accuracy(pop_obs_qubits)

    for iter in range(0, config.EQDE_MAXITER):
        print("QDE iteration start")
        print("Iteration Number: ", iter)
        print("Calculating Original Accuracy")
        qubits_accuracy, qubits_cross_val_score = quantum_diff_evol.pop_accuracy(pop_obs_qubits)
        print("Mutating Population")
        pop_mut_qubits = quantum_diff_evol.pop_mutation(pop_qubits)
        print("Population crossover")
        pop_cross_qubits = quantum_diff_evol.pop_crossover(pop_qubits, pop_mut_qubits, qubits_accuracy)
        pop_obs_cross_qubits = quantum_diff_evol.pop_observe(pop_cross_qubits)
        print("Calculating Crossover Accuracy")
        cross_qubits_accuracy, cross_qubits_cross_val_score = quantum_diff_evol.pop_accuracy(pop_obs_cross_qubits)
        print("Population Selection")
        pop_qubits, pop_obs_qubits = quantum_diff_evol.pop_selection(pop_qubits, pop_obs_qubits, qubits_accuracy, pop_cross_qubits, pop_obs_cross_qubits, cross_qubits_accuracy)

    final_pop_qubits = pop_qubits
    final_pop_obs_qubits = pop_obs_qubits
    print("Calculating Final Accuracy")
    final_qubtis_accuracy, final_qubits_cross_val_score = quantum_diff_evol.pop_accuracy(final_pop_obs_qubits)
    quantum_diff_evol.print_output(final_pop_qubits, final_pop_obs_qubits, final_qubits_cross_val_score)

if __name__ == "__main__":
    elitist_quantum_diff_evol()
