;;Templated problem using jinja2 for learning purposes only 

(define (problem Problem1)
(:domain expensive-transport)

(:objects

    cargo1

    cargo2

    cargo3

    cargo4

    plane1

    plane2

    truck1

    truck2

    London

    Egham

    Tokyo

    Shiraz

    d1

    d2

    d3

    d4

    d5

    d6

)

(:init

    (= (total-cost) 0)

    (current_time d1)

    (day-to-day d1 d2)(day-to-day d2 d3)

    (day-to-day d3 d4)

    (day-to-day d4 d5)(Cargo cargo1)

    (Cargo cargo2)

    (Cargo cargo3)(Cargo cargo4)

    (Plane plane1)

    (Plane plane2)

    (Truck truck1)

    (Truck truck2)

    (Location London)

    ;(Location Egham)

    (Location Tokyo)

    (Location Shiraz)

    (Airport London)

    (Airport Egham)

    (Airport Tokyo)

    (Airport Shiraz)

    (At cargo1 London)

    (At truck1 London)

    (At truck2 Egham)

    (At cargo4 Egham)

    (At plane1 Tokyo)

    (At cargo2 Tokyo)

    (At cargo3 Shiraz)

    (At plane2 Shiraz)

)

(:goal

    (and (At cargo3 Tokyo) (At cargo4 London) (At cargo1 Egham) (At cargo2 Shiraz))

)
)