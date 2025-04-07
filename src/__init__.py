"""
loan-approval-prediction package

This package provides functionality for predicting loan approvals
using machine learning techniques.
"""

__version__ = "0.1.0"

from .preprocessing import clean_data
from .train import train_model
from .visualize import (
    plot_loan_status,
    plot_income_distribution,
    plot_credit_history
)
from .utils import evaluate_model, save_results, load_data

__all__ = [
    'clean_data',
    'train_model',
    'plot_loan_status',
    'plot_income_distribution',
    'plot_credit_history',
    'evaluate_model',
    'save_results',
    'load_data'
]