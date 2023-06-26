;; Simple problem but this time total cost is calculated.
(define (problem problem1)
    (:domain costly-transport)
    (:objects
        cargo1 cargo2 plane1 plane2 truck1 truck2 London New-york

    )

    (:init
        (= (total-cost) 0)
        (Cargo cargo1)
        (Cargo cargo2)
        (Plane plane1)
        (Plane plane2)
        (Truck truck1)
        (Truck truck2)
        (Location London)
        (Location New-york)
        (Airport London)
        (Airport New-york)

        (At cargo1 New-york)
        (At truck1 New-york)
        (At truck2 London)
        (At cargo2 London)
        (At plane1 New-york)
        (At plane2 London)

    )
    (:goal
        (and (At cargo1 London) (At cargo2 New-york))
    )
    (:metric minimize
        (total-cost)
    )
)