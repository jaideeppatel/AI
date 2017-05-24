import sys
from copy import deepcopy

import numpy as np
import pandas as pd


class BayesNetwork:
    # nodes must be added in an order of parents being first
    def __init__(self):
        self._nodes = []

    def get_random_variables_list(self):
        random_vars_list = [n.get_node_name() for n in self._nodes]
        return random_vars_list.copy()

    def _get_node_reference(self, node_identifier):
        return [node for node in self._nodes if node.get_node_name() == node_identifier].pop()

    def _create_bayes_node(self, node_identifier):
        new_node = BayesNode(node_identifier)
        self._nodes.append(new_node)
        return new_node

    def add_node(self, node_identifier, distribution):
        if node_identifier not in self.get_random_variables_list():
            new_node = self._create_bayes_node(node_identifier)
            new_node.set_distribution(distribution)
        else:
            print("Node exists already.")
            exit(-1)

    def add_node_dependency(self, parent, child):

        if child not in self.get_random_variables_list():
            print("Node: '" + child + "' not found in the network. Add node '" + child + "' to the network first.")
            exit(-1)

        if parent not in self.get_random_variables_list():
            print("Node: '" + parent + "' not found in the network. Add node '" + parent + "' to the network first.")
            exit(-1)

        # Updating children list of the parent
        parent_node = self._get_node_reference(parent)
        if child not in parent_node.get_children():
            parent_node.add_child(child)

        # Updating parent list of child
        child_node = self._get_node_reference(child)
        if parent not in child_node.get_parents():
            child_node.add_parent(parent)

    def get_probability_distribution(self, node_identifier):
        node = self._get_node_reference(node_identifier)
        distribution = node.get_distribution()
        return deepcopy(distribution)

    def get_parents_list(self, node_identifier):
        node = self._get_node_reference(node_identifier)
        parents = node.get_parents()
        return parents.copy()

    def get_children_list(self, node_identifier):
        node = self._get_node_reference(node_identifier)
        children = node.get_children()
        return children.copy()

    def get_states(self, node_identifier):
        node = self._get_node_reference(node_identifier)
        states = node.get_states()
        return states


class BayesNode:
    def __init__(self, node_name, states=('t', 'f')):
        self._name = node_name
        self._parents = []
        self._children = []
        self._distribution = None
        self._states = states

    def get_node_name(self):
        return self._name

    def add_parent(self, parent_name):
        self._parents.append(parent_name)

    def get_parents(self):
        return deepcopy(self._parents)

    def add_child(self, child_name):
        self._children.append(child_name)

    def get_children(self):
        return deepcopy(self._children)

    def set_distribution(self, distribution):
        self._distribution = distribution

    def get_distribution(self):
        return deepcopy(self._distribution)

    def get_states(self):
        return self._states


def get_input():
    [num_of_evidence_inputs, num_of_query_inputs] = input().split()
    input_evidence_list = []
    input_query_list = []
    num_of_evidence_inputs = int(num_of_evidence_inputs)
    num_of_query_inputs = int(num_of_query_inputs)
    # Format of storage
    # Evidence
    # [('a', 'f'), ('b', 't')]
    # Query
    # ['j']

    while num_of_evidence_inputs > 0:
        input_evidence_list.append(tuple(input().strip().split()))
        num_of_evidence_inputs += -1
    while num_of_query_inputs > 0:
        input_query_list.append(input().strip())
        num_of_query_inputs += -1
    return input_evidence_list, input_query_list


