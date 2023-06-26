; Generated with complex_render.py using Jinja2 templating tool. 
; Needs a bit of formatting after the file creation to make the problem file look nicer and more readable. 
; The goal section of the template does not work and has to be coded manually(to have all cargo objects in the desired locations and not just in order) 

(define (problem ComplexTransport)
    (:domain capacity-transport)

    (:objects
        cargo1 cargo2 cargo3 cargo4 cargo5 cargo6 cargo7 cargo8 cargo9 cargo10 plane1 plane2 plane3 truck1 truck2 truck3 london egham tokyo shiraz beijing seoul newyork losangeles sydney 
        d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 d11 d12 d13 d14 d15 d16 d17 d18 d19 d20 x0 x1 x2 x3 x4 x5 x6
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
        (day-to-day d7 d8)
        (day-to-day d8 d9)
        (day-to-day d9 d10)
        (day-to-day d10 d11)
        (day-to-day d11 d12)
        (day-to-day d12 d13)
        (day-to-day d13 d14)
        (day-to-day d14 d15)
        ; (day-to-day d15 d16)
        ; (day-to-day d16 d17)
        ; (day-to-day d17 d18)
        ; (day-to-day d18 d19)
        ; (day-to-day d19 d20)

        (Cargo cargo1)
        (Cargo cargo2)
        (Cargo cargo3)
        (Cargo cargo4)
        (Cargo cargo5)
        (Cargo cargo6)
        (Cargo cargo7)
        (Cargo cargo8)
        (Cargo cargo9)
        (Cargo cargo10)

        (Plane plane1)
        (Plane plane2)
        (Plane plane3)

        (Truck truck1)
        (Truck truck2)
        (Truck truck3)

        (Location london)
        (Airport london)
        (Location egham)
        (Airport egham)
        (Location tokyo)
        (Airport tokyo)
        (Location shiraz)
        (Airport shiraz)
        (Location beijing)
        (Airport beijing)
        (Location seoul)
        (Airport seoul)
        (Location newyork)
        (Airport newyork)
        (Location losangeles)
        (Airport losangeles)
        (Location sydney)
        (Airport sydney)

        (At cargo1 london)
        (At cargo2 london)
        (At cargo3 egham)
        (At cargo4 egham)
        (At cargo5 tokyo)
        (At cargo6 shiraz)
        (At cargo7 beijing)
        (At cargo8 seoul)
        (At cargo9 newyork)
        (At cargo10 losangeles)

        (At truck1 london)
        (At truck2 egham)
        (At truck3 tokyo)

        (At plane1 shiraz)
        (At plane2 beijing)
        (At plane3 seoul)

        (capacity-counter x0 x1)
        (capacity-counter x1 x2)
        (capacity-counter x2 x3)
        (capacity-counter x3 x4)
        (capacity-counter x4 x5)
        (capacity-counter x5 x6)

        (capacity truck1 x5)
        (capacity truck2 x3)
        (capacity truck3 x2)
        (capacity plane1 x1)
        (capacity plane2 x3)
        (capacity plane3 x4)
    )

    (:goal
        (and
            (At cargo1 egham)
            (At cargo2 london)
            (At cargo3 tokyo)
            (At cargo4 sydney)
            (At cargo5 london)
            (At cargo6 egham)
            (At cargo7 newyork)
            (At cargo8 london)
            (At cargo9 egham)
            (At cargo10 tokyo)
        )
    )
)