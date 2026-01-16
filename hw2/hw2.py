"""
CMSC 14100
Winter 2026
Homework #2

DISTRIBUTION
"""

####################################################################
# Please see the assignment writeup for restrictions on the Python #
# constructs that you are allowed to use in your solutions.        #
####################################################################


# Exercise 1
def add_one_and_multiply(a, x):
    """
    Add 1 to a, and multiply by x.

    Args:
        a (int): an integer value
        x (int): an integer value

    Returns (int):
        The result of adding 1 to a and then multiplying by x
    """
    return (a + 1) * x

# Exercise 2
def is_snowing(temp_f, prec_in):
    """
    Determine whether it is snowing based on temperature and precipitation.

    It is snowing exactly when the temperature is at or below 32°F and the
    precipitation amount is greater than 0 inches.

    Args:
        temp_f (int or float): the temperature in degrees Fahrenheit
        prec_in (int or float): the precipitation amount in inches

    Returns (bool):
        True if it is snowing, False otherwise
    """
    assert prec_in >= 0, "Precipitation amount cannot be negative"

    return (temp_f <= 32) and (prec_in > 0)


# Exercise 3
def convert_fahrenheit_to_celsius(temp_f):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Args:
        temp_f (int or float): a temperature in degrees Fahrenheit

    Returns (int or float):
        The corresponding temperature in degrees Celsius
    """
    return (temp_f - 32) * (5 / 9)


# Exercise 4
def is_extreme_temperature(temp_f):
    """
    Decide whether a temperature is considered extreme by Chicago standards.

    A temperature is extreme if it is below -4.5°F or above 94.9°F.

    Args:
        temp_f (int or float): the temperature in degrees Fahrenheit

    Returns (bool):
        True if the temperature is extreme, False otherwise
    """
    return (temp_f < -4.5) or (temp_f > 94.9)   
         


# Exercise 5
def can_flight_takeoff(temp_f, vel_mph, vis_mi):
    """
    Determine whether a flight can take off based on weather conditions.

    A flight can take off only if all of the following are true:
    the temperature is at least -10°F, the wind speed is no more than 30 mph,
    and the visibility is at least 3 miles.

    Args:
        temp_f (int or float): the temperature in degrees Fahrenheit
        vel_mph (int or float): the wind speed in miles per hour
        vis_mi (int or float): the visibility in miles

    Returns (bool):
        True if takeoff is allowed, False otherwise
    """
    return (temp_f >= -10) and (vel_mph <= 30) and (vis_mi >= 3)


# Exercise 6
def compute_wind_chill(temp_f, vel_mph):
    """
    Compute the wind chill temperature.

    Args:
        temp_f (int or float): the temperature in degrees Fahrenheit
        vel_mph (int or float): the wind speed in miles per hour

    Returns (int or float):
        The wind chill temperature in degrees Fahrenheit
    """
    assert temp_f <= 50, "Temperature must be at or below 50°F"
    assert vel_mph > 3, "Wind speed must be greater than 3 mph"

    v_pow = vel_mph ** 0.16
    return (
    35.74 + (0.6215 * temp_f) - 
    (35.75 * v_pow) +
    (0.4275 * temp_f * v_pow)
    )



# Exercise 7
def is_severe_weather(temp_f, vel_mph, vis_mi, prec_in):
    """
    Determine whether weather conditions are considered severe.

    Weather is considered severe if any one of the following is true:
    the temperature is extreme for Chicago, the flight cannot take off,
    or the precipitation amount is greater than 10 inches.

    Args:
        temp_f (int or float): the temperature in degrees Fahrenheit
        vel_mph (int or float): the wind speed in miles per hour
        vis_mi (int or float): the visibility in miles
        prec_in (int or float): the precipitation amount in inches

    Returns (bool):
        True if weather is severe, False otherwise
    """

    return (
    is_extreme_temperature(temp_f)
    or not can_flight_takeoff(temp_f, vel_mph, vis_mi)
    or (prec_in > 10)
    )
