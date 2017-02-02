import math

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

def inicialize_table(n, prices_sum):
    table = [[0 for x in range(prices_sum + 1)] for x in range(n + 1)]
    table[0] = [math.inf for x in range(prices_sum + 1)]
    table[0][0] = 0
    return table

def calculate(input, e):
    '''
    computes for given parameters the most optimal result using FPTAS
    :param input: list of needed parameters: weights, prices, n_items, limit, id
    :return: computed result in str format
    '''
    weights, raw_prices, n_items, limit, id = input[0], input[1], input[2], input[3], input[4]

    #FPTAS part
    prices_max = max(raw_prices)
    k = e*prices_max/n_items
    prices = [int(x/k) for x in raw_prices]


    # constructing table with dinamic programming
    prices_sum=sum(prices)
    table = inicialize_table(n_items, prices_sum)
    for column in [x+1 for x in range(n_items)]:
        for row in [x + 1 for x in range(prices_sum)]:
            c=prices[column-1]
            w=weights[column-1]
            val_near = table[column-1][row]
            if (row-c)<0:
                val_up=math.inf
            else:
                val_up=table[column-1][row-c]
            table[column][row]=min(val_near, val_up+w)

    #go throgh last column and find w<M
    for i in [prices_sum-x for x in range(prices_sum+1)]:
        if table[n_items][i] <= limit:
            max_price = i
            break

    # construct max_array
    max_array=[0 for x in range(n_items)]
    row=max_price
    for column in [n_items-x for x in range(n_items)]:
        c = prices[column-1]
        w = weights[column - 1]
        val_current = table[column][row]
        val_near = table[column-1][row]
        val_up = table[column - 1][row - c]
        if val_current==val_near:
            max_array[column-1]=0
        if val_current==(val_up+w):
            max_array[column-1]=1
            row = row-c

    max_price=0
    for pair in [[price, condition] for price, condition in zip(raw_prices, max_array)]:
        if(pair[1]==1):
            max_price+=pair[0]

    return id + " " + str(n_items) + " " + str(max_price) + "  " + str(max_array)[1:-1].replace(',', '')


def compute(filename, first_item_only, error):
    '''
    :param filename: file to read data from
    :return: list of results in str format
    '''
    result = []
    with open(filename, 'r')as file:
        for line in file:
            item = line.rstrip().split()
            input = preprocess(item)
            output = calculate(input, error)
            result.append(output)
            if(first_item_only):
                break
    return result

# print(compute("inst/knap_4.inst.dat", first_item_only=False))