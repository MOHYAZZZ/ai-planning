;My intial and basic cargo transport Domain
;; actions load unload and fly was not implemented by me

(define (domain cargo-transport)

    (:requirements :strips :action-costs :fluents)

    (:predicates
        (In ?obj ?place)
        (At ?obj ?place)
        (Location ?place)
        (Cargo ?obj)
        (Plane ?obj)
        (Airport ?obj)
        (Truck ?obj)

    )

    ; (:functions
    ;     (total-cost) - number
    ; )
    (:action LOAD
        :parameters (?c ?p ?a)
        :precondition (and (At ?c ?a)
            (At ?p ?a)
            (Cargo ?c)
            (Plane ?p)
            (Airport ?a))
        :effect (and (not (At ?c ?a)) (In ?c ?p))
    )

    (:action UNLOAD
        :parameters (?c ?p ?a)
        :precondition (and (In ?c ?p)
            (At ?p ?a)
            (Cargo ?c)
            (Plane ?p)
            (Airport ?a))
        :effect (and (not (In ?c ?p)) (At ?c ?a))
    )

    (:action FLY
        :parameters (?p ?from ?to)
        :precondition (and (At ?p ?from)
            (Plane ?p)
            (Airport ?from)
            (Airport ?to))
        :effect (and
            (not (At ?p ?from))
            (At ?p ?to)
            ; (increase (total-cost) 5)
        )
    )
    (:action Drive
        :parameters (?t ?from ?to)
        :precondition (and(At ?t ?from)
            (Truck ?t)
            (Location ?from)
            (Location ?to))
        :effect (and
            (not (At ?t ?from))
            (At ?t ?to)
            ; (increase (total-cost) 5)
        )
    )
    ;; I am keeping the load and unload for planes and trucks seperate for now might concatinate them later (:action Pick-up
    (:action Pick-up
        :parameters (?c ?t ?l)
        :precondition (and (At ?c ?l)
            (At ?c ?l)
            (At ?t ?l)
            (Cargo ?c)
            (Truck ?t)
            (Location ?l)

        )
        :effect (and (not (At ?c ?l)) (In ?c ?t))
    )
    (:action drop
        :parameters (?c ?t ?l)
        :precondition (and (In ?c ?t)
            (At ?t ?l)
            (Cargo ?c)
            (Truck ?t)
            (Location ?l))
        :effect (and (not (In ?c ?t)) (At ?c ?l))
    )
)