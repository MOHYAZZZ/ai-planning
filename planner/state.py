import json

class State:
    def __init__(self, cargo_locations):
        self.cargo_locations = cargo_locations
        self.vehicle_locations = {}
        self.cargo_vehicles = {}
        self.total_cost = 0
        self.planes = []
        self.trucks = []
        self.days_available = None
        self.state_action_history = []
        self.priority = 0
        
    # Compares priorities of two states
    def __lt__(self, other):
        return self.priority < other.priority
    
    def get_cargo_locations(self):
        return self.cargo_locations
    
    def get_cargo_vehicles(self):
        return self.cargo_vehicles
    
    def get_vehicle_locations(self):
        return self.vehicle_locations   
    
    def get_days_available(self):
        return self.days_available
    
    def get_total_cost(self):
        return self.total_cost
    
    def get_planes(self):
        return self.planes
    
    def get_trucks(self):
        return self.trucks
    
    # Calculates the number of cargos not at their goal location
    def get_num_cargo_not_at_location(self, goal_state):
        goal_state_cargo_locations = goal_state.get_cargo_locations()
        num_not_at_location = 0
        for current_cargo_location_pair in self.cargo_locations.items():
            if current_cargo_location_pair not in goal_state_cargo_locations:
                num_not_at_location += 1
        
        return num_not_at_location
    
    def set_days_available(self, days):
        self.days_available = days
    
    def decrement_days_available(self, days):
        self.days_available -= days
        
    def set_cargo_location(self, cargo_name, new_cargo_location):
        self.cargo_locations[cargo_name] = new_cargo_location
        
    def set_vehicle_locations(self, vehicle_name, vehicle_location):
        self.vehicle_locations[vehicle_name] = vehicle_location
    
    def set_vehicle_locations_dict(self, vehicle_locations_dict):
        self.vehicle_locations = vehicle_locations_dict
        
    def set_cargo_vehicle(self, cargo_name, vehicle_name):
        self.cargo_vehicles[cargo_name] = vehicle_name
        
    def set_cargo_vehicle_dict(self, cargo_vehicles_dict):
        self.cargo_vehicles = cargo_vehicles_dict
        
    def add_to_total_cost(self, cost):
        self.total_cost += cost
    
    
    def set_total_cost(self, cost):
        self.total_cost = cost
    
    
    def set_planes(self, planes):
        self.planes = planes
    
    def set_trucks(self, trucks):
        self.trucks = trucks
        
    def get_state_action_history(self):
        return self.state_action_history
    
    def append_state_action_history(self, state):
        self.state_action_history.append(state)
    
    # Checks if the current state is a goal state
    def goal_validator(self, goal_state):
        for cargo, location in self.cargo_locations.items():
            if goal_state.get_cargo_locations()[cargo] != location:
                return False
        
        for vehicle in self.cargo_vehicles.values():
            if vehicle is not None:
                return False
        return True
    
    def get_priority(self):
        return self.priority
    
    def set_priority(self, priority):
        self.priority = priority
    
    def get_label(self):
        return str(self.get_cargo_locations())
    
    # Returns a string representation of the current state
    def __str__(self):
        return json.dumps({
            "cargo_locations": self.cargo_locations,
            "cargo_vehicles": self.cargo_vehicles,
            "vehicle_locations": self.vehicle_locations,
            "total_cost": self.total_cost,
            "days_available": self.days_available
        })