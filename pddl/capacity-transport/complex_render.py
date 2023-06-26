import jinja2

locations = ['london', 'egham', 'tokyo', 'shiraz',
             'beijing', 'seoul', 'newyork', 'losangeles', 'sydney']

cargo_locations = {
    'cargo1': 'london',
    'cargo2': 'london',
    'cargo3': 'egham',
    'cargo4': 'egham',
    'cargo5': 'tokyo',
    'cargo6': 'shiraz',
    'cargo7': 'beijing',
    'cargo8': 'seoul',
    'cargo9': 'newyork',
    'cargo10': 'losangeles'
}

truck_locations = {
    'truck1': 'london',
    'truck2': 'egham',
    'truck3': 'tokyo'
}

plane_locations = {
    'plane1': 'shiraz',
    'plane2': 'beijing',
    'plane3': 'seoul'
}

template_loader = jinja2.FileSystemLoader(searchpath='.')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('complex.template')

output = template.render(
    locations=locations,
    cargo_locations=cargo_locations,
    truck_locations=truck_locations,
    plane_locations=plane_locations
)

with open('complex_transport.pddl', 'w') as f:
    f.write("; Generated with complex_render.py using Jinja2 templating tool. \n")
    f.write("; Needs a bit of formatting after the file creation to make the problem file look nicer and more readable. \n")
    f.write("; The goal section of the template does not work and has to be coded manually(to have all cargo objects in the desired locations and not just in order) \n\n")
    f.write(output)
