from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="loan-approval-prediction",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Machine Learning model for loan approval prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/loan-approval-prediction",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=0.24.0",
        "plotly>=5.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "flake8>=3.9",
            "black>=21.0",
        ],
        "viz": [
            "matplotlib>=3.0",
            "seaborn>=0.11",
        ],
    },
    entry_points={
        "console_scripts": [
            "loan-predict=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["data/*.csv"],
    },
)