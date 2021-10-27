def pipe_skin_friction_coefficient(reynolds_number):
    return 0.079 * (reynolds_number ** -0.25)


def wall_skin_friction_coefficient(reynolds_number):
    return 0.058 * (reynolds_number ** -0.20)


def turbulent_skin_friction_coefficient(reynolds_number):
    return 0.027 * (reynolds_number ** (-1 / 7))
