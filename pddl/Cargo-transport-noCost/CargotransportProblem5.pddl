;;The defualt solver cannot solve this problem due to "Suspected timeout."
;; I have invluded this to check other solvers like  https://www.fast-downward.org/ later on.

(define (problem problem4)
    (:domain cargo-transport)
    (:objects
        cargo1 cargo2 cargo3 cargo4 cargo5 truck1 truck2 truck3 truck4 plane1 plane2 plane3 plane4 Manchester Birmingham London New-york Liverpool Edinburgh Jersey-City
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
        (Location New-york)
        (Location Jersey-City)
        (At cargo1 Manchester) ;boths cargo 1 and 2 are at Manchester
        (At cargo2 Manchester)
        (At plane1 Manchester)
        (At cargo3 London)
        (At cargo4 Birmingham)
        (At plane2 London)
        (At plane3 Liverpool)
        (At truck1 Edinburgh)
        (At truck2 New-york)
        (At cargo5 Jersey-City)
        (At truck3 Jersey-City)

    )

    (:goal
        (and
            (At cargo1 Edinburgh) (At cargo2 London) (At cargo3 Liverpool) (At cargo4 Manchester) (At cargo5 New-york)
        )
    )

)