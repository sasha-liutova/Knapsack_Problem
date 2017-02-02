import heuristic
import bruteforce
import branchAndBound
import decomposition_by_price
from time import time
import matplotlib.pyplot as plt

max_weights = max_prices = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
capacity_ratios = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
exponents = [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

def form_filenames(dir, values):
    res = []
    for val in values:
        res.append('./data/' + dir + '/file_' + str(val) + '.dat')
    return res

max_weight_files = form_filenames('max_weight', max_weights)
max_price_files = form_filenames('max_price', max_prices)
capacity_ratio_files = form_filenames('capacity_ratio', capacity_ratios)
exponents_gran__1 = form_filenames('exponent_granularity_-1', exponents)
exponents_gran_0 = form_filenames('exponent_granularity_0', exponents)
exponents_gran_1 = form_filenames('exponent_granularity_1', exponents)

def evaluate_error (module, filenames, correct_output):
    errors = []
    index=0
    for filename in filenames:
        function_output = module.compute(filename, False)
        error_sum, error_n=0,0
        for function_line, correct_line in zip(function_output, correct_output[index]):
            c_opt = (int)(correct_line.split()[2])
            c_apx = (int)(function_line.split()[2])
            error = (c_opt-c_apx)/c_opt
            error_sum += error
            error_n += 1
        average_error = error_sum/error_n
        errors.append(average_error)
        index += 1
    return errors

def evaluate_time (module, filenames):
    times = []
    for filename in filenames:
        # print('progress: ', filenames.index(filename), '/', len(filenames))
        t0 = time()
        function_output = module.compute(filename, False)
        execution_time=(time() - t0)/len(function_output)
        times.append(execution_time)
    return times

def get_correct_results(filenames):
    results = []
    for filename in filenames:
        results.append(bruteforce.compute(filename, False))
    return results

def evaluate_algorithm_time (algorithm):
    print(evaluate_time(algorithm, max_weight_files))
    print(evaluate_time(algorithm, max_price_files))
    print(evaluate_time(algorithm, capacity_ratio_files))
    print(evaluate_time(algorithm, exponents_gran__1))
    print(evaluate_time(algorithm, exponents_gran_0))
    print(evaluate_time(algorithm, exponents_gran_1))

def evaluate_algorithm_error (algorithm):
    print(evaluate_error(algorithm, max_weight_files, get_correct_results(max_weight_files)))
    print(evaluate_error(algorithm, max_price_files, get_correct_results(max_price_files)))
    print(evaluate_error(algorithm, capacity_ratio_files, get_correct_results(capacity_ratio_files)))
    print(evaluate_error(algorithm, exponents_gran__1, get_correct_results(exponents_gran__1)))
    print(evaluate_error(algorithm, exponents_gran_0, get_correct_results(exponents_gran_0)))
    print(evaluate_error(algorithm, exponents_gran_1, get_correct_results(exponents_gran_1)))

# evaluate_algorithm_time(branchAndBound)

res_max_weight_bb = [0.006200461387634277, 0.006411600112915039, 0.006280579566955566, 0.0063603782653808595, 0.0061046981811523435, \
                     0.005784482955932617, 0.006093959808349609, 0.005816659927368164, 0.00610569953918457, 0.0053014039993286135]
res_max_price_bb = [0.00568972110748291, 0.005784039497375488, 0.005966095924377441, 0.005546197891235351, 0.005456557273864746, \
                    0.005589561462402344, 0.005709962844848633, 0.005521702766418457, 0.005514020919799805, 0.005849299430847168]
res_capacity_ratio_bb = [0.000993218421936035, 0.002531900405883789, 0.00444364070892334, 0.005521240234375, 0.005867762565612793, \
                         0.005029420852661132, 0.004728517532348633, 0.003927297592163086, 0.003401017189025879, 0.0034045839309692384]
res_exp__1_bb = [0.005394439697265625, 0.006007800102233887, 0.006107277870178222, 0.0067615795135498044, 0.00638956069946289, \
                 0.005537357330322266, 0.00573887825012207, 0.005375280380249024, 0.0048979616165161135, 0.005140724182128906, 0.00489774227142334]
res_exp_0_bb = [0.006469740867614746, 0.006254558563232422, 0.006213383674621582, 0.006262321472167969, 0.006566863059997558, 0.006681361198425293, \
                0.006297321319580078, 0.006456618309020996, 0.006293396949768066, 0.006102700233459473, 0.007141561508178711]
res_exp_1_bb = [0.006198859214782715, 0.005412240028381348, 0.005731000900268555, 0.0055666971206665035, 0.005679459571838379, 0.005628643035888672, \
                0.005548181533813476, 0.005654964447021484, 0.0059192609786987305, 0.005747241973876953, 0.0055370616912841794]

# evaluate_algorithm_time(decomposition_by_price)

res_max_weight_dec = [0.0034239959716796877, 0.0038430213928222655, 0.0038494014739990233, 0.0034927415847778322, 0.0033931398391723634, \
                      0.0037822198867797853, 0.0041261625289916995, 0.0037194395065307615, 0.0037280607223510744, 0.0039991426467895505]
res_max_price_dec =[0.0020001792907714845, 0.003710522651672363, 0.00545297622680664, 0.007551741600036621, 0.009332561492919922, \
                    0.010788540840148925, 0.012484302520751953, 0.014732317924499512, 0.016476120948791504, 0.018393239974975585]
res_capacity_ratio_dec = [0.0036858415603637697, 0.003539419174194336, 0.003500504493713379, 0.003834819793701172, 0.0036202621459960936, \
                          0.0037049007415771483, 0.0038248395919799807, 0.003390402793884277, 0.0035203790664672854, 0.0034896373748779298]
res_exp__1_dec = [0.003355278968811035, 0.003479580879211426, 0.0033677196502685546, 0.0033649778366088867, 0.003352360725402832, 0.0034355211257934572, \
                  0.0033293437957763673, 0.003751683235168457, 0.003827619552612305, 0.0036301565170288085, 0.0035710382461547853]
res_exp_0_dec = [0.004009742736816407, 0.003874979019165039, 0.0038703393936157225, 0.0037146759033203124, 0.0040216207504272464, 0.0039911985397338865, \
                 0.00395899772644043, 0.003450021743774414, 0.00343170166015625, 0.0035274410247802734, 0.0035318422317504885]
res_exp_1_dec = [0.0031584024429321287, 0.003236660957336426, 0.003233199119567871, 0.00339695930480957, 0.0033934593200683595, 0.00338991641998291, \
                 0.003442578315734863, 0.0038529586791992186, 0.0036326026916503906, 0.0035270214080810546, 0.0033157205581665038]

# evaluate_algorithm_time(bruteforce)

res_max_weight_brute = [0.005769138336181641, 0.005879578590393067, 0.00535247802734375, 0.005493316650390625, 0.006251959800720215, \
                        0.00573211669921875, 0.006588759422302246, 0.005767359733581543, 0.005208978652954102, 0.005869617462158203]
res_max_price_brute = [0.005498642921447754, 0.0059107780456542965, 0.005942339897155762, 0.00525212287902832, 0.005243139266967773, \
                       0.005625438690185547, 0.005345578193664551, 0.005180983543395996, 0.005164761543273926, 0.0054610824584960934]
res_capacity_ratio_brute = [0.0048052406311035155, 0.004711999893188477, 0.004980802536010742, 0.005000081062316895, 0.005382919311523437, \
                            0.005820159912109375, 0.005889158248901367, 0.005715417861938477, 0.006046361923217773, 0.006402659416198731]
res_exp__1_brute = [0.006105337142944336, 0.006075081825256348, 0.006189417839050293, 0.006115260124206543, 0.005992860794067383, 0.006327238082885742, \
                    0.0060163593292236325, 0.005366039276123047, 0.005215363502502441, 0.005448899269104004, 0.005477619171142578]
res_exp_0_brute = [0.0057327175140380856, 0.005499258041381836, 0.005992741584777832, 0.006371841430664062, 0.006322617530822754, 0.006009278297424317, \
                   0.006621179580688477, 0.006079840660095215, 0.006204638481140137, 0.006297240257263184, 0.005877919197082519]
res_exp_1_brute = [0.005938801765441894, 0.005890922546386719, 0.005965337753295898, 0.005888876914978028, 0.006191582679748535, 0.0054803800582885745, \
                   0.006179380416870117, 0.006348299980163574, 0.005817279815673828, 0.006176896095275879, 0.0063328218460083005]

# evaluate_algorithm_time(heuristic)

res_max_weight_heur = [2.6717185974121094e-05, 2.451896667480469e-05, 2.4700164794921874e-05, 2.451896667480469e-05, 2.441883087158203e-05, \
                       2.7942657470703126e-05, 2.8438568115234375e-05, 2.4003982543945314e-05, 2.5177001953125e-05, 2.38800048828125e-05]
res_max_price_heur = [2.4499893188476564e-05, 2.468109130859375e-05, 2.3598670959472657e-05, 2.5119781494140625e-05, 2.3679733276367186e-05, \
                      2.3779869079589843e-05, 2.3679733276367186e-05, 2.51007080078125e-05, 2.7561187744140624e-05, 3.0102729797363282e-05]
res_capacity_ratio_heur = [2.414226531982422e-05, 2.6259422302246094e-05, 2.6917457580566408e-05, 2.605915069580078e-05, 2.463817596435547e-05, \
                           2.3641586303710937e-05, 2.434253692626953e-05, 2.4700164794921874e-05, 2.4280548095703126e-05, 2.4538040161132813e-05]
res_exp__1_heur = [4.3439865112304685e-05, 3.859996795654297e-05, 3.387928009033203e-05, 3.370285034179688e-05, 3.103733062744141e-05, 2.9978752136230468e-05, \
                   2.7918815612792967e-05, 2.7136802673339842e-05, 2.5196075439453127e-05, 2.3975372314453126e-05, 2.448081970214844e-05]
res_exp_0_heur = [2.372264862060547e-05, 2.4061203002929688e-05, 2.5177001953125e-05, 2.2716522216796875e-05, 2.2635459899902343e-05, 2.26593017578125e-05, \
                  2.2559165954589845e-05, 2.3922920227050782e-05, 2.2759437561035155e-05, 2.26593017578125e-05, 2.2664070129394532e-05]
res_exp_1_heur = [2.3360252380371095e-05, 2.513885498046875e-05, 2.371788024902344e-05, 2.2840499877929687e-05, 2.3622512817382812e-05, 2.270221710205078e-05, \
                  2.2816658020019532e-05, 2.3617744445800782e-05, 5.0201416015625e-05, 4.5957565307617185e-05, 3.384113311767578e-05]

# evaluate_algorithm_error(heuristic)

res_max_weight_heur_error = [0.032864105352368674, 0.028063048301482228, 0.024677833243716994, 0.03736104700977448, 0.01747591191209747, \
                            0.03565154093823641, 0.03206259309559651, 0.04445289017230304, 0.035435994231441996, 0.03251398012099129]
res_max_price_heur_error = [0.03859198840685714, 0.04931719304214533, 0.04410081942682897, 0.031932425561797276, 0.031690390025222205, \
                            0.027553641522416815, 0.03288986928743147, 0.02836815886616008, 0.05247267856973978, 0.040251336356262664]
res_capacity_ratio_heur_error = [0.12226686413501005, 0.06935789706144443, 0.0683984115011919, 0.053919091357197454, 0.032318598055873456, \
                                 0.027925739239804227, 0.021436809695636157, 0.00879271744965472, 0.0046370207684966035, 0.026253800947191472]
res_exp__1_heur_error = [0.046816833652124246, 0.046816833652124246, 0.046816833652124246, 0.04546749932745833, 0.04546749932745833, 0.046816833652124246, \
                         0.037281483777063855, 0.023129290705449, 0.03979320819558932, 0.024630142812359132, 0.032869013025327055]
res_exp_0_heur_error = [0.03714130243959321, 0.03714130243959321, 0.03714130243959321, 0.036171025618570114, 0.036171025618570114, 0.03714130243959321, \
                        0.036171025618570114, 0.036171025618570114, 0.036171025618570114, 0.03714130243959321, 0.03714130243959321]
res_exp_1_heur_error = [0.030649754498589536, 0.03282952305405642, 0.03282952305405642, 0.03231397857507489, 0.03282952305405642, 0.03231397857507489, \
                        0.03580894927152199, 0.035367633348777135, 0.02932364450130827, 0.03954902625388588, 0.035922831357371]


def plot_data(x, y, label_x, label_y, title):
    maximum = max(y)
    minimum = min(y)
    step = (maximum - minimum) / 5

    for xi, yi in zip(x, y):
        plt.scatter(xi, yi)

    plt.ylim(minimum - step, maximum + step)

    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
    plt.show()

# plot_data(max_weights, res_max_weight_heur_error, 'Max weight', 'Error', 'Heuristic function')
# plot_data(max_prices, res_max_price_heur_error, 'Max price', 'Error', 'Heuristic function')
# plot_data(capacity_ratios, res_capacity_ratio_heur_error, 'Capacity ratio', 'Error', 'Heuristic function')
# plot_data(exponents, res_exp__1_heur_error, 'Exponent (granularity = -1)', 'Error', 'Heuristic function')
# plot_data(exponents, res_exp_0_heur_error, 'Exponent (granularity = 0)', 'Error', 'Heuristic function')
# plot_data(exponents, res_exp_1_heur_error, 'Exponent (granularity = 1)', 'Error', 'Heuristic function')

def plot_param (input, x, x_label, y_label, labels, scale):
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
        plt.scatter(x[0], time_list[0], color=colors[index], label=labels[index])
        for i in range(1, size):
            plt.scatter(x[i], time_list[i], color=colors[index])
        index+=1

    legend = ax.legend(loc='upper center')
    frame = legend.get_frame()
    frame.set_facecolor('0.90')
    for label in legend.get_texts():
        label.set_fontsize('medium')
    for label in legend.get_lines():
        label.set_linewidth(1.5)

    plt.ylim(minimum - step, maximum + step*5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# plot_param ([res_max_weight_brute, res_max_weight_bb, res_max_weight_dec, res_max_weight_heur],
#             max_weights, 'Maximum weight', 'Time [s]',
#             ['Brute force', 'Branch & Bound', 'Decomposition by price', 'Heuristic function'], 'linear')
# plot_param ([res_max_price_brute, res_max_price_bb, res_max_price_dec, res_max_price_heur],
#             max_prices, 'Maximum price', 'Time [s]',
#             ['Brute force', 'Branch & Bound', 'Decomposition by price', 'Heuristic function'], 'linear')
# plot_param ([res_capacity_ratio_brute, res_capacity_ratio_bb, res_capacity_ratio_dec, res_capacity_ratio_heur],
#             capacity_ratios, 'Capacity ratio', 'Time [s]',
#             ['Brute force', 'Branch & Bound', 'Decomposition by price', 'Heuristic function'], 'linear')
# plot_param ([res_exp__1_brute, res_exp__1_bb, res_exp__1_dec, res_exp__1_heur],
#             exponents, 'Exponent (granularity = -1)', 'Time [s]',
#             ['Brute force', 'Branch & Bound', 'Decomposition by price', 'Heuristic function'], 'linear')
# plot_param ([res_exp_0_brute, res_exp_0_bb, res_exp_0_dec, res_exp_0_heur],
#             exponents, 'Exponent (granularity = 0)', 'Time [s]',
#             ['Brute force', 'Branch & Bound', 'Decomposition by price', 'Heuristic function'], 'linear')
# plot_param ([res_exp_1_brute, res_exp_1_bb, res_exp_1_dec, res_exp_1_heur],
#             exponents, 'Exponent (granularity = 1)', 'Time [s]',
#             ['Brute force', 'Branch & Bound', 'Decomposition by price', 'Heuristic function'], 'linear')