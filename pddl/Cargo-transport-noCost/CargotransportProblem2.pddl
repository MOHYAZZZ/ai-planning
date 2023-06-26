;;Simple and basic problem.
;;This problem will get harder as the term goes by and get a better understanding of PDDL.
(define (problem problem2)
    (:domain cargo-transport)
    (:objects
        cargo3 cargo4 truck1 truck2 Manchester Birmingham

    )

    (:init

        (cargo cargo3)
        (Cargo cargo4)
        (Truck truck1)
        (Truck truck2)
        (Location Birmingham)
        (Location Manchester)

        (At cargo3 Birmingham)
        (At cargo4 Manchester)
        (At truck1 Birmingham)
        (At truck2 Manchester)
    )
    (:goal
        (and (At cargo3 Manchester) (At cargo4 Birmingham))
    )
)