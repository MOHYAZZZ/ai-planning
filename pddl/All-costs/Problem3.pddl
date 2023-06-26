(define (problem Problem3)
    (:domain expensive-transport)

    (:objects

        cargo1 cargo2 cargo3 cargo4 cargo5 cargo6 truck1 truck2 plane1 plane2 Manchester Birmingham London New-york d1 d2 d3 d4 d5 d6 d7

    )

    (:init
        (= (total-cost) 0)
        (current_time d1)
        (day-to-day d1 d2)
        (day-to-day d2 d3)
        (day-to-day d3 d4)
        (day-to-day d4 d5)
        (day-to-day d5 d6)
        (day-to-day d6 d7)
        (Cargo cargo1)
        (Cargo cargo2)
        (Cargo cargo3)
        (Cargo cargo4)
        (Cargo cargo5)
        (Cargo cargo6)
        (Truck truck1)
        (Truck truck2)
        (Plane plane1)
        (Plane plane2)
        (Location Manchester)
        (Location Birmingham)
        (Location London)
        (Location New-york)

        (At cargo1 London)
        (At cargo6 London)
        (At truck1 London)

        (At cargo2 Birmingham)
        (At truck2 Birmingham)

        (At cargo3 Manchester)
        (At plane1 Manchester)

        (At cargo4 New-york)
        (At cargo5 New-york)
        (At plane2 New-york)
    )
    (:goal
        (and
            (At cargo2 London)
            (At cargo1 Birmingham)
            (At cargo3 London)
            (At cargo4 Manchester)
            (At cargo6 Manchester)
            (At cargo5 London)

        )
    )
    (:metric minimize
        (total-cost)
    )
)