# ecg-digitization
ECG Digitization Project
Converting ECG Images → Time-Series Data Using Computer Vision & Machine Learning
This project aims to reconstruct digital time-series ECG signals from images of electrocardiogram printouts. The goal is to build a robust pipeline capable of handling real-world ECG images, including scans, mobile photos, and degraded paper records.
This project is inspired by a Kaggle competition but is being developed independently as a portfolio-focused biomedical machine learning project.

Project Goals
- Extract ECG waveforms from noisy, grid-based images
- Convert pixel-level signals into calibrated 1D time-series
- Build lightweight ML and classical CV models suitable for limited compute
- Evaluate performance using ground-truth digital ECG signals
- Produce clean, reproducible research code and documentation

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

Repository Structure
```text
ecg-digitization/
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_baseline_model.ipynb
│   └── 04_inference.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── curve_extraction.py
│   ├── model.py
│   ├── train.py
│   └── inference.py
│
├── experiments/
│   └── experiment_log.md
│
└── kaggle/
    └── placeholder.txt
  ```  
Dataset
- The project uses images and ECG time-series metadata that include:
- ECG waveform images (scans, photos, degradations)
- 12-lead digital ground-truth signals
- Sampling frequency
- Lead-specific signal lengths
- Metadata for training and evaluation
(Dataset is not stored in this repo due to size.)

Evaluation Metrics
- RMSE
- Dynamic Time Warping (DTW)
- R-peak alignment
- Visual overlay plots

Setup
Install dependencies:
pip install -r requirements.txt
Run preprocessing (example):
python src/preprocessing.py

Project Status
- [ ] Repo initialized
- [ ] Data exploration notebook
- [ ] Lead-level cropping
- [ ] Gridline removal pipeline
- [ ] Curve extraction prototype
- [ ] Baseline ML model
- [ ] Evaluation suite
- [ ] Final report + writeup

License
MIT License
