'''
Modelling Sun-Mercury system
'''

# universal gravitational constant in m^3 * kg^–1 * s^–2:
G = 6.67430e-11

# speed of interaction effect in m/s (speed of light is assumed):
c = 299792458

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
# mass of Sun in kg:
M = 1988500e+24

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html

# mass of Mercury in kg:
m = 0.33010e+24

# gravitational constant of the Sun-Mercury system:
g = G * (M + m)

# reduced unit factor for distance:
RU = c ** 2 / g

# eccentricity: 0.205630

# perihelion 46.000E+6 km

# aphelion of Mercury in reduced unit:
r0 = 69.818e+9 * RU

# min orbital velocity in reduced unit:
u0 = 38.86e+3 / c

# reduced unit factor for time:
TU = c ** 3 / g

# initial data:

# time of initial trajectory in reduced unit:
dt = [r0]

# parabolic trajectory is assumed:
x = [r0, r0 - r0 ** -2 * dt[0] ** 2 / 2]
y = [0, u0 * dt[0]]


def acceleration(k):
    '''
    k == 0: classic acceleration
    k > 0: acceleration by retarded interaction
    '''
    n = -1 - k
    return lambda z: -z[n] / (x[n] ** 2 + y[n] ** 2) ** 1.5


def verlet(z, acceleration):
    '''
    Verlet integration with non-constant time differences

    dt[-1] = t_next - t[-1]
    and
    dt[-2] = t[-1] - t[-2]

    Returns z_next.
    '''
    return z[-1] + (z[-1] - z[-2]) * dt[-1] / dt[-2] + acceleration(z) * (dt[-1] + dt[-2]) * dt[-1] / 2


def has_one_year_elapsed():
    return (y[-1] == 0 or (y[-2] < 0 and y[-1] > 0)) and x[-1] > 0


def verlet_1(z):
    return verlet(z, acceleration(1))


year = 0
iteration = 0
orbits = []
year_step_to_display = 300

while year < 3 * year_step_to_display:
    dt += [(x[-1] ** 2 + y[-1] ** 2) ** .5]

    x_next = verlet_1(x)
    y_next = verlet_1(y)
    x += [x_next]
    y += [y_next]

    iteration += 1

    if has_one_year_elapsed():
        year += 1
        print(year, iteration)

        if year % year_step_to_display == 0 or year == 1:
            step = len(x) // 100 or 1
            orbits += [(year, x[-1], (y[-1] - y[-2]) / dt[-1], x[::step], y[::step])]

        x = x[-2:]
        y = y[-2:]
        dt = dt[-2:]

with open('result.py', 'w') as result:
    result.write(f'''
import matplotlib.pyplot as plt

for year, r_max, u_min, x, y in {orbits}:
    plt.plot(x, y, label=f'{{year}}, {{r_max / {r0}:.4g}}, {{u_min / {u0}:.3g}}')
plt.title("""Retarded interaction - Sun-Mercury
Changes of orbit after many orbital period
u[0] = {u0:.3e}  r%[0] = {r0:.3e}""")
plt.legend(title='period, r_max / r[0], u_min / u[0]')
plt.xlabel('r_x%')
plt.ylabel('r_y%')
plt.show()
''')
