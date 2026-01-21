# ecg-digitization
ECG Digitization Project
Converting ECG Images → Time-Series Data Using Computer Vision 
This project reconstructs digital ECG time-series signals from images of electrocardiogram (ECG) printouts. The goal is to build a robust, reproducible pipeline capable of handling real-world ECG images, including scans, mobile photos, and degraded paper records.
This project is inspired by a Kaggle challenge but is developed independently as a portfolio-focused biomedical signal processing and computer vision project.
Project Goals
- Extract ECG waveforms from noisy, grid-based images
- Convert pixel-level curves into calibrated 1D time-series
- Handle real-world artifacts (gridlines, blur, broken traces)
- Align extracted signals with digital ground truth
- Evaluate performance using quantitative metrics and visual overlays
- Produce clean, reproducible research code 

Implemented Pipeline
1. Preprocessing
- Grayscale conversion
- Contrast enhancement
- Adaptive thresholding
2. Gridline Suppression
- Morphological filtering
- Structural element removal
- Noise cleanup
3. Lead-Level Cropping
- Automatic segmentation of individual leads
- Margin trimming
4. Curve Extraction
- Continuity-aware column-wise tracking
- Gap re-locking
- Pixel-space denoising
- Smoothing and interpolation
5. Signal Reconstruction
- Pixel → signal normalization
- Baseline correction
- Time-series resampling
6. Ground-Truth Alignment
- Best window matching (handles time-span mismatch)
- Shift alignment
- Shape-based evaluation

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
│   ├── 03_lead_cropping.ipynb
│   └── curve_extraction.ipynb
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

Evaluation 
Evaluation focueses on shpae fidelity and temporal alginment, not just pointwise error
Metrics
- RMSE
- Dynamic Time Warping (DTW)
- R-peak alignment
- Visual overlay plots

Setup
Install dependencies:
pip install -r requirements.txt
Run preprocessing (example):
python src/preprocessing.py

Evaluation
Current evaluation focuses on shape and temporal alignment, not just pointwise error.
Metrics
Pearson correlation (primary)
Visual overlay plots (primary diagnostic)
RMSE (planned)
Dynamic Time Warping (planned)
R-peak alignment (planned)

Example Result (Current Baseline)
Using classical CV + continuity tracking + GT window alignment:
- Correlation (aligned window): ~0.79
- Robust to grid noise, broken traces, and partial crops
- Good local alignment of wavefrom morphology

Limitations:
- Performance depends on the quality of thresholding and grid removal
- Very faint traces can be difficult to recover
- Heavy overlap between gridlines and trace may cause tracking errors
- Current pipeline operates on single leads independently
- Calibration to physical units (mV, ms) is not yet implemented

Setup
Install Dependencies:
pip install -r requirements.txt

Project Status
- [X] Repo initialized
- [X] Data exploration notebook
- [X] Lead-level cropping
- [X] Gridline removal pipeline
- [X] Curve extraction prototype
- [ ] Baseline ML model
- [ ] Evaluation suite
- [ ] Final report + writeup

License
MIT License
