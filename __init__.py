from utils import *

df = pd.read_csv('coins.csv')

print(df['Close'].values)
