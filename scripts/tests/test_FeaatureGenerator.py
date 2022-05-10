"""File for testing FeatureGenerator class."""


import numpy as np
import matplotlib.pyplot as plt
from preprocessing.load_data_class import DataLoader
from preprocessing.generate_features_class import FeatureGenerator


# path to data folder:
data_folder = "../../data/"

# number of FFT points:
N_fft = np.power(2, 16)
# number of data examples to use:
num_examples = 10


print()
# load data:
data_loader = DataLoader()
X_raw, y, _, _ = data_loader.load_and_split_data(data_folder)
Fs = data_loader.Fs
X_raw = X_raw[0:num_examples]
y = y[0:num_examples]


# test FeatureGenerator class:
feature_generator = FeatureGenerator()
example = 5

# test computation of FFT:
# plot raw audio data in time domain:
feature_generator.plot_time(X_raw, Fs, example, norm=True, fig_num=1)
# compute and plot FFT:
X_fft = feature_generator.compute_fft(X_raw, Fs, N_fft=N_fft, norm=True)
feature_generator.plot_freq(X_fft, example, fig_num=2)

# test fft_bins() method:
freq_range = (50.0, 100.0)
n_bins = 5
X_fft_bin = feature_generator.generate_features("fft_bins", X_raw, Fs, N_fft=N_fft, norm=True, freq_range=freq_range,
                                                n_bins=n_bins)
print(X_fft_bin.shape)


# show plots:
plt.show()

