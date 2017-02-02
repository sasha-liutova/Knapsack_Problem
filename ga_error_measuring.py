import genetic_algorithm

filenames =[("knap_30.inst", "knap_30.sol"),
            ("knap_32.inst", "knap_32.sol"),
            ("knap_35.inst", "knap_35.sol"),
            ("knap_37.inst", "knap_37.sol"),
            ("knap_40.inst", "knap_40.sol")]


def calculate_real_errors():
    result_average = []
    for filename in filenames:
        input_filename, output_filename = "inst/" + filename[0] + ".dat", "sol/" + filename[1] + ".dat"
        function_output = genetic_algorithm.compute(input_filename, False)
        correct_output = []
        with open(output_filename, 'r') as file:
            for line in file:
                correct_output.append(line.rstrip())
        error_sum, error_n = 0, 0
        for function_line, correct_line in zip(function_output, correct_output):
            c_opt = int(correct_line.split()[2])
            c_apx = int(function_line.split()[2])
            error = (c_opt-c_apx)/c_opt
            error_sum += error
            error_n += 1
        average_error = error_sum/error_n
        result_average.append(average_error)
    print('average errors: ', result_average)


def twick_params():
    result_average = []
    filename = ("knap_30.inst", "knap_30.sol")
    input_filename, output_filename = "inst/" + filename[0] + ".dat", "sol/" + filename[1] + ".dat"
    for p in [(x+1)*0.1 for x in range(9)]:
        function_output = genetic_algorithm.twick_params(input_filename, n_iterations=400, n_individuals=60,
                                                         crossover_probability=p, mutation_probability=0.13)
        correct_output = []
        with open(output_filename, 'r') as file:
            for line in file:
                correct_output.append(line.rstrip())
        error_sum, error_n = 0, 0
        for function_line, correct_line in zip(function_output, correct_output):
            c_opt = int(correct_line.split()[2])
            c_apx = int(function_line.split()[2])
            error = (c_opt-c_apx)/c_opt
            error_sum += error
            error_n += 1
        average_error = error_sum/error_n
        print(p, average_error)
        result_average.append((p, average_error))
    print('average errors: ', result_average)

twick_params()

average_errors_per_crossover_probability = [(0.1, 0.11697343543759497), (0.2, 0.09305629019370495),
                                           (0.30000000000000004, 0.08405006064632276), (0.4, 0.06804388000278254),
                                           (0.5, 0.06317313170845935), (0.6000000000000001, 0.05564630036142579),
                                           (0.7000000000000001, 0.05051877764365754), (0.8, 0.05365309404477634),
                                           (0.9, 0.04453185634750257)]
average_errors_per_mutation_probability = [(0.0, 0.06271955986246948), (0.1, 0.0461989764358365), (0.2, 0.05323949675533175),
                                            (0.30000000000000004, 0.05220204903418879), (0.4, 0.047220737854106576),
                                            (0.5, 0.05288846424466906), (0.6000000000000001, 0.04756092436375299),
                                            (0.7000000000000001, 0.050888815593931186), (0.8, 0.05136198627596325),
                                            (0.9, 0.05340420454368023)]
average_errors_per_mutation_probability_2 = [(0.05, 0.053201445147672374), (0.060000000000000005, 0.061279910150043165),
                                             (0.07, 0.050632276265604556), (0.08, 0.049340440664719855), (0.09, 0.05144121494541721),
                                             (0.1, 0.05516019840758686), (0.11, 0.04809587890485576),
                                             (0.12000000000000001, 0.06276034400176844), (0.13, 0.04708866275621098),
                                             (0.14, 0.05482353881557121)]
average_errors_per_n_population = [(100, 0.0997649053390144), (200, 0.05296669775452094), (300, 0.034991283750120415),
                                   (400, 0.02674809381634324), (500, 0.023446717481485534)]
average_errors_per_size_indivizual = [(40, 0.03317353932803003), (50, 0.028917196932337793), (60, 0.0233661090693152),
                                      (70, 0.018657092179974348), (80, 0.016979750322696), (90, 0.018501349415218974),
                                      (100, 0.019654204939680234), (120, 0.019363144097159172)]