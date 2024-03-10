import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('matplot/customers-100.csv')
plt.boxplot(df['City'])