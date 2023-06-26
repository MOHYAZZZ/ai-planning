;; PDDL instance problem for the Air cargo transport
;; The author of this piece of code is: https://github.com/arii
;; This is a simple PDDL code inspired by the book Artificial Intelligence : A Modern Approach page 369-370

(define (problem pb1)
    (:domain air-cargo)
    (:objects
        C1 C2 P1 P2 SFO JFK
    )
    (:init
        ;; types
        (Cargo C1)
        (Cargo C2)
        (Plane P1)
        (Plane P2)
        (Airport SFO)
        (Airport JFK)

        ;; locations
        (At C1 SFO)
        (At C2 JFK)
        (At P1 SFO)
        (At P2 JFK)
    )

    (:goal
        (and (At C1 JFK) (At C2 SFO))
    )
)