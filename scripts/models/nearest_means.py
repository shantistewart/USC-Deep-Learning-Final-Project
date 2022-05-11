"""Script for running a nearest means classifier."""


import numpy as np
from sklearn.neighbors import NearestCentroid
from models.run_model import run_model


# path to data folder:
data_folder = "../../data/"


print()
# create nearest means classifier (with Euclidean distance metric):
model = NearestCentroid(metric="euclidean")
# fraction of total data to use for test set:
test_fract = 0.2
# feature generation parameters:
feature_type = "fft_bins"
freq_range = (55.0, 1760.0)
N_fft = np.power(2, 16)
n_bins = 5
feature_gen_params = {
    "freq_range": freq_range,
    "n_bins": n_bins,
    "N_fft": N_fft,
    "norm": True
}
# feature normalization type:
norm_type = None

# run model:
run_model(data_folder, model, test_fract, feature_type, feature_gen_params, norm_type=norm_type, tune_model=False)

