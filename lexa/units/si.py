from .dimensions import base_dimensions as dims
from .quantity import Quantity

# Base Units
metre = Quantity("meter", dims.length)
kilogram = Quantity("kilogram", dims.mass)
second = Quantity("second", dims.time)
ampere = Quantity("ampere", dims.current)
kelvin = Quantity("kelvin", dims.temperature)
mole = Quantity("mole", dims.amount)
candela = Quantity("candela", dims.luminous_intensity)

# Compound Units
joule = Quantity("joule", kilogram * metre ** 2 * second ** -2)
newton = Quantity("newton", kilogram * metre * second ** -2)
