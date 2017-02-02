import math
import random
import copy
import matplotlib.pyplot as plt

def preprocess(item):
    '''
    :param item: str line from input file
    :return: list of parameters extracted from item
    '''
    id, n, M = item[0], int(item[1]), int(item[2])
    del item[:3]
    weights, prices, switch = [], [], True
    for i in range(len(item)):
        if switch:
            weights.append(int(item[i]))
        else:
            prices.append(int(item[i]))
        switch = not switch
    return([weights, prices, n, M, id])


def compute(filename, first_item_only):
    """
    :param filename: file to read data from
    :param first_item_only: compute only first instance (True) or all (False)
    :return: list of results in str format
    """
    result = []
    with open(filename, 'r')as file:
        for line in file:
            item = line.rstrip().split()
            input = preprocess(item)
            output = calculate(input, n_iterations=400, n_individuals=70, crossover_probability=0.7, mutation_probability=0.13)
            result.append(output)
            if first_item_only:
                break
    return result

def inicialize_population(n_individuals, length, weights, limit):
    """
    inicializes population with random values
    :param n_individuals: size of population
    :param length: size of individual (vector)
    :return: list of vectors with 0's and 1's
    """
    population = []
    while len(population) < n_individuals:
        individual = []
        for j in range(length):
            individual.append(random.getrandbits(1))
        if(is_valid(individual, weights, limit)):
            population.append(individual)
    return population


def fitness(individual, prices):
    sum = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            sum += prices[i]
    return sum


def selection(population, prices):

    # calculating fitness function for each individual
    fitnesses = [fitness(individual, prices) for individual in population]
    # print('fitness function: ', fitnesses)

    # generating roulette based on fitness values
    roulette, index = [], 0
    for f in fitnesses:
        for i in range(f):
            roulette.append(index)
        index += 1

    # selecting individuals
    population_new = []
    for i in range(len(population)):
        value = random.randint(0, len(roulette) - 1)
        number_of_individual = roulette[value]
        individual = population[number_of_individual]
        # print('chosen #', number_of_individual, ' ', individual)
        population_new.append(individual)

    # print('selected population: ', population_new)
    return population_new


def is_valid(individual, weights, limit):
    sum = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            sum += weights[i]
    if sum > limit:
        return False
    else:
        return True


def crossover_pair(individual1, individual2, weights, limit):
    if individual1 == individual2:
        return [individual1, individual2]
    counter = 0
    while True:
        point = random.randint(0,len(individual1)-1)
        individual1_new = individual1[:point] + individual2[point:]
        individual2_new = individual2[:point] + individual1[point:]
        if is_valid(individual1_new, weights, limit) and is_valid(individual2_new, weights, limit):
            # print('crossed over ', individual1, individual2, ' -> ', individual1_new, individual2_new)
            return [individual1_new, individual2_new]
        if counter > len(individual1) * 2:
            return [individual1, individual2]
        counter += 1


def crossover_population(population, weights, limit, probability):
    population_new = []
    for i in range(int(len(population)/2)):
        number = random.random()
        if number < probability:
            population_new.extend(crossover_pair(population[i], population[i+1], weights, limit))
        else:
            population_new.extend([population[i], population[i + 1]])
    if len(population_new) < len(population):
        population_new.append(population[-1])
    # print('crossed over population: ', population_new)
    return population_new


def flip(n):
    if n == 0:
        return 1
    else:
        return 0


def mutation_individual(individual, weights, limit):
    counter = 0
    while True:
        index = random.randint(0, len(individual) - 1)
        individual_new = copy.deepcopy(individual)
        individual_new[index] = flip(individual_new[index])
        if is_valid(individual_new, weights, limit):
            # print('mutation: ', individual, ' -> ', individual_new)
            return individual_new
        if counter > len(individual)*2:
            return individual
        counter += 1


def mutation_population(population, weights, limit, probability):
    number = random.random()
    if number < probability:
        index = random.randint(0, len(population) - 1)
        population[index] = mutation_individual(population[index], weights, limit)
    return population


def get_statistics(population, prices):
    fitnesses = [fitness(individual, prices) for individual in population]
    return {'min': min(fitnesses), 'max': max(fitnesses), 'avg': sum(fitnesses) / float(len(fitnesses))}


def get_best_individual(population, prices):
    fitnesses = [fitness(individual, prices) for individual in population]
    best_price = max(fitnesses)
    index = fitnesses.index(best_price)
    best_individual = population[index]
    return {'individual': best_individual, 'price': best_price}



def plot_statistics(statistics):

    values_max = [x['max'] for x in statistics]
    values_min = [x['min'] for x in statistics]

    maximum = max(values_max)
    minimum = min(values_min)
    step = (maximum-minimum)/5

    counter = 0
    for item in statistics:
        plt.scatter(counter, item['max'], color='green', s=2)
        plt.scatter(counter, item['min'], color='red', s=2)
        plt.scatter(counter, item['avg'], color='yellow', s=2)
        counter += 1

    plt.ylim(minimum-step, maximum+step)

    plt.xlabel('# population')
    plt.ylabel('optimization criterion')
    plt.show()


def calculate(input, n_individuals, n_iterations, crossover_probability, mutation_probability):
    weights, prices, n_items, limit, id = input[0], input[1], input[2], input[3], input[4]

    population = inicialize_population(n_individuals, n_items, weights, limit)
    # print('Initial population: ', population)
    statistics = [get_statistics(population, prices)]
    for iteration in range(n_iterations):
        # print('iteration ', iteration+1)
        population = selection(population, prices)
        population = crossover_population(population, weights, limit, crossover_probability)
        population = mutation_population(population, weights, limit, mutation_probability)

        # optional for investigation
        # current_statistics = get_statistics(population, prices)
        # statistics.append(current_statistics)

    # optional
    # plot_statistics(statistics)

    solution = get_best_individual(population, prices)
    return id + " " + str(n_items) + " " + str(solution['price']) + "  " + str(solution['individual'])[1:-1].replace(',', '')


# print (calculate([[18, 42, 88, 3] , [114, 136, 192, 223], 4, 100, '9000'], 10, 30, 0.5, 0.8))
# print (calculate([[22, 4, 2, 7, 26, 6, 1, 16, 43, 15, 40, 21, 3, 19, 48, 18, 49, 8, 41, 27] ,
#                   [175, 131, 30, 11, 135, 71, 249, 141, 138, 164, 252, 172, 9, 88, 70, 42, 146, 182, 68, 67],
#                   20, 250, '9150'], n_individuals=50, n_iterations=200, crossover_probability=0.3, mutation_probability=0.1))

def twick_params (filename, n_iterations, n_individuals, crossover_probability, mutation_probability):
    """
    :param filename: file to read data from
    :param first_item_only: compute only first instance (True) or all (False)
    :return: list of results in str format
    """
    result = []
    with open(filename, 'r')as file:
        for line in file:
            item = line.rstrip().split()
            input = preprocess(item)
            output = calculate(input, n_iterations, n_individuals, crossover_probability, mutation_probability)
            result.append(output)
    return result