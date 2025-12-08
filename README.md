# ecg-digitization
ECG Digitization Project
Converting ECG Images → Time-Series Data Using Computer Vision & Machine Learning
This project aims to reconstruct digital time-series ECG signals from images of electrocardiogram printouts. The goal is to build a robust pipeline capable of handling real-world ECG images, including scans, mobile photos, and degraded paper records.
This project is inspired by a Kaggle competition but is being developed independently as a portfolio-focused biomedical machine learning project.
Project Goals
Extract ECG waveforms from noisy, grid-based images
Convert pixel-level signals into calibrated 1D time-series
Build lightweight ML and classical CV models suitable for limited compute
Evaluate performance using ground-truth digital ECG signals
Produce clean, reproducible research code and documentation
Methods Overview
This project will explore several approaches:
1. Classical Computer Vision
Grayscale + thresholding
Gridline removal
Edge detection
Curve tracing / morphological thinning
Resampling into waveform arrays
2. Machine Learning Models
Small CNN regression model
Autoencoder for curve reconstruction
