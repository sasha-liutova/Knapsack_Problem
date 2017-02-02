import matplotlib.pyplot as plt
import fptas
from time import time

errors=[0.01, 0.05, 0.1, 0.15, 0.25, 0.4, 0.5]

def calculate_real_errors():
    result_average, result_max=[],[]
    filename = ("knap_15.inst", "knap_15.sol", 15)
    input_filename, output_filename = "inst/" + filename[0] + ".dat", "sol/" + filename[1] + ".dat"
    for e in errors:
        function_output = fptas.compute(input_filename, False, e)
        correct_output = []
        with open(output_filename, 'r') as file:
            for line in file:
                correct_output.append(line.rstrip())
        error_sum, error_n, error_max= 0, 0, 0
        for function_line, correct_line in zip(function_output, correct_output):
            c_opt = (int)(correct_line.split()[2])
            c_apx = (int)(function_line.split()[2])
            error = (c_opt-c_apx)/c_opt
            error_sum+=error
            error_n+=1
            if(error>error_max):
                error_max=error
        average_error = error_sum/error_n
        result_average.append([e, average_error])
        result_max.append([e, error_max])
    print('average errors: ', result_average)
    print('maximal errors: ', result_max)

max_errors = [[0.01, 0], [0.05, 0], [0.1, 0.000724112961622013], [0.15, 0.0015698587127158557],
              [0.25, 0.003357582540570789], [0.4, 0.0028749401054144704], [0.5, 0.004917025199754148]]

def calculate_runtime():
    time_array = []
    filename = ("knap_15.inst", "knap_15.sol", 15)
    for e in errors:
        input_filename = "inst/" + filename[0] + ".dat"
        t0 = time()
        for i in range(100):
            fptas.compute(input_filename, False, e)
        execution_time = (time() - t0) / 100 /50 # 100 times, 50 instances
        time_array.append([e, execution_time])
        print(e, ": ", execution_time, "s")
    print(time_array)

runtimes=[[0.01, 0.15634798526763916], [0.05, 0.030872454643249513], [0.1, 0.015250535011291503],
          [0.15, 0.010135569572448731], [0.25, 0.005866279602050781], [0.4, 0.0035594701766967773], [0.5, 0.0030081939697265627]]

def plotGraph(data, y_axis):
    maximum = max([x[1] for x in data])
    minimum = min([x[1] for x in data])
    step = (maximum-minimum)/5

    for point in data:
        plt.scatter(point[0], point[1])
    # plt.plot(errors, [x[1] for x in data])

    plt.ylim(minimum-step, maximum+step)

    plt.xlabel('Set error')
    plt.ylabel(y_axis)
    plt.show()

# calculate_real_errors()
# plotGraph(max_errors, 'Maximal relative error')
# calculate_runtime()
plotGraph(runtimes, 'Average runtime [s]')