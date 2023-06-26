import time
from state import State
from queue import PriorityQueue
from state_definitions import *


# set the number of problem you want to solve
from problem2 import *


ACTIONS_COST_PREDICTION = {'load' : FLY + UNLOAD, 'unload' : 0, 'pick_up' : DRIVE + DROP_OFF, 'drop_off' : 0,
                           'fly' : UNLOAD, 'drive' : DROP_OFF}


# Function to print state history, total cost, and total days
def state_history_printer(state):
    step_number = 1
    for state_action in state.get_state_action_history() :
        print(str(step_number) + ": " + str(state_action[1]))
        step_number += 1
    print("total cost: " + str(state.get_total_cost()))
    print("total days: " + str((DAYS_AVAILABLE - state.get_days_available()) + 1))

# Heuristic function to estimate the remaining cost to reach the goal state
def get_heuristic(state, action, goal_state) :
    num_cargo_not_at_location = 0
    for cargo in state.get_cargo_locations() :
        if state.get_cargo_locations()[cargo] != goal_state.get_cargo_locations()[cargo] :
            num_cargo_not_at_location += 1

    cost_prediction = ACTIONS_COST_PREDICTION[action[0]]

    return num_cargo_not_at_location * cost_prediction

# Main function implementing the A* search algorithm
def main() :
    start_time = time.time()
    pq = PriorityQueue()
    num_nodes_generated = 0
    pq.put((0, (INITIAL_STATE, None)))
    num_nodes_generated += 1

    while not pq.empty() :
        state, prev_action = pq.get()[1]
        
        possible_actions = find_possible_actions(state, GOAL_STATE)
        for action in possible_actions :
            if action == prev_action :
                continue

            if is_action_based_on_state_possible(state, action) :
                new_state = perform_action(state, action)
                new_state.append_state_action_history((state, action))
                
                if new_state.goal_validator(GOAL_STATE) :
                    print("Goal Reached!")
                    print(state_history_printer(new_state))
                    print("Number of nodes generated: ", num_nodes_generated)
                    return new_state

                h = get_heuristic(new_state, action, GOAL_STATE)
                new_state.set_priority(h)

                pq.put((h, (new_state, action)))
                num_nodes_generated += 1
            
            printer = "Nodes Generated: " + str(num_nodes_generated) + "  " + "Time Elapsed: " +  str(time.time() - start_time)
            print(printer, end="\r")

                


    print("No plan found")
    print("Number of nodes generated: ", num_nodes_generated)


if __name__ == '__main__':
    main()

