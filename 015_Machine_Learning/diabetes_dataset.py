

import numpy as np
import pandas as pd

def generate_diabetes_dataset(n_samples=1000, random_state=42):
    """
    Generate synthetic diabetes risk dataset with realistic correlations.
    
    Features:
    - age: Patient age (years)
    - bmi: Body Mass Index
    - systolic_bp: Systolic blood pressure (mmHg)
    - glucose_level: Fasting glucose level (mg/dL)
    - family_history: Family history of diabetes (0=No, 1=Yes)
    
    Target:
    - diabetes_risk: Risk level (Low, Moderate, High)
    """
    
    np.random.seed(random_state)
    
    print(f"Generating {n_samples} synthetic patient records...")
    
    # Generate base demographics
    age = np.random.normal(45, 15, n_samples)  # Mean age 45, std 15
    age = np.clip(age, 18, 85)  # Clip to realistic age range
    
    # Family history (30% have family history)
    family_history = np.random.binomial(1, 0.3, n_samples)
    
    # BMI with some correlation to age (older people tend to have higher BMI)
    bmi_base = np.random.normal(26, 4, n_samples)
    age_effect = (age - 30) * 0.05  # Slight increase with age
    bmi = bmi_base + age_effect + np.random.normal(0, 1, n_samples)
    bmi = np.clip(bmi, 16, 45)  # Realistic BMI range
    
    # Systolic BP correlated with age and BMI
    bp_base = 90 + (age - 18) * 0.8  # Increases with age
    bp_bmi_effect = (bmi - 25) * 1.2  # Increases with BMI
    systolic_bp = bp_base + bp_bmi_effect + np.random.normal(0, 10, n_samples)
    systolic_bp = np.clip(systolic_bp, 90, 200)  # Realistic BP range
    
    # Glucose level influenced by age, BMI, and family history
    glucose_base = 85 + (age - 18) * 0.3  # Slight increase with age
    glucose_bmi_effect = (bmi - 25) * 1.5  # Strong correlation with BMI
    glucose_family_effect = family_history * 15  # Family history adds risk
    glucose_level = (glucose_base + glucose_bmi_effect + 
                    glucose_family_effect + np.random.normal(0, 12, n_samples))
    glucose_level = np.clip(glucose_level, 70, 250)  # Realistic glucose range
    
    # Create diabetes risk based on realistic medical criteria
    risk_scores = np.zeros(n_samples)
    
    # Age factor (higher risk with age)
    risk_scores += np.where(age >= 65, 2, np.where(age >= 45, 1, 0))
    
    # BMI factor
    risk_scores += np.where(bmi >= 30, 2, np.where(bmi >= 25, 1, 0))
    
    # Blood pressure factor
    risk_scores += np.where(systolic_bp >= 140, 2, np.where(systolic_bp >= 130, 1, 0))
    
    # Glucose factor (most important)
    risk_scores += np.where(glucose_level >= 126, 3, 
                           np.where(glucose_level >= 100, 2, 
                                   np.where(glucose_level >= 90, 1, 0)))
    
    # Family history factor
    risk_scores += family_history * 2
    
    # Add some randomness to make it more realistic
    risk_scores += np.random.normal(0, 0.5, n_samples)
    
    # Convert to categorical risk levels
    diabetes_risk = np.where(risk_scores >= 6, 'High',
                            np.where(risk_scores >= 3, 'Moderate', 'Low'))
    
    # Create DataFrame
    df = pd.DataFrame({
        'age': np.round(age, 1),
        'bmi': np.round(bmi, 1),
        'systolic_bp': np.round(systolic_bp, 0).astype(int),
        'glucose_level': np.round(glucose_level, 0).astype(int),
        'family_history': family_history,
        'diabetes_risk': diabetes_risk
    })
    
    return df

def save_dataset(df, filename='diabetes_risk_dataset.csv'):
    """
    Save the dataset to CSV file.
    """
    df.to_csv(filename, index=False)
    print(f"✅ Dataset saved as '{filename}'")
    print(f"📊 Dataset shape: {df.shape}")
    return filename

def run():
    """
    Main function to generate and save the diabetes dataset.
    """
    print("Creating Synthetic Diabetes Risk Dataset")
    print("="*50)
    
    # Generate the dataset
    df = generate_diabetes_dataset(n_samples=1000, random_state=42)
    
    # Save to CSV
    csv_filename = save_dataset(df)
    
    
if __name__ == "__main__":
    run()
