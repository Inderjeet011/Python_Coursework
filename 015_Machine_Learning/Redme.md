# Iris Dataset Machine Learning Project

## Overview
This project demonstrates a complete machine learning workflow using the classic Iris dataset. The script (`iris.py`) implements various machine learning tasks from data loading to model evaluation and prediction.

## Dataset
The Iris dataset contains measurements of 150 iris flowers from three different species:
- **Iris Setosa**
- **Iris Versicolor** 
- **Iris Virginica**

Each flower is described by four features:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

## Tasks Implemented

### TASK 1: Data Loading and Preparation
- Downloads the Iris dataset from UCI Machine Learning Repository
- Loads data into a pandas DataFrame
- Adds meaningful column names
- Displays dataset information (shape, first few rows, data types)
- Randomizes data to prevent bias in train/test split

### TASK 2: Data Visualization
Creates two types of visualizations:

1. **Scatter Matrix Plot** (`iris_scatter_matrix.png`)
   - Shows relationships between all feature pairs
   - Includes histograms on the diagonal
   - Color-coded by species for easy identification

2. **RadViz Plot** (`iris_radviz.png`)
   - Radial visualization showing how well features separate the classes
   - Useful for understanding feature importance and class separability

### TASK 3: Data Preparation and Splitting
- Prepares features (X) and target variable (y)
- Splits data into training (80%) and testing (20%) sets
- Uses stratified sampling to maintain class distribution
- Sets random state for reproducibility

### TASK 4: Model Training and Evaluation
- Trains a Support Vector Machine (SVM) classifier with linear kernel
- Performs 5-fold cross-validation for robust evaluation
- Evaluates model performance on the test set
- Reports accuracy scores

Splitting data into training and testing sets...
Training set size: 120
Testing set size: 30

Training Support Vector Machine classifier...

Performing 5-fold cross-validation...
Cross-validation scores: [0.91666667 0.95833333 1.         1.         0.95833333]
Mean CV score: 0.967 (+/- 0.062)
Test set score: 0.967

Making prediction for new iris sample...
Sample measurements:
  Sepal length: 4.7cm
  Sepal width:  3.4cm
  Petal length: 1.1cm
  Petal width:  0.2cm
Predicted species: Iris-setosa

### Machine Learning Techniques Used
- **Support Vector Machine (SVM)** with linear kernel
- **Cross-validation** for robust model evaluation
- **Stratified sampling** for balanced train/test split

## Performance Results
- **Cross-validation accuracy**: 96.7% (mean score: 0.967)
- **Cross-validation scores**: [0.917, 0.958, 1.000, 1.000, 0.958] - showing excellent consistency
- **Test set accuracy**: 96.7%
- **Standard deviation**: ±0.062 (very low variance indicates stable model)
## Dependencies
- `numpy` - Numerical computing
- `pandas` - Data manipulation and analysis
- `matplotlib.pyplot` - Plotting and visualization
- `sklearn` - Machine learning algorithms and utilities

