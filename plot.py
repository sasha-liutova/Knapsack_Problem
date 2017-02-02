import heuristic
import bruteforce
from time import time
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import timeit
import branchAndBound
import decomposition_by_price
import fptas
import genetic_algorithm

module = genetic_algorithm

filenames=[#("knap_4.inst", "knap_4.sol"),
        # ("knap_10.inst", "knap_10.sol"),
        # ("knap_15.inst", "knap_15.sol"),
        # ("knap_20.inst", "knap_20.sol"),
        # ("knap_22.inst", "knap_22.sol"),
        # ("knap_25.inst", "knap_25.sol"),
        # ("knap_27.inst", "knap_27.sol"),
        ("knap_30.inst", "knap_30.sol"),
        ("knap_32.inst", "knap_32.sol"),
        ("knap_35.inst", "knap_35.sol"),
        ("knap_37.inst", "knap_37.sol"),
        ("knap_40.inst", "knap_40.sol")]

# n_items_list=[4,10,15,20,22,25,27,30,32,35,37,40]
n_items_list=[30,32,35,37,40]


def compute_and_measure():
    '''
    this function goes through all files in 'filenames',
    calls compute function for each file
    and measures execution time
    '''
    time_array=[]
    for filename in filenames:
        input_filename = "inst/" + filename[0] + ".dat"
        t0 = time()
        # for i in range(100):
        module.compute(input_filename, False)
        # execution_time=(time() - t0)/100
        execution_time=(time() - t0)/50 # to remove
        print(input_filename, ": ", execution_time, "s")
        time_array.append(execution_time)

    print(time_array)
    return time_array


heuristic_times = [2.005577087402344e-05, 2.0046234130859375e-05, 4.009723663330078e-05,
                   6.015777587890625e-05, 4.011154174804688e-05, 4.0106773376464843e-05,
                   8.022308349609375e-05, 6.014823913574219e-05, 8.021354675292969e-05,
                   8.022308349609375e-05, 6.015300750732422e-05, 0.0001002645492553711]
bruteforce_times = [0.0001709461212158203, 0.005635976791381836, 0.2832798957824707,
                    11.443778038024902, 52.36095905303955, 418.48946499824524,
                    2516.797786951065]
decomposition_times = [0.0018309903144836425, 0.006576669216156006, 0.02592468023300171,
                       0.031094989776611327, 0.04452325105667114, 0.045320188999176024,
                       0.07419995784759521, 0.06149864912033081, 0.08398935794830323,
                       0.1025024700164795, 0.12450228929519654, 0.11403974056243897]
fptas_times = [0.00038859844207763674, 0.002823770046234131, 0.014538578987121582,
               0.024073519706726075, 0.03790639877319336, 0.04533541917800903,
               0.0773849892616272, 0.07279804944992066, 0.1095798683166504,
               0.14116930961608887, 0.1794053602218628, 0.18901655912399293]
branch_and_bound_times_OLD = [0.00021354913711547853, 0.017455320358276367, 1.0178715586662292,
                          38.09934616088867, 171.27201581001282, 1429.8650159835815]
branch_and_bound_times = [0.0003005361557006836, 0.004913406372070312, 0.0343262791633606,
                          0.5493367052078247, 0.20151611804962158, 4.192444422245026,
                          15.237244827747345]
ga_times = [0.1090716028213501, 0.12713141918182372, 0.12877163887023926, 0.1294948434829712, 0.14116404056549073]


def plot(time_list):
    maximum = max(time_list)
    minimum = min(time_list)
    step = (maximum-minimum)/5

    for time, n_items in zip(time_list, n_items_list):
        plt.scatter(n_items, time)
    # plt.plot(n_items_list[:len(time_list)], time_list)

    plt.ylim(minimum-step, maximum+step)

    plt.xlabel('N')
    plt.ylabel('time [s]')
    plt.show()

def plotComparisonTwo(time_list1, time_list2):
    maximim = max([max(time_list1),max(time_list2)])
    minimum = min([min(time_list1),min(time_list2)])
    step = (maximim - minimum) / 5
    size = min(len(time_list1), len(time_list2))

    for index in range(0, size):
        plt.scatter(n_items_list[index], time_list1[index], color='red')
        plt.scatter(n_items_list[index], time_list2[index], color='blue')

    plt.plot(n_items_list[:size], time_list1[:size], color='red')
    plt.plot(n_items_list[:size], time_list2[:size], color='blue')

    plt.ylim(minimum - step, maximim + step)

    plt.xlabel('N')
    plt.ylabel('time [s]')
    plt.show()

def plotComparisonMultiple(input, labels, scale):
    colors=['red', 'blue', 'green', 'yellow', 'orange', 'black']
    if(len(input) > len(colors)):
        return

    maximum = max([max(i) for i in input])
    minimum = min([min(i) for i in input])
    step = (maximum - minimum) / 5
    if scale == 'log':
        step *= 100
    size = min([len(i) for i in input])

    index, lines=0,[]
    fig, ax = plt.subplots()
    ax.set_yscale(scale)
    for time_list in input:
        plt.scatter(n_items_list[0], time_list[0], color=colors[index], label=labels[index])
        for i in range(1, size):
            plt.scatter(n_items_list[i], time_list[i], color=colors[index])
        index+=1

    legend = ax.legend(loc='upper center')
    frame = legend.get_frame()
    frame.set_facecolor('0.90')
    for label in legend.get_texts():
        label.set_fontsize('medium')
    for label in legend.get_lines():
        label.set_linewidth(1.5)

    plt.ylim(minimum - step, maximum + step)
    plt.xlabel('N')
    plt.ylabel('time [s]')
    plt.show()


# plot(ga_times)
# plot(bruteforce_times)
# plotComparison(bruteforce_times, heuristic_times)

# plotComparisonMultiple([bruteforce_times, branch_and_bound_times, decomposition_times, fptas_times],
#      ['Brute force', 'Branch & Bound', 'Decomposition by price', 'FPTAS'], 'log')

ga_times = compute_and_measure()
plot(ga_times)
