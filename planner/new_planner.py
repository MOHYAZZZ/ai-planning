# My second approach to solve problems in python.
# Please check my a_star_planner.py

from state import State
import networkx as nx
import matplotlib.pyplot as plt
from my_queue import Queue
import copy


# ACTION COSTS
LOAD = 2
UNLOAD = 2
PICK_UP = 1
DROP_OFF = 1
FLY = 5
DRIVE = 3

# ACTION DAYS
FLY_DAYS = 1
DRIVE_DAYS = 2

DAYS_AVAILABLE = 4

# ACTIONS AVAILABLE IN DOMAIN

# Load action is to load cargo in the PLANE
def load(current_state, cargo_name, plane):
    if (current_state.get_vehicle_locations()[plane] == current_state.get_cargo_locations()[cargo_name]) and (plane in current_state.get_planes()):
        new_state = copy.deepcopy(current_state)
        new_state.set_cargo_location(cargo_name, None)
        new_state.set_cargo_vehicle(cargo_name, plane)
        new_state.add_to_total_cost(LOAD)
        return new_state
    return None

# Unload action is to unload cargo from the PLANE


def unload(current_state, cargo_name, plane):
    cargo_vehicle = current_state.get_cargo_vehicles()[cargo_name]
    if (cargo_vehicle == plane) and (plane in current_state.get_planes()):
        new_state = copy.deepcopy(current_state)
        cargo_location = new_state.get_vehicle_locations()[plane]
        new_state.set_cargo_location(cargo_name, cargo_location)
        new_state.set_cargo_vehicle(cargo_name, None)
        new_state.add_to_total_cost(UNLOAD)
        return new_state
    return None

# Pick up action is to load cargo on the TRUCK


def pick_up(current_state, cargo_name, truck):
    if (current_state.get_vehicle_locations()[truck] == current_state.get_cargo_locations()[cargo_name]) and (truck in current_state.get_trucks()):
        new_state = copy.deepcopy(current_state)
        new_state.set_cargo_location(cargo_name, None)
        new_state.set_cargo_vehicle(cargo_name, truck)
        new_state.add_to_total_cost(PICK_UP)
        return new_state
    return None

# Drop off action is to unload cargo from the TRUCK


def drop_off(current_state, cargo_name, truck):
    cargo_vehicle = current_state.get_cargo_vehicles()[cargo_name]
    if (cargo_vehicle == truck) and (truck in current_state.get_trucks()):
        new_state = copy.deepcopy(current_state)
        cargo_location = new_state.get_vehicle_locations()[truck]
        new_state.set_cargo_location(cargo_name, cargo_location)
        new_state.set_cargo_vehicle(cargo_name, None)
        new_state.add_to_total_cost(DROP_OFF)
        return new_state
    return None


def fly(current_state, from_location, to_location, plane):
    if from_location == to_location:
        return None

    plane_location = current_state.get_vehicle_locations()[plane]
    if (plane_location == from_location and plane in current_state.get_cargo_vehicles().values()) and (plane in current_state.get_planes()):
        new_state = copy.deepcopy(current_state)
        new_state.set_vehicle_locations(plane, to_location)
        new_state.add_to_total_cost(FLY)
        new_state.decrement_days_available(FLY_DAYS)
        return new_state
    return None


def drive(current_state, from_location, to_location, truck):
    if from_location == to_location:
        return None

    truck_location = current_state.get_vehicle_locations()[truck]
    if (truck_location == from_location and truck in current_state.get_cargo_vehicles().values()) and (truck in current_state.get_trucks()):
        new_state = copy.deepcopy(current_state)
        new_state.set_vehicle_locations(truck, to_location)
        new_state.add_to_total_cost(DRIVE)
        new_state.decrement_days_available(DRIVE_DAYS)
        return new_state
    return None


##################################################################################################################
######################################### SOLVE#####################################################################

