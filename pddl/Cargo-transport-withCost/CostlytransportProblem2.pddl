;; Another problem with costs a bit more complex than problem1
;; This is problem3 of transport-noCost
(define (problem problem2)
    (:domain costly-transport)
    (:objects
        cargo1 cargo2 cargo3 cargo4 truck1 truck2 plane1 plane2 Manchester Birmingham London New-york

    )

    (:init
        (= (total-cost) 0)
        (cargo cargo3)
        (Cargo cargo4)
        (Truck truck1)
        (Truck truck2)
        (Location Birmingham)
        (Location Manchester)
        (Cargo cargo1)
        (Cargo cargo2)
        (Plane plane1)
        (Plane plane2)
        (Airport London)
        (Airport New-york)

        (At cargo3 Birmingham)
        (At cargo4 Manchester)
        (At truck1 Birmingham)
        (At truck2 Manchester)

        (At cargo1 New-york)
        (At cargo2 London)
        (At plane1 New-york)
        (At plane2 London)
        
    )
    (:goal
        (and (At cargo3 Manchester) (At cargo4 Birmingham) (At cargo1 London) (At cargo2 New-york))
    )
)