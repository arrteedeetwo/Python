# print numpy array without scientific notation
np.array_str(x,  suppress_small=True)


# make dummy variables out of a variable with categories (logistic regressoin)
pd.get_dummies()

# OSX grapichs/framework workaround for venv
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
