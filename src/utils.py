import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score

def evaluate_model(y_true, y_pred):
    """Calculate and return evaluation metrics"""
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, pos_label='Y'),
        'recall': recall_score(y_true, y_pred, pos_label='Y')
    }

def save_results(results, filepath):
    """Save prediction results to CSV"""
    pd.DataFrame(results).to_csv(filepath, index=False)
    print(f"Results saved to {filepath}")

def load_data(filepath):
    """Load data from CSV with basic validation"""
    df = pd.read_csv(filepath)
    required_columns = [
        'Gender', 'Married', 'Dependents', 'Education',
        'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome',
        'LoanAmount', 'Loan_Amount_Term', 'Credit_History',
        'Property_Area', 'Loan_Status'
    ]
    
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing required columns in dataset")
    
    return df