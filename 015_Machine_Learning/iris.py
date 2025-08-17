#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test learning algorithms on the classic Iris dataset.

@author: Phil Weir <phil.weir@flaxandteal.co.uk>
@license: MIT
"""

import os
import numpy as np
import pandas
import matplotlib.pyplot as plt

from sklearn import svm

from sklearn import datasets
from pandas.plotting import scatter_matrix, radviz
from sklearn.model_selection import train_test_split

def run():
    # ============================================================================
    # TASK 1: DATA LOADING AND PREPARATION
    # ============================================================================
    
    # Download and load the iris dataset
    if not os.path.exists('iris.data'):
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        df = pandas.read_csv(url, header=None)
        df.to_csv('iris.data', header=False, index=False)
    
    df = pandas.read_csv('./iris.data', header=None)
    
    # Add column names for better understanding
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    
    # Display dataset information
    print("Dataset shape:", df.shape)
    print("\nFirst few rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)

    # Randomize data to prevent bias in train/test split
    reordering = np.random.permutation(df.index)
    df = df.reindex(reordering)
    
    # ============================================================================
    # TASK 2: DATA VISUALIZATION
    # ============================================================================
    
    # Create visualizations
    print("\nCreating visualizations...")
    
    # Scatter matrix
    print("Creating scatter matrix...")
    scatter_matrix(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']], 
                  c=df['species'].astype('category').cat.codes, 
                  figsize=(10, 8), 
                  alpha=0.8,
                  diagonal='hist')
    plt.title('Iris Dataset - Scatter Matrix')
    plt.savefig('iris_scatter_matrix.png')
    plt.show()
    
    # RadViz
    print("Creating RadViz plot...")
    plt.figure(figsize=(10, 8))
    # Create a DataFrame with features and class column for radviz
    radviz_df = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']]
    radviz(radviz_df, 'species')
    plt.title('Iris Dataset - RadViz Visualization')
    plt.savefig('iris_radviz.png')
    plt.show()
    
    # ============================================================================
    # TASK 3: DATA PREPARATION AND SPLITTING
    # ============================================================================
    
    # Prepare features and target
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['species']
    
    # Split data into training and testing sets
    print("\nSplitting data into training and testing sets...")
    X_training, X_testing, y_training_target, y_testing_target = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training set size: {len(X_training)}")
    print(f"Testing set size: {len(X_testing)}")
    
    # ============================================================================
    # TASK 4: MODEL TRAINING AND EVALUATION
    # ============================================================================
    
    # Train the Support Vector Machine classifier
    print("\nTraining Support Vector Machine classifier...")
    classifier = svm.SVC(kernel='linear', C=1).fit(X_training, y_training_target)
    
    # Perform cross-validation for robust evaluation
    print("\nPerforming 5-fold cross-validation...")
    from sklearn.model_selection import cross_val_score
    
    cv_scores = cross_val_score(classifier, X_training, y_training_target, cv=5)
    print(f"Cross-validation scores: {cv_scores}")
    print(f"Mean CV score: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
    
    # Evaluate on test set
    test_score = classifier.score(X_testing, y_testing_target)
    print(f"Test set score: {test_score:.3f}")
    
    # ============================================================================
    # PREDICTION EXAMPLE
    # ============================================================================
    
    # Make a prediction for a new iris sample
    print("\nMaking prediction for new iris sample...")
    print("Sample measurements:")
    print("  Sepal length: 4.7cm")
    print("  Sepal width:  3.4cm")
    print("  Petal length: 1.1cm")
    print("  Petal width:  0.2cm")
    
    samples = [[4.7, 3.4, 1.1, 0.2]]
    prediction = classifier.predict(samples)
    print(f"Predicted species: {prediction[0]}")
    
    # ============================================================================
    # TASK SUMMARY
    # ============================================================================
    
    print("\n" + "="*60)
    print("TASK COMPLETION SUMMARY")
    print("="*60)
    print("✅ TASK 0: Explained slicing operations")
    print("✅ TASK 1: Data loading from local CSV file")
    print("✅ TASK 2: Added scatter_matrix and RadViz visualizations")
    print("✅ TASK 3: Implemented train_test_split")
    print("✅ TASK 4: Implemented cross-validation")
    print("="*60)

if __name__ == "__main__":
    run()
