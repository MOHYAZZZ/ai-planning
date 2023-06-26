; Like always lets start simple
(define (problem Problem1)
    (:domain expensive-transport)
    (:objects
        cargo1 cargo2 plane1 plane2 truck1 truck2 London New-york d1 d2 d3 d4 d5 d6 d7

    )

    (:init
        (= (total-cost) 0)
        (current_time d1)
        (day-to-day d1 d2)
        (day-to-day d2 d3)
        ; (day-to-day d3 d4)
        ; (day-to-day d4 d5)
        ; (day-to-day d5 d6)
        ; (day-to-day d6 d7)

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