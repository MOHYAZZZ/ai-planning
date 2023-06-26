from state import State
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


# ACTIONS
def load(current_state, cargo_name, plane) :
    if (current_state.get_vehicle_locations()[plane] == current_state.get_cargo_locations()[cargo_name]) and (
            plane in current_state.get_planes()) :
        new_state = copy.deepcopy(current_state)
        new_state.set_cargo_location(cargo_name, None)
        new_state.set_cargo_vehicle(cargo_name, plane)
        new_state.add_to_total_cost(LOAD)
        return new_state
    return None


def unload(current_state, cargo_name, plane) :
    cargo_vehicle = current_state.get_cargo_vehicles()[cargo_name]
    if (cargo_vehicle == plane) and (plane in current_state.get_planes()) :
        new_state = copy.deepcopy(current_state)
        cargo_location = new_state.get_vehicle_locations()[plane]
        new_state.set_cargo_location(cargo_name, cargo_location)
        new_state.set_cargo_vehicle(cargo_name, None)
        new_state.add_to_total_cost(UNLOAD)
        return new_state
    return None


def pick_up(current_state, cargo_name, truck) :
    if (current_state.get_vehicle_locations()[truck] == current_state.get_cargo_locations()[cargo_name]) and (
            truck in current_state.get_trucks()) :
        new_state = copy.deepcopy(current_state)
        new_state.set_cargo_location(cargo_name, None)
        new_state.set_cargo_vehicle(cargo_name, truck)
        new_state.add_to_total_cost(PICK_UP)
        return new_state
    return None


def drop_off(current_state, cargo_name, truck) :
    cargo_vehicle = current_state.get_cargo_vehicles()[cargo_name]
    if (cargo_vehicle == truck) and (truck in current_state.get_trucks()) :
        new_state = copy.deepcopy(current_state)
        cargo_location = new_state.get_vehicle_locations()[truck]
        new_state.set_cargo_location(cargo_name, cargo_location)
        new_state.set_cargo_vehicle(cargo_name, None)
        new_state.add_to_total_cost(DROP_OFF)
        return new_state
    return None


def fly(current_state, from_location, to_location, plane) :
    if from_location == to_location :
        return None

    plane_location = current_state.get_vehicle_locations()[plane]
    if (plane_location == from_location and plane in current_state.get_cargo_vehicles().values()) and (
            plane in current_state.get_planes()) :
        new_state = copy.deepcopy(current_state)
        new_state.set_vehicle_locations(plane, to_location)
        new_state.add_to_total_cost(FLY)
        new_state.decrement_days_available(FLY_DAYS)
        return new_state
    return None


def drive(current_state, from_location, to_location, truck) :
    if from_location == to_location :
        return None

    truck_location = current_state.get_vehicle_locations()[truck]
    if (truck_location == from_location and truck in current_state.get_cargo_vehicles().values()) and (
            truck in current_state.get_trucks()) :
        new_state = copy.deepcopy(current_state)
        new_state.set_vehicle_locations(truck, to_location)
        new_state.add_to_total_cost(DRIVE)
        new_state.decrement_days_available(DRIVE_DAYS)
        return new_state
    return None

# Perform action function
def perform_action(state, action) :
    new_state = None
    # Calls the appropriate action function based on the action type
    if action[0] == 'load' :
        new_state = load(state, action[1], action[2])

    elif action[0] == 'unload' :
        new_state = unload(state, action[1], action[2])

    elif action[0] == 'pick_up' :
        new_state = pick_up(state, action[1], action[2])

    elif action[0] == 'drop_off' :
        new_state = drop_off(state, action[1], action[2])

    elif action[0] == 'fly' :
        new_state = fly(state, action[2], action[3], action[1])
    else :
        new_state = drive(state, action[2], action[3], action[1])

    return new_state


