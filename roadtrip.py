import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


# Store data from spreadsheet into a Pandas dataframe
# Note that we usually place the response variable as the final column in a dataframe.
data = {"Kms": [390.0,
              403.0,
              396.5,
              383.5,
              321.1,
              391.3,
              386.1,
              371.8,
              404.3,
              392.6,
              386.49,
              395.2,
              385.5,
              372.0,
              397.0,
              407.0,
              372.33,
              375.6,
              399.0],
        "Dollars":[36.66, 
                 37.05, 
                 34.71, 
                 32.5, 
                 32.63, 
                 34.45,
                 36.79,
                 37.44,
                 38.09,
                 38.09,
                 38.74,
                 39.0,
                 40.0,
                 36.21,
                 34.05,
                 41.79,
                 30.25,
                 38.83,
                 39.66]
      }

df = pd.DataFrame(data)


# Plot data points as a scatterplot 
plt.scatter(df["Kms"], df["Dollars"])
plt.title("Total Kms driven vs. Total paid for petrol")
plt.xlabel("Total driven (Kms)")
plt.ylabel("Total paid (Australian dollars)")
plt.grid()
plt.show()


# Build a simple linear regression model
# First, separate explanatory variables (x) from the response variable (y)
x = df.iloc[:,:-1].values
y = df.iloc[:,1].values


# Model 1 #
# Initialise a linear regression model (with intercept)
model = LinearRegression()

# Fit the linear regression model on the data
model.fit(x, y)

# Get the intercept and coefficient values
intercept = model.intercept_
coeff_intercept = model.coef_ 
print("Model with intercept:")
print("Intercept: ", intercept)
print("Coefficient: ", coeff_intercept)

# Visualise the regression line over all data points
x_line1 = df.iloc[:,0].values
y_line1 = x_line1 * coeff_intercept + intercept

plt.scatter(df["Kms"], df["Dollars"])
plt.title("Total Kms driven vs. Total paid for petrol")
plt.xlabel("Total driven (Kms)")
plt.ylabel("Total paid (Australian dollars)")
plt.plot(x_line1, y_line1, ":g", label="y=8.3257 + 0.0735*x")
plt.legend(loc='upper left')
plt.grid()
plt.show()


# Model 2 #
# Initialise a linear regression model (no intercept)
model2 = LinearRegression(fit_intercept=False)

# Fit the linear regression model on the data
model2.fit(x, y)

# Print the intercept and coefficient learned by the linear regression model
intercept_zero = 0
coeff_nointercept = model2.coef_ 
print("Model without intercept:")
print("Intercept: ", intercept_zero)
print("Coefficient: ", coeff_nointercept)

# Visualise the 2nd regression line over all data points
# Include the first regression line for easy comparison.
x_line2 = df.iloc[:,0].values
y_line2 = x_line2 * coeff_nointercept + intercept_zero

plt.scatter(df["Kms"], df["Dollars"])
plt.title("Total Kms driven vs. Total paid for petrol")
plt.xlabel("Total driven (Kms)")
plt.ylabel("Total paid (Australian dollars)")
plt.plot(x_line1, y_line1, ":g", label="y=8.3257 + 0.0735*x")
plt.plot(x_line2, y_line2, ":r", label="y=0.0 + 0.0950*x")
plt.legend(loc='upper left')
plt.grid()
plt.show()













