"""File for testing MLP class."""

# path to data folder:
data_folder = "../../data/"

import matplotlib.pyplot as plt
#from models.mlp_class import MLP
from preprocessing.load_data_class import DataLoader
from preprocessing.generate_features_class import FeatureGenerator

# import data
# split into training and validation sets
data_loader = DataLoader()
X_train, y_train, X_test, y_test = data_loader.load_and_split_data(data_folder)
Fs = data_loader.Fs

# turn to frequency domain with FeatureGenerator
feature_gen = FeatureGenerator()
freq_range = (50.0, 1000.0)
X_train_fft = feature_gen.compute_fft(X_train, Fs)
peaks = feature_gen.generate_features('fft_peaks', X_train, Fs, freq_range, n_peaks=15)

plt.figure(1)
plt.plot(X_train_fft)
plt.plot(peaks, X_train_fft[peaks], 'x')
plt.show()