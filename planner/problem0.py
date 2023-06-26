from state import State

DAYS_AVAILABLE = 10


# INITIAL_STATE Problem 0 of ALL-cost folder just for testing purposes does not solve anything important

INITIAL_STATE_CARGO_LOCATIONS = {"cargo1" : "New-york"}
INITIAL_STATE = State(INITIAL_STATE_CARGO_LOCATIONS)
INITIAL_STATE.set_vehicle_locations("truck1", "New-york")
INITIAL_STATE.set_vehicle_locations("plane1", "New-york")
INITIAL_STATE.set_cargo_vehicle("cargo1", None)
INITIAL_STATE.set_days_available(DAYS_AVAILABLE)
INITIAL_STATE.set_planes(["plane1"])
INITIAL_STATE.set_trucks(["truck1"])

# GOAL_STATE

GOAL_STATE_CARGO_LOCATIONS = {"cargo1" : "London"}
GOAL_STATE = State(GOAL_STATE_CARGO_LOCATIONS)