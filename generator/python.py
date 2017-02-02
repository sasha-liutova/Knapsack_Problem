import subprocess
import os

n_things = 10
n_instances = 50
capacity_ratio = 0.5 # pozorovat 0.1 - 1
max_weight = 100 # pozorovat 50-500
max_price = 100 # pozorovat 50-500
exponent = 0.5 # -1 - 1
granularity = 1 # pozorovat -1/0/1

max_weight_range = max_price_range = [(i+1)*50 for i in range(10)]
capacity_ratio_range = [(i+1)*0.1 for i in range(10)]
exponent_range = [i*0.2-1 for i in range(11)]

for exponent in exponent_range:
	filename = "file_" + str(exponent) + ".dat"
	newpath = './data10/exponent_granularity_1/'
	if not os.path.exists(newpath):
	    os.makedirs(newpath)

	file = open(newpath + filename, "w")

	subprocess.Popen(["./a.out",
		"-n", str(n_things),
		"-N", str(n_instances),
		"-m", str(capacity_ratio),
		"-W", str(max_weight),
		"-C", str(max_price),
		"-k", str(exponent),
		"-d", str(granularity)],
		stdout = file)