# Finds all possible actions that are sensible.
def find_possible_actions(initial_state, goal_state) :
    actions = []

    # Generate load/pickUp actions
    for cargo, cargo_location in initial_state.get_cargo_locations().items() :
        for vehicle, vehicle_location in initial_state.get_vehicle_locations().items() :
            if cargo_location == vehicle_location and initial_state.get_cargo_vehicles()[cargo] is None :
                actions.append(("load", cargo, vehicle))
                actions.append(("pick_up", cargo, vehicle))

    # Generate fly/ drive actions
    for vehicle, vehicle_location in initial_state.get_vehicle_locations().items() :
        for destination in goal_state.get_cargo_locations().values() :
            if vehicle_location != destination :
                actions.append(("fly", vehicle, vehicle_location, destination))
                actions.append(
                    ("drive", vehicle, vehicle_location, destination))

    # Generate unload/ drop-off actions
    for cargo in initial_state.get_cargo_locations() :
        for vehicle in initial_state.get_vehicle_locations() :
            actions.append(("unload", cargo, vehicle))
            actions.append(("drop_off", cargo, vehicle))

    possible_actions = []
    # Filters actions based on vehicle type
    for action in actions :
        if action[0] == 'load' and 'plane' in action[2] :
            possible_actions.append(action)
        if action[0] == 'pick_up' and 'truck' in action[2] :
            possible_actions.append(action)
        if action[0] == 'unload' and 'plane' in action[2] :
            possible_actions.append(action)
        if action[0] == 'drop_off' and 'truck' in action[2] :
            possible_actions.append(action)
        if action[0] == 'fly' and 'plane' in action[1] :
            possible_actions.append(action)
        if action[0] == 'drive' and 'truck' in action[1] :
            possible_actions.append(action)

    return possible_actions

# Checks if an action is possible based on the current state
def is_action_possible(state, action) :
    # Returns False if there are no days available
    if state.get_days_available() <= 0 :
        return False
    
    # Checks conditions for each type of action
    if action[0] == 'load' :
        # Checks if the plane is already carrying cargo (planes and trucks can only carry one cargo at a time)
        if action[2] in state.get_cargo_vehicles().values():
            return False
        
        # Checks if the plane and cargo are at the same location and the plane is available
        if (state.get_cargo_vehicles()[action[1]] is not None) :
            return False

        if (state.get_vehicle_locations()[action[2]] == state.get_cargo_locations()[action[1]]) and (
                action[2] in state.get_planes()) :
            return True
        else :
            return False
    elif action[0] == 'unload' :
        if (state.get_cargo_vehicles()[action[1]] is None) :
            return False
        cargo_vehicle = state.get_cargo_vehicles()[action[1]]
        if (cargo_vehicle == action[2]) and (action[2] in state.get_planes()) :
            return True
        else :
            return False

    elif action[0] == 'pick_up' :
        if action[2] in state.get_cargo_vehicles().values():
            return False
        
        if (state.get_cargo_vehicles()[action[1]] is not None) :
            return False

        if (state.get_vehicle_locations()[action[2]] == state.get_cargo_locations()[action[1]]) and (
                action[2] in state.get_trucks()) :
            return True
        else :
            return False

    elif action[0] == 'drop_off' :
        if (state.get_cargo_vehicles()[action[1]] is None) :
            return False
        cargo_vehicle = state.get_cargo_vehicles()[action[1]]
        if (cargo_vehicle == action[2]) and (action[2] in state.get_trucks()) :
            return True
        else :
            return False
    elif action[0] == 'fly' :
        if state.get_days_available() < FLY_DAYS :
            return False
        if action[2] == action[3] :
            return False
        plane_location = state.get_vehicle_locations()[action[1]]
        if (plane_location == action[2] and action[1] in state.get_cargo_vehicles().values()) and (
                action[1] in state.get_planes()) :
            return True
        else :
            return False
    else :
        if state.get_days_available() < DRIVE_DAYS :
            return False
        if action[2] == action[3] :
            return False
        truck_location = state.get_vehicle_locations()[action[1]]
        if (truck_location == action[2] and action[1] in state.get_cargo_vehicles().values()) and (
                action[1] in state.get_trucks()) :
            return True
        else :
            return False

# Checks if an action is possible based on the current state and the state history
def is_action_based_on_state_possible(state, action) :
    condition = True

    if state.get_state_action_history() == [] :
        return is_action_possible(state, action)

    if is_action_possible(state, action) :

        for state_action in state.get_state_action_history() :
            if state_action[1] == action :
                return False

        # Checks if unload action is possible based on previous actions
        if (action[0] == 'unload') :
            for state_action in state.get_state_action_history() :
                previous_action = state_action[1]
                previous_state = state_action[0]
                if previous_action == action :
                    return False

                # You can't unload if you haven't flown
                if previous_action[0] == 'fly' and previous_action[1] == action[2] and \
                        previous_state.get_cargo_vehicles()[action[1]] == action[2] :
                    condition = True
                else :
                    condition = False

        # Checks if drop_off action is possible based on previous actions
        if (action[0] == 'drop_off') :
            for state_action in state.get_state_action_history() :
                previous_action = state_action[1]
                previous_state = state_action[0]
                if previous_action == action :
                    return False

                if previous_action[0] == 'drive' and previous_action[1] == action[2] and \
                        previous_state.get_cargo_vehicles()[action[1]] == action[2] :
                    condition = True
                else:
                    condition = False

        return condition
    return False

