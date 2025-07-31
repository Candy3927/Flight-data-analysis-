import statistics as stats
import numpy as np

# mean
sample = [100, 115, 93, 102, 297]
x_bar = stats.mean(sample)
print("Mean:", x_bar)

# median
sample = [15, 10, 6, 5, 3, 1]
median = stats.median(sample)
print("Median: %.2f" % median)

# mode
sample = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
mode = stats.mode(sample)
print("Mode value: %d" % mode)


# range
sample = [100, 115, 93, 102, 297]
the_range = np.max(sample) - np.min(sample)
print("Range: %d" % the_range)

# sample and population variance
sample = np.array([1, 2, 3, 4, 5])
s_square = sample.var(ddof=1)
sigma_square = sample.var()
print("Sample variance: %.2f. Population variance: %.2f." % (s_square, sigma_square))

# sample and population standard deviation
s = sample.std(ddof=1)
sigma = sample.std()
print("Sample std. dev.: %.2f. Population std. dev.: %.2f." % (s, sigma))

# iqr and percentiles
sample = [1, 2, 3, 5, 7, 8, 11, 12, 15, 15, 18, 18, 20]
pct25 = np.percentile(sample, 25)
pct75 = np.percentile(sample, 75)
iqr = pct75 - pct25
print("IQR: %d. 25th percentile: %d. 75th percentile: %d" % (iqr, pct25, pct75))