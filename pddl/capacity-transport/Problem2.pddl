;;Templated problem using jinja2 for learning purposes only 

(define (problem Problem2)
    (:domain capacity-transport)

    (:objects

        cargo1 cargo2 cargo3 cargo4 plane1 plane2 truck1 truck2 London Egham Tokyo Shiraz d1 d2 d3 d4 d5 d6 x0 x1 x2 x3 x4 x5 x6

    )

    (:init

        (= (total-cost) 0)

        (current_time d1)

        (day-to-day d1 d2)
        
        (day-to-day d2 d3)

        (day-to-day d3 d4)

        (day-to-day d4 d5)
        
        (day-to-day d5 d6)
    
        (Cargo cargo1)

        (Cargo cargo2)

        (Cargo cargo3)
        
        (Cargo cargo4)

        (Plane plane1)

        (Plane plane2)

        (Truck truck1)

        (Truck truck2)

        (Location London)

        (Location Egham)

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

        (capacity-counter x0 x1)

        (capacity-counter x1 x2)

        (capacity-counter x2 x3)

        (capacity-counter x3 x4)

        (capacity-counter x4 x5)

        (capacity-counter x5 x6)

        (capacity truck1 x5)

        (capacity truck2 x3)

        (capacity plane1 x1) ; max level capacity 
        
        (capacity plane2 x3)

    )

    (:goal

        (and (At cargo3 Tokyo) (At cargo4 London) (At cargo1 Egham) (At cargo2 Shiraz))

    )
)