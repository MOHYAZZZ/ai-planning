# Problem3 (problem.pddl) of All-cost folder

from state import State

DAYS_AVAILABLE = 10

# INITIAL_STATE 
INITIAL_STATE_CARGO_LOCATIONS = {"cargo1": "New-york", "cargo2": "LosAngeles", "cargo3": "London", "cargo4": "Paris", "cargo5": "Chicago"}
INITIAL_STATE = State(INITIAL_STATE_CARGO_LOCATIONS)
INITIAL_STATE.set_vehicle_locations("truck1", "New-york")
INITIAL_STATE.set_vehicle_locations("plane1", "New-york")
INITIAL_STATE.set_vehicle_locations("truck2", "LosAngeles")
INITIAL_STATE.set_vehicle_locations("plane2", "LosAngeles")
# INITIAL_STATE.set_vehicle_locations("truck3", "London")
INITIAL_STATE.set_vehicle_locations("plane3", "London")
INITIAL_STATE.set_vehicle_locations("truck4", "Paris")
# INITIAL_STATE.set_vehicle_locations("plane4", "Paris")
INITIAL_STATE.set_vehicle_locations("truck5", "Chicago")
# INITIAL_STATE.set_vehicle_locations("plane5", "Chicago")
INITIAL_STATE.set_cargo_vehicle("cargo1", None)
INITIAL_STATE.set_cargo_vehicle("cargo2", None)
INITIAL_STATE.set_cargo_vehicle("cargo3", None)
INITIAL_STATE.set_cargo_vehicle("cargo4", None)
INITIAL_STATE.set_cargo_vehicle("cargo5", None)
INITIAL_STATE.set_days_available(DAYS_AVAILABLE)
INITIAL_STATE.set_planes(["plane1", "plane2", "plane3", "plane4", "plane5"])
INITIAL_STATE.set_trucks(["truck1", "truck2", "truck3", "truck4", "truck5"])


# GOAL_STATE
GOAL_STATE_CARGO_LOCATIONS = {"cargo1": "Paris", "cargo2": "London", "cargo3": "Rome", "cargo4": "Madrid", "cargo5": "Houston"}
GOAL_STATE = State(GOAL_STATE_CARGO_LOCATIONS)