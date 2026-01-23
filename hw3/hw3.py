"""
CMSC 14100
Winter 2026
Homework #3

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

def find_relative_return(current_day_price, prev_day_price):
    """
    Calculates the relative return for a pair of prices.

    The return is defined as the ratio of the price on the specified
    day to the price on the previous day.

    Args:
        current_day_price (float): the current day's price
        prev_day_price (float): the previous day's price

    Returns (float | None):
            - Returns the ratio of current day to previous day.
            - Returns None if either price is 0 or negative.
    """
    if current_day_price <= 0 or prev_day_price <= 0:
     return None
    return current_day_price / prev_day_price


def find_value_at_risk(current_day_price, prev_day_price):
    """
    Calculates the value at risk for a pair of prices.

    Args:
        current_day_price (float): the current day's price
        prev_day_price (float): the previous day's price

    Returns (float | None):
        - Returns None if the relative return cannot be computed.
        - Returns 0.0 if the relative return is greater than 1.0.
        - Otherwise, returns 1 minus the relative return.
    """
    rel_return = find_relative_return(current_day_price, prev_day_price)
    if rel_return is None:
        return None

    if rel_return > 1.0:
        return 0.0

    return 1 - rel_return


def get_stock_rating(return_on_investment, avg_value_at_risk):
    """
    Determines the stock rating based on return on investment and
    average value at risk.

    Args:
        return_on_investment (float): the return on investment
        avg_value_at_risk (float): the average value at risk

    Returns (str):
        One of the follwoing ratings: 
        "AAA", "AA", "A", "BBB", "BB", "B", "C", or "D"
    """
    if return_on_investment >= 1.1 and avg_value_at_risk < 0.05:
        return "AAA"

    if return_on_investment >= 1.1 and avg_value_at_risk < 0.1:
        return "AA"

    if return_on_investment >= 1.1 and avg_value_at_risk < 0.15:
        return "A"

    if return_on_investment >= 1.2 and avg_value_at_risk < 0.2:
        return "BBB"

    if return_on_investment >= 1.2 and avg_value_at_risk < 0.25:
        return "BB"

    if return_on_investment >= 1.2 and avg_value_at_risk < 0.3:
        return "B"

    if return_on_investment >= 1.4 and avg_value_at_risk >= 0.3:
        return "C"

    return "D"


def compare_stock_ratings(ratings_1, ratings_2):
    """
    Compares two stock ratings.

    Args:
        rating_1 (str): rating for stock 1
        rating_2 (str): rating for stock 2

    Returns (int):
        1  if ratings_1 is better
        -1 if ratings_2 is better
        0  if they are equal
    """
    rating_order = ["D", "C", "B", "BB", "BBB", "A", "AA", "AAA"]

    value_1 = 0
    value_2 = 0

    
    for i in range(len(rating_order)):
        if ratings_1 == rating_order[i]:
            value_1 = i + 1
            break

   
    for i in range(len(rating_order)):
        if ratings_2 == rating_order[i]:
            value_2 = i + 1
            break

    if value_1 > value_2:
        return 1
    if value_2 > value_1:
        return -1
    return 0


def find_period_return(prices):
    """
    Computes the relative return over a time period.

    Args:
        prices (list[float]): list of prices over time

    Returns (float | None):
        - None if the list is empty
        - None if any price is <= 0
        - Otherwise, last price divided by first price
    """
    
    if len(prices) == 0:
        return None

    
    for p in prices:
        if p <= 0:
            return None

    
    first_price = prices[0]
    last_price = prices[len(prices) - 1]

    return last_price / first_price


def find_avg_var(prices):
    """
    Computes the average value at risk over a time period.

    Args:
        prices (list[float]): list of prices over time

    Returns (float | None):
        - None if prices is empty
        - None if any price <= 0
        - 0.0 if there is only one valid price
        - Otherwise, the average value at risk
    """
    
    if len(prices) == 0:
        return None

    for p in prices:
        if p <= 0:
            return None

    if len(prices) == 1:
        return 0.0

    total_var = 0.0
    count = 0

    for i in range(1, len(prices)):
        var = find_value_at_risk(prices[i], prices[i - 1])
        if var is None:
          return None
        total_var += var
        count += 1

    return total_var / count

def find_stock_rating_from_prices(prices):
    """
    Determines the stock rating from a list of prices.

    Args:
        prices (list[float]): list of prices over time

    Returns (str | None):
        - Stock rating if computable
        - None if period return or average value at risk is None
    """
    period_return = find_period_return(prices)
    avg_var = find_avg_var(prices)

    if period_return is None or avg_var is None:
        return None

    return get_stock_rating(period_return, avg_var)
