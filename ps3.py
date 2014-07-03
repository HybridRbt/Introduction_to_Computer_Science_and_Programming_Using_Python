__author__ = 'jeredyang'


def f(x):
    import math

    return 10 * math.e ** (math.log(0.5) / 5.27 * x)


def radiationExposure(start, stop, step):
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    """
    # FILL IN YOUR CODE HERE...
    total = 0
    points = []

    while start < stop:
        points.append(start)
        start += step

    for point in points:
        total += f(point) * step

    return total


def radiationExposureRecur(start, stop, step):
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    """
    # FILL IN YOUR CODE HERE...
    if start + step >= stop:
        return f(start) * step

    return f(start) * step + radiationExposure(start + step, stop, step)


def test():
    print radiationExposure(0, 5, 1)
    print radiationExposure(5, 11, 1)
    print radiationExposure(0, 11, 1)
    print radiationExposure(40, 100, 1.5)

    assert radiationExposure(0, 5, 1) - radiationExposureRecur(0, 5, 1) < 0.001
    assert radiationExposure(5, 11, 1) == radiationExposureRecur(5, 11, 1)
    assert radiationExposure(0, 11, 1) == radiationExposureRecur(0, 11, 1)
    assert radiationExposure(40, 100, 1.5) - radiationExposureRecur(40, 100, 1.5) < 0.001

test()
