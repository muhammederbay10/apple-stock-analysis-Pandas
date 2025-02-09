import pandas as pd
import matplotlib.pyplot as plt

apple_stck_price = pd.read_csv(r'C:\Users\moham\Downloads\aAPL_historical_data.csv')

print(apple_stck_price.head())

apple_stck_price["Stock Mean"] = apple_stck_price[["Open", "High", "Low", "Close"]].mean(axis=1)

print(apple_stck_price.head())

print(apple_stck_price.describe)

print(apple_stck_price.loc[4000])

print(apple_stck_price.iloc[4000])

def check():

    if (apple_stck_price["Open"] > 1).any():

        print(apple_stck_price["Open"])

    else:
        print("The open stock price is less than 1$")

check()    

# print(apple_stck_price["Open"].plot())
# plt.show()

print(apple_stck_price.sample(frac = 0.2))