; This domain adds to the latest domain from all-cost and has the following characteristics:
; is for transporting cargo from location to location using planes and trucks.
; has a cost for every action
; Keeps track of time using static predicates 
; uses similar technique of time to keep track of capacity levels (code idea from IPC 2014 domain) 

(define(domain capacity-transport)

    (:requirements :action-costs :typing)

    (:predicates

        (in ?object ?location)
        (at ?object ?location)
        (location ?location)
        (cargo ?object)
        (plane ?object)
        (airport ?object)
        (truck ?object)
        (day-to-day ?day1 ?day2) ; day-to-day is a static predicate that keeps track of time for the actions fly and drive 
        (current_time ?day1) ; keeps track of the current time

        ; capcaity predicates
        ; the capacity of a vehicle in a hierarchical way
        ; each x represents a capacity level
        (capacity ?vehicle ?x1)
        ; indicates that one capacity level is a lower capacity than another
        (capacity-counter ?x1 ?x2)

    )

    (:functions
        ; function to keep track of costs
        (total-cost) - number
    )
    ; loads cargo to the plane.
    ; the action load has a cost of 2 units
    (:action load
        :parameters (?cargo ?plane ?airport ?x1 ?x2)
        :precondition (and (at ?cargo ?airport)
            (at ?plane ?airport)
            (cargo ?cargo)
            (plane ?plane)
            (airport ?airport)
            (capacity-counter ?x1 ?x2)
            (capacity ?plane ?x2)
        )
        :effect (and (not (at ?cargo ?airport))
            (in ?cargo ?plane)
            (capacity ?plane ?x1)
            (not (capacity ?plane ?x2))
            (increase (total-cost) 2))
    )
    ; unloads cargo from the plane to the airport
    ; the action unload has a cost of 2 units
    (:action unload
        :parameters (?cargo ?plane ?airport ?x1 ?x2)
        :precondition (and (in ?cargo ?plane)
            (at ?plane ?airport)
            (cargo ?cargo)
            (plane ?plane)
            (airport ?airport)
            (capacity-counter ?x1 ?x2)
            (capacity ?plane ?x1)
        )
        :effect (and (not (in ?cargo ?plane))
            (at ?cargo ?airport)
            (capacity ?plane ?x2)
            (not (capacity ?plane ?x1))
            (increase (total-cost) 2))
    )
    ; fly from ariport to another airport
    ; this action uses day-to-day predicate and populate it, in other words the action takes on day to complete.
    ; sets the current time has to be specifed in init state and one of the effects of fly action is to set the current time to next day.
    ; the action fly has a cost of 5 units  
    (:action fly
        :parameters (?plane ?from ?to ?day1 ?day2)
        :precondition (and
            (at ?plane ?from)
            (plane ?plane)
            (airport ?from)
            (airport ?to)
            (current_time ?day1)
            (day-to-day ?day1 ?day2)
        )
        :effect (and
            (not (at ?plane ?from))
            (at ?plane ?to)
            (increase (total-cost) 5)
            (not (current_time ?day1))
            (current_time ?day2)
        )
    )
    ; drive from location to location
    ; this action uses day-to-day and current-time just like fly action above
    ; the action drive has a cost of 3 units 
    (:action drive
        :parameters (?truck ?from ?to ?day1 ?day2)
        :precondition (and(at ?truck ?from)
            (truck ?truck)
            (location ?from)
            (location ?to)
            (current_time ?day1)
            (day-to-day ?day1 ?day2)
        )
        :effect (and
            (not (At ?truck ?from))
            (at ?truck ?to)
            (increase (total-cost) 3)
            (not (current_time ?day1))
            (current_time ?day2)
        )
    )
    ; pick-up cargo from a location and put on the truck 
    ; the action has a cost of 1 unit
    (:action pick-up
        :parameters (?cargo ?truck ?location ?x1 ?x2)
        :precondition (and (at ?cargo ?location)
            (at ?cargo ?location)
            (at ?truck ?location)
            (cargo ?cargo)
            (truck ?truck)
            (Location ?location)
            (capacity-counter ?x1 ?x2)
            (capacity ?truck ?x2)
        )
        :effect (and
            (not (at ?cargo ?location))
            (in ?cargo ?truck)
            (capacity ?truck ?x1)
            (not (capacity ?truck ?x2))
            (increase (total-cost) 1)
        )
    )
    ; drop cargo from the truck to the location
    ; the action has a cost of 1 unit
    (:action drop
        :parameters (?cargo ?truck ?location ?x1 ?x2)
        :precondition (and (in ?cargo ?truck)
            (at ?truck ?location)
            (cargo ?cargo)
            (truck ?truck)
            (location ?location)
            (capacity-counter ?x1 ?x2)
            (capacity ?truck ?x1)
        )
        :effect (and
            (not (in ?cargo ?truck))
            (at ?cargo ?location)
            (capacity ?truck ?x2)
            (not (capacity ?truck ?x1))
            (increase (total-cost) 1)
        )
    )
)