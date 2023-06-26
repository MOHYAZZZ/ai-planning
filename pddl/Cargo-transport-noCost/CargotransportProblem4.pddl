(define (problem problem4)
    (:domain cargo-transport)
    (:objects
        cargo1 cargo2 cargo3 cargo4 cargo5 truck1 truck2 truck3 truck4 plane1 plane2 plane3 plane4 Manchester Birmingham London New-york Liverpool Edinburgh
    )

    (:init
        (Cargo cargo1)
        (Cargo cargo2)
        (Cargo cargo3)
        (Cargo cargo4)
        (Truck truck1)
        (Truck truck2)
        (Truck truck3)
        (Truck truck4)
        (Plane plane1)
        (Plane plane2)
        (Plane plane3)
        (Location Manchester)
        (Location Birmingham)
        (Location London)
        (Location Liverpool)
        (Location Edinburgh)
        (At cargo1 Manchester) ;boths cargo 1 and 2 are at Manchester
        (At cargo2 Manchester)
        (At plane1 Manchester)
        (At cargo3 London)
        (At cargo4 Birmingham)
        (At plane2 London)
        (At plane3 Liverpool)
        (At truck1 Edinburgh)

    )

    (:goal
        (and
            (At cargo1 Edinburgh) (At cargo2 London) (At cargo3 Liverpool) (At cargo4 Manchester)
        )
    )

)