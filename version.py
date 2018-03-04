import sys
import os
import platform
import re
import pandas as pd
import decimal
import matplotlib
import numpy as np
import IPython
import scipy
import sklearn
import tensorflow as tf
import requests

print("\n")
print("Python version: %s" % sys.version)
print("sys.platform: %s" % sys.platform)
print("Python OS Name: %s" % os.name)
print("platform version: %s" % platform.__version__)
print("platform system: %s" % platform.system())
print("re version: %s" % re.__version__)
print("pandas version: %s" % pd.__version__)
print("decimal version: %s" % decimal.__version__)
print("matplotlib version: %s" % matplotlib.__version__)
print("numpy version: %s" % np.__version__)
print("IPython version: %s" % IPython.__version__)
print("scipy version: %s" % scipy.__version__)
print("scikit-learn version: %s" % sklearn.__version__)
print("tensorflow version: %s" % tf.__version__)
print("requests version: %s" % requests.__version__)

print("\n########################")
from scipy import sparse
# create a 2d numpy array with a diagonal of ones, and zeros everywhere else
eye = np.eye(6)
print("Numpy array:\n%s" % eye)
# convert the numpy array to a scipy sparse matrix in CSR format
# only the non-zero entries are stored
print("########################")
sparse_matrix = sparse.csr_matrix(eye)
print("\nScipy sparse CSR matrix:\n%s" % sparse_matrix)

print("########################")
import pandas as pd
# create a simple dataset of people
data = {'Name': ["John", "Anna", "Peter", "Linda"],
'Location' : ["New York", "Paris", "Berlin", "London"],
'Age' : [24, 13, 53, 33]
}
data_pandas = pd.DataFrame(data)
print("\n", data_pandas)