def create_bayes_network():
    burglary = 'B'
    earthquake = 'E'
    alarm = 'A'
    john_calling = 'J'
    mary_calling = 'M'

    prior_burglary = pd.DataFrame({'t': 0.001, 'f': 0.999}, index=[1])
    prior_earthquake = pd.DataFrame({'t': 0.002, 'f': 0.998}, index=[1])
    posterior_alarm = pd.DataFrame({'B': ['t', 't', 'f', 'f'],
                                    'E': ['t', 'f', 't', 'f'],
                                    't': [0.95, 0.94, 0.29, 0.001],
                                    'f': [0.05, 0.06, 0.71, 0.999]
                                    })
    posterior_john_calling = pd.DataFrame({'A': ['t', 'f'],
                                           't': [0.90, 0.05],
                                           'f': [0.10, 0.95]
                                           })
    posterior_mary_calling = pd.DataFrame({'A': ['t', 'f'],
                                           't': [0.70, 0.01],
                                           'f': [0.30, 0.99]
                                           })

    network = BayesNetwork()

    network.add_node(burglary, prior_burglary)
    network.add_node(earthquake, prior_earthquake)
    network.add_node(alarm, posterior_alarm)
    network.add_node(john_calling, posterior_john_calling)
    network.add_node(mary_calling, posterior_mary_calling)

    network.add_node_dependency(burglary, alarm)
    network.add_node_dependency(earthquake, alarm)
    network.add_node_dependency(alarm, john_calling)
    network.add_node_dependency(alarm, mary_calling)

    return network


def normalize_distribution(distribution):
    if sum(distribution) == 0:
        print("Not enough samples found")
        return [0] * len(distribution)
    else:
        alpha = 1 / sum(distribution)
        return [d * alpha for d in distribution]


def get_probability(network, node_identifier, node_truth_value, evidence):
    """

    :param evidence:
    :param node_truth_value:
    :param node_identifier:
    :type network: BayesNetwork
    """
    parents = network.get_parents_list(node_identifier)
    distribution = network.get_probability_distribution(node_identifier)
    if len(parents) != 0:
        parent_observed_values = [e for e in evidence if e[0] in parents]
        temp_truth_table = []

        for i, (parent, observed_value) in enumerate(parent_observed_values):
            temp_truth_table.append(distribution[parent] == observed_value)

        truth_table = []
        for t in temp_truth_table:
            if not truth_table:
                for i in range(0, len(temp_truth_table[0])):
                    truth_table.append(t[i])
            else:
                for i in range(0, len(temp_truth_table[0])):
                    truth_table[i] = truth_table[i] and t[i]
        probability = distribution[truth_table][node_truth_value]

    else:
        probability = distribution[node_truth_value]

    index = probability.first_valid_index()
    return np.float(probability[index])


def enumerate_all(network, node_list, evidence):
    if len(node_list) == 0:
        return 1
    node = node_list[0]
    rest_nodes = node_list[1:]

    if node in [n[0] for n in evidence]:
        node_observed_value = [n[1] for n in evidence if n[0] == node].pop()
        probability = get_probability(network, node, node_observed_value, evidence)
        return probability * enumerate_all(network, rest_nodes, evidence)
    else:
        temp_sum = 0
        states = network.get_states(node)
        for state in states:
            new_evidence_list = deepcopy(evidence)
            new_evidence_list.append((node, state))
            temp_sum += get_probability(network, node, state, evidence) * enumerate_all(network, rest_nodes,
                                                                                        new_evidence_list)
        return temp_sum


def enumeration_ask(query, evidence, network):
    """

    :param evidence:
    :param query:
    :type network: BayesNetwork
    """
    node_list = network.get_random_variables_list()
    states = network.get_states(query)
    distribution = []

    for state in states:
        new_evidence_list = deepcopy(evidence)
        new_evidence_list.append((query, state))
        dist_state = enumerate_all(network, node_list, new_evidence_list)
        distribution.append(dist_state)
    return normalize_distribution(distribution)


def is_evidence_in_sample(evidence, sample):
    for e in evidence:
        if e not in sample:
            return False
    return True


def prior_sample(network):
    """

    :type network: BayesNetwork
    """
    node_list = network.get_random_variables_list()
    sample = []
    for n in node_list:
        truth_values = network.get_states(n)
        probability = [get_probability(network, n, s, sample) for s in truth_values]
        node_truth_value = np.random.choice(truth_values, p=probability)
        node_sample = (n, node_truth_value)
        sample.append(node_sample)

    return sample


