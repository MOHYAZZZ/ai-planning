; slightly harder problem
(define (problem Problem2)
    (:domain expensive-transport)

    (:objects
        cargo1 cargo2 cargo3 cargo4 truck1 truck2 plane1 plane2 Manchester Birmingham London New-york d1 d2 d3 d4 d5 d6 d7
    )

    (:init
        (= (total-cost) 0)
        (current_time d1)
        (day-to-day d1 d2)
        (day-to-day d2 d3)
        (day-to-day d3 d4)
        (day-to-day d4 d5)
        ; (day-to-day d5 d6)
        ; (day-to-day d6 d7)
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
    (:metric minimize
        (total-cost)
    )
)