import pandas as pd
import numpy as np
import streamlit as st

# Set seed for reproducibility
np.random.seed(42)

# Number of rows
num_rows = 5

# Generate data
names = [f"Person_{i}" for i in range(1, num_rows+1)]
ages = np.random.randint(20, 60, num_rows)
salaries = np.random.randint(40000, 120000, num_rows)

# Create DataFrame
df = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'Salary': salaries
})

df.to_csv('/tmp/output.csv')

input_form_csv = pd.read_csv('/tmp/output.csv')

st.dataframe(input_form_csv)