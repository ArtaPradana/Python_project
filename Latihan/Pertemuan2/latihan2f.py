# memanggil numpy dan matplotlib
import numpy
import matplotlib.pyplot as plt

# membuat distribusi normal dengan mean=5, stdev=1 dan jumlah data 100.000
x = numpy.random.normal(5.0, 1.0, 100000)
# plotting dengan matplotlib
plt.hist(x, 100)
plt.show()