def generate_all_actions_available(initial_state, goal_state):
    actions = []

    # Generate load/pickUp actions
    for cargo, cargo_location in initial_state.get_cargo_locations().items():
        for vehicle, vehicle_location in initial_state.get_vehicle_locations().items():
            if cargo_location == vehicle_location and initial_state.get_cargo_vehicles()[cargo] is None:
                actions.append(("load", cargo, vehicle))
                actions.append(("pick_up", cargo, vehicle))

    # Generate fly/ drive actions
    for vehicle, vehicle_location in initial_state.get_vehicle_locations().items():
        for destination in goal_state.get_cargo_locations().values():
            if vehicle_location != destination:
                actions.append(("fly", vehicle, vehicle_location, destination))
                actions.append(
                    ("drive", vehicle, vehicle_location, destination))

    # Generate unload/ drop-off actions
    for cargo in initial_state.get_cargo_locations():
        for vehicle in initial_state.get_vehicle_locations():
            actions.append(("unload", cargo, vehicle))
            actions.append(("drop_off", cargo, vehicle))

    return actions


def eliminate_impossible_actions(actions):
    possible_actions = []

    for action in actions:
        if action[0] == 'load' and 'plane' in action[2]:
            possible_actions.append(action)
        if action[0] == 'pick_up' and 'truck' in action[2]:
            possible_actions.append(action)
        if action[0] == 'unload' and 'plane' in action[2]:
            possible_actions.append(action)
        if action[0] == 'drop_off' and 'truck' in action[2]:
            possible_actions.append(action)
        if action[0] == 'fly' and 'plane' in action[1]:
            possible_actions.append(action)
        if action[0] == 'drive' and 'truck' in action[1]:
            possible_actions.append(action)

    return possible_actions


def is_action_possible(state, action):
    if state.get_days_available() < 1:
        return False

    if action[0] == 'load':

        if (state.get_cargo_vehicles()[action[1]] is not None):
            return False

        if (state.get_vehicle_locations()[action[2]] == state.get_cargo_locations()[action[1]]) and (action[2] in state.get_planes()):
            return True
        else:
            return False
    elif action[0] == 'unload':
        if (state.get_cargo_vehicles()[action[1]] is None):
            return False
        cargo_vehicle = state.get_cargo_vehicles()[action[1]]
        if (cargo_vehicle == action[2]) and (action[2] in state.get_planes()):
            return True
        else:
            return False

    elif action[0] == 'pick_up':
        if (state.get_cargo_vehicles()[action[1]] is not None):
            return False

        if (state.get_vehicle_locations()[action[2]] == state.get_cargo_locations()[action[1]]) and (action[2] in state.get_trucks()):
            return True
        else:
            return False

    elif action[0] == 'drop_off':
        if (state.get_cargo_vehicles()[action[1]] is None):
            return False
        cargo_vehicle = state.get_cargo_vehicles()[action[1]]
        if (cargo_vehicle == action[2]) and (action[2] in state.get_trucks()):
            return True
        else:
            return False
    elif action[0] == 'fly':
        if state.get_days_available() < FLY_DAYS:
            return False
        if action[2] == action[3]:
            return False
        plane_location = state.get_vehicle_locations()[action[1]]
        if (plane_location == action[2] and action[1] in state.get_cargo_vehicles().values()) and (action[1] in state.get_planes()):
            return True
        else:
            return False
    else:
        if state.get_days_available() < DRIVE_DAYS:
            return False
        if action[2] == action[3]:
            return False
        truck_location = state.get_vehicle_locations()[action[1]]
        if (truck_location == action[2] and action[1] in state.get_cargo_vehicles().values()) and (action[1] in state.get_trucks()):
            return True
        else:
            return False


