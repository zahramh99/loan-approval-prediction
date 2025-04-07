import pandas as pd
from preprocessing import clean_data
from train import train_model
from visualize import plot_loan_status, plot_income_distribution

def main():
    # Load data
    df = pd.read_csv('data/loan_prediction.csv')
    
    # Clean and preprocess data
    df = clean_data(df)
    
    # Visualize data
    plot_loan_status(df)
    plot_income_distribution(df)
    
    # Train model
    model, X_test, y_test = train_model(df)
    
    # Make predictions
    predictions = model.predict(X_test)
    results = X_test.copy()
    results['Loan_Status_Predicted'] = predictions
    print("\nPrediction Results:")
    print(results.head())

if __name__ == "__main__":
    main()