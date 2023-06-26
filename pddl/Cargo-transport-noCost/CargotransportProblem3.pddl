(define (problem problem3)
    (:domain cargo-transport)
    (:objects
        cargo1 cargo2 cargo3 cargo4 truck1 truck2 plane1 plane2 Manchester Birmingham London New-york

    )

    (:init

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
        ; (= (distance Birmingham Manchester) 10)
        ; (= (distance A C) 35)
    )
    (:goal
        (and (At cargo3 Manchester) (At cargo4 Birmingham) (At cargo1 London) (At cargo2 New-york))
    )
)