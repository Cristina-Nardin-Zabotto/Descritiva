import statsmodels.stats.api as sms
import pandas as pd

def get_example_data():
    x = [432, 32, 654, 6542, 5432, 453, 147, 765, 687]
    x2 = [1432, 132, 1654, 16542, 15432, 1453, 1147, 1765, 1687]
    return pd.DataFrame({'$x$': x, '$x_2$': x2})


def normality_test(data, verbose=True):
    """ Applies Normality Test (Anderson-Darling). """
    statistic, pvalue = sms.diagnostic.normal_ad(data)
    if verbose:
        print("Anderson-Darling:\n\tstatistic={}, \n\tpvalue={}".format(statistic, pvalue))

    return statistic, pvalue

example_data = get_example_data()
normality_test(example_data)
