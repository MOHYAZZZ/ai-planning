# Problem 2 of All-cost folder

from state import State

DAYS_AVAILABLE = 7


# INITIAL_STATE 
INITIAL_STATE_CARGO_LOCATIONS = {"cargo1": "New-york", "cargo2": "London", "cargo3": "Birmingham", "cargo4": "Manchester"}
INITIAL_STATE = State(INITIAL_STATE_CARGO_LOCATIONS)
INITIAL_STATE.set_vehicle_locations("truck2", "Manchester")
INITIAL_STATE.set_vehicle_locations("truck1", "Birmingham")
INITIAL_STATE.set_vehicle_locations("plane1", "New-york")
INITIAL_STATE.set_vehicle_locations("plane2", "London")
INITIAL_STATE.set_cargo_vehicle("cargo1", None)
INITIAL_STATE.set_cargo_vehicle("cargo2", None)
INITIAL_STATE.set_cargo_vehicle("cargo3", None)
INITIAL_STATE.set_cargo_vehicle("cargo4", None)
INITIAL_STATE.set_days_available(DAYS_AVAILABLE)
INITIAL_STATE.set_planes(["plane1", "plane2"])
INITIAL_STATE.set_trucks(["truck1", "truck2"])


# GOAL_STATE
GOAL_STATE_CARGO_LOCATIONS = {"cargo1": "London", "cargo2": "New-york", "cargo3": "Manchester", "cargo4": "Birmingham"}
GOAL_STATE = State(GOAL_STATE_CARGO_LOCATIONS)