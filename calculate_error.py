import heuristic
import matplotlib.pyplot as plt

filenames=[("knap_4.inst", "knap_4.sol", 4),
        ("knap_10.inst", "knap_10.sol", 10),
        ("knap_15.inst", "knap_15.sol", 15),
        ("knap_20.inst", "knap_20.sol", 20),
        ("knap_22.inst", "knap_22.sol", 22),
        ("knap_25.inst", "knap_25.sol", 25),
        ("knap_27.inst", "knap_27.sol", 27),
        ("knap_30.inst", "knap_30.sol", 30),
        ("knap_32.inst", "knap_32.sol", 32),
        ("knap_35.inst", "knap_35.sol", 35),
        ("knap_37.inst", "knap_37.sol", 37),
        ("knap_40.inst", "knap_40.sol", 40)]

def calculate_errors():
    result_average, result_max=[],[]
    for filename in filenames:
        input_filename, output_filename = "inst/" + filename[0] + ".dat", "sol/" + filename[1] + ".dat"
        function_output = heuristic.compute(input_filename, False)
        correct_output = []
        with open(output_filename, 'r') as file:
            for line in file:
                correct_output.append(line.rstrip())
        error_sum, error_n, error_max=0,0,0
        for function_line, correct_line in zip(function_output, correct_output):
            c_opt = (int)(correct_line.split()[2])
            c_apx = (int)(function_line.split()[2])
            error = (c_opt-c_apx)/c_opt
            error_sum+=error
            error_n+=1
            if(error>error_max):
                error_max=error
        average_error = error_sum/error_n
        result_average.append([filename[2], average_error])
        result_max.append([filename[2], error_max])
    print(result_average)
    print(result_max)

result_errors_average = [[4, 0.08159994043482], [10, 0.03779275900134663], [15, 0.009673343067280276], [20, 0.014227549644495067],
[22, 0.017292535948782675], [25, 0.013678302803203802], [27, 0.011185503849476109], [30, 0.010693825806338136],
[32, 0.0075559034137441606], [35, 0.011878296727568769], [37, 0.0076777704556048884], [40, 0.006926520942449999]]
result_errors_max = [[4, 0.6836734693877551], [10, 0.22362052274927396], [15, 0.08542713567839195], [20, 0.08433734939759036],
                     [22, 0.08752475247524752], [25, 0.054243542435424355], [27, 0.10601719197707736], [30, 0.05513784461152882],
                     [32, 0.036118003859939345], [35, 0.04609218436873747], [37, 0.08196721311475409], [40, 0.025724874645737954]]

def plot_errors(error_list):
    maximim = max([x[1] for x in error_list])
    minimum = min([x[1] for x in error_list])
    step = (maximim - minimum) / 5

    plt.scatter([x[0] for x in error_list], [x[1] for x in error_list])
    plt.plot([x[0] for x in error_list], [x[1] for x in error_list])

    plt.ylim(minimum - step, maximim + step)

    plt.xlabel('N')
    plt.ylabel('relative error')
    plt.show()

def errorComparison(error_list1, error_list2):
    maximim = max(max([x[1] for x in error_list1]), max([x[1] for x in error_list2]))
    minimum = min(min([x[1] for x in error_list1]), min([x[1] for x in error_list2]))
    step = (maximim - minimum) / 5

    plt.scatter([x[0] for x in error_list1], [x[1] for x in error_list1], color='red')
    plt.plot([x[0] for x in error_list1], [x[1] for x in error_list1], color='red')

    plt.scatter([x[0] for x in error_list2], [x[1] for x in error_list2], color='blue')
    plt.plot([x[0] for x in error_list2], [x[1] for x in error_list2], color='blue')

    plt.ylim(minimum - step, maximim + step)

    plt.xlabel('N')
    plt.ylabel('relative error')
    plt.show()

# calculate_errors()
# plot_errors(result_errors_max)
errorComparison(result_errors_max, result_errors_average)