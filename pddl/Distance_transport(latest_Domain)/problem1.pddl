; Currently does not work 
; will debug this after Modifying FD
(define (problem problem1)
    (:domain distance-transport)
    (:objects
        cargo1 cargo2 plane1 plane2 truck1 truck2 London LHR New-york JFK d1 d2 d3 x0 x1 x2 x3
    )

    (:init
        (= (total-cost) 0)
        (current-time d1)
        (day-to-day d1 d2)
        (day-to-day d2 d3)

        (capacity-counter x0 x1)
        (capacity-counter x1 x2)

        (capacity plane1 x1) ; max level capacity 
        (capacity plane2 x3)

        (current_time day1)
        (at cargo1 LHR)
        (at cargo2 JFK)
        (at plane1 LHR)
        (at plane2 New-york)
        (at truck1 London)
        (at truck2 New-york)
        (distance London New-york 30)
        (distance LHR JFK 30)
    )

    (:goal
        (and (at cargo1 London) (at cargo2 New-york))

    )

    (:metric minimize
        (total-cost)
    )
)