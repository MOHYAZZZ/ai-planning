;;Simple and basic problem.
;;This problem will get harder as the term goes by and get a better understanding of PDDL.
(define (problem problem1)
    (:domain cargo-transport)
    (:objects
        cargo1 cargo2 plane1 plane2 London New-york

    )

    (:init
        (Cargo cargo1)
        (Cargo cargo2)
        (Plane plane1)
        (Plane plane2)
        (Airport London)
        (Airport New-york)

        (At cargo1 New-york)
        (At cargo2 London)
        (At plane1 New-york)
        (At plane2 London)

    )
    (:goal
        (and (At cargo1 London) (At cargo2 New-york))
    )
)