initial_state_cargo_locations = {"cargo1": "New-york", "cargo2": "London"}
initial_state = State(initial_state_cargo_locations)
initial_state.set_vehicle_locations("truck2", "London")
initial_state.set_vehicle_locations("truck1", "New-york")
initial_state.set_vehicle_locations("plane1", "New-york")
initial_state.set_vehicle_locations("plane2", "London")
initial_state.set_cargo_vehicle("cargo1", None)
initial_state.set_cargo_vehicle("cargo2", None)
initial_state.set_days_available(DAYS_AVAILABLE)
initial_state.set_planes(["plane1", "plane2"])
initial_state.set_trucks(["truck1", "truck2"])


goal_state_cargo_locations = {"cargo1": "London", "cargo2": "New-york"}
goal_state = State(goal_state_cargo_locations)


# G = nx.DiGraph()

# G.add_node(initial_state)
# G.add_node(goal_state)


# create node for initial state here
# create node for goal state here


def is_action_based_on_state_possible(state, action):
    condition = True

    if state.get_state_action_history() == []:
        return is_action_possible(state, action)

    if is_action_possible(state, action):
        if (action[0] == 'unload'):
            for state_action in state.get_state_action_history():
                previous_action = state_action[1]
                previous_state = state_action[0]
                if previous_action == action:
                    return False

                # You can't unload if you haven't flown
                if previous_action[0] == 'fly' and previous_action[1] == action[2] and previous_state.get_cargo_vehicles()[action[1]] == action[2]:
                    condition = True
                else:
                    condition = False

        if (action[0] == 'drop_off'):
            for state_action in state.get_state_action_history():
                previous_action = state_action[1]
                previous_state = state_action[0]
                if previous_action == action:
                    return False

                if previous_action[0] == 'drive' and previous_action[1] == action[2] and previous_state.get_cargo_vehicles()[action[1]] == action[2]:
                    condition = True
                else:
                    condition = False

        return condition
    return False


def perform_action(state, action):
    new_state = None
    if action[0] == 'load':
        new_state = load(state, action[1], action[2])

    elif action[0] == 'unload':
        new_state = unload(state, action[1], action[2])

    elif action[0] == 'pick_up':
        new_state = pick_up(state, action[1], action[2])

    elif action[0] == 'drop_off':
        new_state = drop_off(state, action[1], action[2])

    elif action[0] == 'fly':
        new_state = fly(state, action[2], action[3], action[1])
    else:
        new_state = drive(state, action[2], action[3], action[1])

    return new_state


G = nx.DiGraph()

successful_states = []

def grapher_iterative(initial_state, goal_state):
    
    
    node_counter = 0
    queue = Queue()

    G.add_node(goal_state)

    queue.enqueue((initial_state, None))
    G.add_node(initial_state)

    while not queue.is_empty():
        state, previous_action = queue.dequeue()

        possible_actions = eliminate_impossible_actions(
            generate_all_actions_available(state, goal_state))
        for action in possible_actions:

            if action == previous_action:
                continue

            else:
                if is_action_based_on_state_possible(state, action):
                    new_state = perform_action(state, action)
                    # action failed
                    if new_state is None:
                        continue
                    else:
                        new_state.append_state_action_history((state, action))
                        if new_state.goal_validator(goal_state):
                            # We have reached goal state.
                            G.add_edge(state, goal_state, action=action)
                            print("action: " + str(action) + "\nstate: " +
                                  str(new_state.get_cargo_locations()))
                            successful_states.append(new_state)
                            print("goal reached\n\n\n\n\n")
                            continue

                        else:
                            queue.enqueue((new_state, action))
                            G.add_node(new_state)
                            node_counter += 1
                            G.add_edge(state, new_state, action=action)
                            print("action: " + str(action) + "\nstate: " +
                                  str(new_state.get_cargo_locations()))
                else:
                    continue

    print(node_counter)



grapher_iterative(initial_state, goal_state)

successful_state_number = 0
print(len(successful_states))
for state in successful_states:
    print("succesful state history number: " + str(successful_state_number) + "\n")
    for state_action in state.get_state_action_history():
        print(str(state_action[1]) + "\n")
    
    successful_state_number += 1


