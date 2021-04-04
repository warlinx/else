import matplotlib.pyplot as plt

gdp_cap = [10, 14, 12, 13, 8, 16, 15]
life_exp = [7, 3, 5, 6, 5, 4, 8]
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()