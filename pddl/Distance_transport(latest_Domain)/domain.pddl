; The next version of the capacity domain 
; Currently does not work 
; will debug this after Modifying FD

(define (domain distance-transport)
    (:requirements :action-costs :typing)

    (:predicates
        (in ?object ?location)
        (at ?object ?location)
        (location ?location)
        (cargo ?object)
        (plane ?object)
        (airport ?object)
        (truck ?object)
        (day-to-day ?day1 ?day2)
        (current_time ?day1)
        (capacity ?vehicle ?x1)
        (capacity-counter ?x1 ?x2)
        (distance ?location1 ?location2 ?distance)
    )

    (:functions
        (total-cost) - number
    )

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

    (:action fly
        :parameters (?plane ?from ?to ?day1 ?day2 ?distance)
        :precondition (and
            (at ?plane ?from)
            (plane ?plane)
            (airport ?from)
            (airport ?to)
            (current_time ?day1)
            (day-to-day ?day1 ?day2)
            (distance ?from ?to ?distance)
            (> ?distance 100)
        )
        :effect (and
            (not (at ?plane ?from))
            (at ?plane ?to)
            (increase (total-cost) 5)
            (not (current_time ?day1))
            (current_time ?day2)
        )
    )

    (:action drive
        :parameters (?truck ?from ?to ?day1 ?day2 ?distance)
        :precondition (and
            (at ?truck ?from)
            (truck ?truck)
            (location ?from)
            (location ?to)
            (current_time ?day1)
            (day-to-day ?day1 ?day2)
            (distance ?from ?to ?distance)
            (<= ?distance 100)
        )
        :effect (and
            (not (at ?truck ?from))
            (at ?truck ?to)
            (increase (total-cost) 3)
            (not (current_time ?day1))
            (current_time ?day2)
        )
    )
)