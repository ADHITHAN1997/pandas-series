import pandas as pd
A = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(A)
print("Change the said data type to numeric:")
B = pd.to_numeric(s1, errors='coerce')
print(B)
