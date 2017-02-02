
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

def calculate(input):
    '''
    computes for given parameters the most optimal result using heuristic
    :param input: list of needed parameters: weights, prices, n_items, limit, id
    :return: computed result in str format
    '''
    weights, prices, n_items, limit, id = input[0], input[1], input[2], input[3], input[4]
    weights_and_prices_list = [(weight, price, price/weight) for weight, price in zip(weights, prices)]
    data = [(i, pair) for i, pair in enumerate(weights_and_prices_list)]
    data.sort(key=lambda tup: tup[1][2], reverse=True) # sort by ratio, biggest comes first
    result = [0 for i in range(n_items)]
    weight_sum, price_sum=0,0
    for i in range(n_items):
        position, weight, price = data[i][0], data[i][1][0], data[i][1][1]
        if(weight_sum + weight < limit):
           weight_sum+=weight
           result[position]=1
           price_sum+=price
        else:
            break
    return id + " " + str(n_items) + " " + str(price_sum) + "  " + str(result)[1:-1].replace(',', '')


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

# print(compute("inst/knap_4.inst.dat"))