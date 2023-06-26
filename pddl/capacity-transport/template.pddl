(define (problem {{ problem_name }})
(:domain {{ domain_name }})

(:objects
{% for object in objects %}
    {{ object }}
{% endfor %}
)

(:init
{% for fact in initial_state %}
    {{ fact }}
{% endfor %}
)

(:goal
{% for condition in goal_state %}
    {{ condition }}
{% endfor %}
)
)
