import time
from state import State
from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

from state_definitions import *

# set the number of problem you want to visualise
from problem1 import *

ACTIONS_COST_PREDICTION = {'load': FLY + UNLOAD, 'unload': 0, 'pick_up': DRIVE + DROP_OFF, 'drop_off': 0,
                           'fly': UNLOAD, 'drive': DROP_OFF}


def state_history_printer(state):
    step_number = 1
    path_edges = []  # Adds a list to store the path edges
    for i, state_action in enumerate(state.get_state_action_history()):
        print(f"{step_number}: {state_action[1]}")
        step_number += 1

        if i < len(state.get_state_action_history()) - 1:
            current_state = str(state_action[0])
            next_state = str(state.get_state_action_history()[i + 1][0])
            path_edges.append((current_state, next_state))  # Adds the edge to the list

    print("total cost: " + str(state.get_total_cost()))
    print("total days: " + str((DAYS_AVAILABLE - state.get_days_available()) + 1))

    return path_edges  # Returns the list of edges


def get_heuristic(state, action, goal_state):
    num_cargo_not_at_location = 0
    for cargo in state.get_cargo_locations():
        if state.get_cargo_locations()[cargo] != goal_state.get_cargo_locations()[cargo]:
            num_cargo_not_at_location += 1

    cost_prediction = ACTIONS_COST_PREDICTION[action[0]]

    return num_cargo_not_at_location * cost_prediction

def display_graph(G):
    plt.clf()
    # pos = nx.spring_layout(G, seed=42)
    pos = nx.kamada_kawai_layout(G) 

    node_colors = ['green' if str(node) == str(INITIAL_STATE) else 'grey' for node in G.nodes()]
    
    nx.draw(G, pos, node_color=node_colors, node_size=600)
    node_labels = {node: attrs['label'] + "\nH: " + str(attrs.get("h", "")) for node, attrs in G.nodes(data=True)}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)
    
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    plt.title("Cargo Transportation Plan A*")
    plt.axis('off')
    plt.draw()
    plt.waitforbuttonpress()


def main():
    pq = PriorityQueue()
    num_nodes_generated = 0
    pq.put((0, (INITIAL_STATE, None)))
    num_nodes_generated += 1

    G = nx.DiGraph()

    while not pq.empty():
        state, prev_action = pq.get()[1]

        # adds node to graph
        G.add_node(str(state), label=str(num_nodes_generated))

        # Calls display_graph to visualize the graph with the new node
        display_graph(G)

        possible_actions = find_possible_actions(state, GOAL_STATE)
        for action in possible_actions:
            if action == prev_action:
                continue

            if is_action_based_on_state_possible(state, action):
                new_state = perform_action(state, action)
                new_state.append_state_action_history((state, action))

                h = get_heuristic(new_state, action, GOAL_STATE)
                new_state.set_priority(h)

                # adds node to graph with heuristic value
                G.add_node(str(new_state), label=str(num_nodes_generated), h=h)

                # adds edge to graph
                G.add_edge(str(state), str(new_state), label=str(action[0]), color='grey', weight=1)

                # Calls display_graph to visualize the graph with the new edge
                display_graph(G)

                if new_state.goal_validator(GOAL_STATE):
                    print("Goal Reached!")

                    # Uses the modified state_history_printer function
                    path_edges = state_history_printer(new_state)

                    # Adds the goal node to the graph and connect it to the last node of the solution path
                    G.add_node(str(GOAL_STATE), label="Goal")
                    G.add_edge(str(new_state), str(GOAL_STATE), label="Done", color='red', weight=1)
                    path_edges.append((str(new_state), str(GOAL_STATE)))

                    # Visualises the final graph
                    display_graph(G)

                    return new_state

                pq.put((h, (new_state, action)))
                num_nodes_generated += 1

    print("No plan found")
                    
if __name__ == '__main__':
    main()
