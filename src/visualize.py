import plotly.express as px
import pandas as pd

def plot_loan_status(df):
    """Plot loan approval status distribution"""
    loan_status_count = df['Loan_Status'].value_counts()
    fig = px.pie(loan_status_count, 
                 names=loan_status_count.index, 
                 title='Loan Approval Status')
    fig.show()

def plot_income_distribution(df):
    """Plot applicant income distribution"""
    fig = px.histogram(df, x='ApplicantIncome', 
                       title='Applicant Income Distribution')
    fig.show()

def plot_credit_history(df):
    """Plot relationship between credit history and loan status"""
    fig = px.histogram(df, x='Credit_History', color='Loan_Status', 
                      barmode='group',
                      title='Loan_Status vs Credit_History')
    fig.show()