def rejection_sample(query, evidence, network, num_of_samples):
    """

    :param query:
    :param evidence:
    :param num_of_samples:
    :type network: BayesNetwork
    """
    states = network.get_states(query)
    distribution = [0] * len(states)
    for i in range(num_of_samples):
        sample = prior_sample(network)
        if is_evidence_in_sample(evidence, sample):
            truth_value = [ev[1] for ev in sample if ev[0] == query].pop()
            distribution[states.index(truth_value)] += 1
    return normalize_distribution(distribution)


def weighted_sample(network, evidence):
    """

    :param evidence:
    :type network: BayesNetwork
    """
    weight = 1
    node_list = network.get_random_variables_list()
    sample = []
    for n in node_list:
        if n in [ev[0] for ev in evidence]:
            event = [ev for ev in evidence if ev[0] == n].pop()
            truth_value = event[1]
            sample.append(event)
            probability = get_probability(network, n, truth_value, sample)
            weight *= probability
        else:
            truth_values = network.get_states(n)
            probability = [get_probability(network, n, s, sample) for s in truth_values]
            node_truth_value = np.random.choice(truth_values, p=probability)
            node_sample = (n, node_truth_value)
            sample.append(node_sample)

    return sample, weight


def likelihood_weighting(query, evidence, network, num_of_samples):
    """

    :param query:
    :param evidence:
    :param num_of_samples:
    :type network: BayesNetwork
    """
    states = network.get_states(query)
    weighted_count_distribution = [0] * len(states)

    for i in range(num_of_samples):
        sample, weight = weighted_sample(network, evidence)
        truth_value = [ev[1] for ev in sample if ev[0] == query].pop()
        weighted_count_distribution[states.index(truth_value)] += weight
        pass

    return normalize_distribution(weighted_count_distribution)


def enumeration(query, evidence, network, num_of_samples=0):
    probability = enumeration_ask(query, evidence, network)
    print(query + " " + str(round(probability[0], 2)))


def prior_sampling(query, evidence, network, num_of_samples):
    """

    :param query:
    :param evidence:
    :param num_of_samples:
    :type network: BayesNetwork
    """
    valid_samples = []
    states = network.get_states(query)
    distribution = [0] * len(states)

    for i in range(num_of_samples):
        sample = prior_sample(network)
        if is_evidence_in_sample(evidence, sample):
            valid_samples.append(sample)
            query_truth_value = [ob[1] for ob in sample if ob[0] == query].pop()
            distribution[states.index(query_truth_value)] += 1

    probability = normalize_distribution(distribution)
    print(query + " " + str(round(probability[0], 2)))


def rejection_sampling(query, evidence, network, num_of_samples):
    """

    :param num_of_samples:
    :param query:
    :param evidence:
    :type network: BayesNetwork
    """
    distribution = rejection_sample(query, evidence, network, num_of_samples)
    print(query + " " + str(round(distribution[0], 2)))


def likelihood_sampling(query, evidence, network, num_of_samples):
    """

    :param query:
    :param num_of_samples:
    :param evidence:
    :type network: BayesNetwork
    """
    probability = likelihood_weighting(query, evidence, network, num_of_samples)
    print(query + " " + str(round(probability[0], 2)))


if __name__ == "__main__":

    if len(sys.argv) == 3:
        selected_method = sys.argv[1]
        num_samples = int(sys.argv[2])

        algorithm_dict = dict(e=enumeration, p=prior_sampling, r=rejection_sampling, l=likelihood_sampling)

        bayes_network = create_bayes_network()
        (evidence_list, query_list) = get_input()

        algorithm = algorithm_dict.get(selected_method)
        for q in query_list:
            algorithm(q, evidence_list, bayes_network, num_samples)

    else:
        print("Execute with valid arguments. \n\
        >> python assignment.py algorithm_char num_of_samples")
        exit(-1)
