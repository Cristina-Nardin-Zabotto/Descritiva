import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.stats.api as sms
from scipy import stats
from scipy.stats import norm

# Supported confidence levels: 50%, 68%, 90%, 95%, and 99%
confidence_level_constant = [0.50, .67], [0.68, .99], [0.90, 1.64], [0.95, 1.96], [0.99, 2.57]
pd.options.display.float_format = '{:0.2f}'.format

def calc_finite_pop(sample_size_infinite, pop_size):
    return round(sample_size_infinite / (1 + ((sample_size_infinite - 1) / float(pop_size))))


def sample_size_prop(confidence_level, sample_error, p=0.5, pop_size=None):
    print("confidence_level: ", confidence_level)
    print("sample error: ", sample_error)
    print("p: ", p)
    print("pop_size: ", pop_size)
    print()

    z_value = 0.0
    e = sample_error / 100.0

    # Loop through supported confidence levels and find the num std deviations for that confidence level
    for i in confidence_level_constant:
        if i[0] == confidence_level:
            z_value = i[1]

    if z_value == 0.0:
        return -1

    # Calculates sample size for Infinite population
    sample_size_infinite = ((z_value ** 2) * p * (1 - p)) / (e ** 2)
    print("Sample Size for infinite population: %d" % sample_size_infinite)

    if pop_size:
        # Adjusts sample size for finite population
        sample_size_finite = calc_finite_pop(sample_size_infinite, pop_size)
        print("Sample Size for finite population: %d" % sample_size_finite)

    print()


def sample_size_mean(confidence_level, std_dev, sample_error, pop_size=None):
    print("confidence_level: ", confidence_level)
    print("std_dev: ", std_dev)
    print("sample_error: ", sample_error)
    print("pop_size: ", pop_size)
    print()

    alpha = 1 - confidence_level
    z = -norm.ppf(alpha / 2)

    # Calculates sample size for Infinite population
    sample_size_infinite = round(((z * std_dev) / sample_error) ** 2)

    print("Sample Size for infinite population: %d" % sample_size_infinite)

    if pop_size:
        # Adjusts sample size for finite population
        sample_size_finite = calc_finite_pop(sample_size_infinite, pop_size)
        print("Sample Size for finite population: %d" % sample_size_finite)

    print()


if __name__ == "__main__":

#  Sample Size

    sample_size_prop(confidence_level=0.95, sample_error=10.0, pop_size=30)
    sample_size_prop(confidence_level=0.95, sample_error=10.0)
    sample_size_mean(confidence_level=0.95, std_dev=5, sample_error=2, pop_size=30)
    sample_size_mean(confidence_level=0.95, std_dev=5, sample_error=2)







