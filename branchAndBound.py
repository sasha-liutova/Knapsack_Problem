import copy

current_best = 0

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

def getSum(prices_or_weights, solution):
    sum=0
    for i in range(len(prices_or_weights)):
        if solution[i] == 1:
            sum+=prices_or_weights[i]
    return sum

def getPossibleMax(prices, solution, index):
    remaining_indexes = [index+t for t in range(len(prices)-index)]
    solution2 = copy.deepcopy(solution)
    for x in remaining_indexes:
        solution2[x]=1
    return getSum(prices, solution2)

def calculate_rec(weights, prices, n_items, limit, solution, index):

    global current_best
    weightSum = getSum(weights, solution)

    if(index == 0):
        current_best = 0

    # end of vector reached or weight limit reached
    if (index == n_items and weightSum < limit) or (weightSum == limit):
        price = getSum(prices, solution)
        if price>current_best:
            current_best=price
        return [price, solution]

    # weight limit exceeded
    if weightSum > limit:
        return 0

    # end of vector not reached yet and weights sum are below limit
    if weightSum < limit:

        # check if our solution can possibly be better than current best
        possible_max = getPossibleMax(prices, solution, index)
        if possible_max < current_best:
            return 0

        result1 = calculate_rec(weights, prices, n_items, limit, solution, index + 1)
        solution2 = copy.deepcopy(solution)
        solution2[index] = 1
        result2 = calculate_rec(weights, prices, n_items, limit, solution2, index + 1)
        if result1!=0 and result2!=0 and result1[0] < result2[0]:
            return result2
        elif result1 != 0 and result2 != 0 and result1[0] >= result2[0]:
            return result1
        elif result1!=0:
            return result1
        elif result2!=0:
            return result2
        else:
            return 0


def calculate(input):
    '''
    computes for given parameters the most optimal result using branch&bound algorithm
    :param input: list of needed parameters: weights, prices, n_items, limit, id
    :return: computed result in str format
    '''
    weights, prices, n_items, limit, id = input[0], input[1], input[2], input[3], input[4]
    calculated = calculate_rec(weights, prices, n_items, limit, [0 for x in range(n_items)], 0)
    max_price, max_array = calculated[0], calculated[1]

    return id + " " + str(n_items) + " " + str(max_price) + "  " + str(max_array)[1:-1].replace(',', '')


def compute(filename, first_item_only):
    '''
    :param filename: file to read data from
    :return: list of results in str format
    '''
    result = []
    with open(filename, 'r')as file:
        for line in file:
            item = line.rstrip().split()
            input = preprocess(item)
            output = calculate(input)
            result.append(output)
            if(first_item_only):
                break
    return result

# print(compute("inst/knap_4.inst.dat", first_item_only=False))