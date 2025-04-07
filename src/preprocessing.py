import pandas as pd

def clean_data(df):
    """Clean and preprocess loan prediction data"""
    # Drop Loan_ID
    df = df.drop('Loan_ID', axis=1)
    
    # Fill missing values in categorical columns with mode
    categorical_cols = ['Gender', 'Married', 'Dependents', 'Self_Employed']
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    # Fill missing values in numerical columns
    df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
    df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)
    
    # Remove outliers from ApplicantIncome and CoapplicantIncome
    df = remove_outliers(df, 'ApplicantIncome')
    df = remove_outliers(df, 'CoapplicantIncome')
    
    return df

def remove_outliers(df, column):
    """Remove outliers using IQR method"""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]