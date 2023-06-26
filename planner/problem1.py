# Problem 1 of ALL-cost folder

from state import State

DAYS_AVAILABLE = 4

# INITIAL_STATE 
INITIAL_STATE_CARGO_LOCATIONS = {"cargo1" : "New-york", "cargo2" : "London"}
INITIAL_STATE = State(INITIAL_STATE_CARGO_LOCATIONS)
INITIAL_STATE.set_vehicle_locations("truck2", "London")
INITIAL_STATE.set_vehicle_locations("truck1", "New-york")
INITIAL_STATE.set_vehicle_locations("plane1", "New-york")
INITIAL_STATE.set_vehicle_locations("plane2", "London")
INITIAL_STATE.set_cargo_vehicle("cargo1", None)
INITIAL_STATE.set_cargo_vehicle("cargo2", None)
INITIAL_STATE.set_days_available(DAYS_AVAILABLE)
INITIAL_STATE.set_planes(["plane1", "plane2"])
INITIAL_STATE.set_trucks(["truck1", "truck2"])

# GOAL_STATE
GOAL_STATE_CARGO_LOCATIONS = {"cargo1" : "London", "cargo2" : "New-york"}
GOAL_STATE = State(GOAL_STATE_CARGO_LOCATIONS)