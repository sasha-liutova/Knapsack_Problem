import itertools

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
    computes for given parameters the most optimal result using bruteforce
    :param input: list of needed parameters: weights, prices, n_items, limit, id
    :return: computed result in str format
    '''
    weights, prices, n_items, limit, id = input[0], input[1], input[2], input[3], input[4]
    max_price, max_array=0,None
    for binary_array in [ [int(i) for i in list('{:0{}b}'.format(i, n_items))] for i in range(1 << n_items)]:
        index, weight_sum=0,0
        for weight in weights:
            if(binary_array[index] == 1):
                weight_sum+=weight
            index+=1
        if(weight_sum <= limit):
            index2, price_sum=0,0
            for price in prices:
                if(binary_array[index2] == 1):
                    price_sum+=price
                index2+=1
            if(price_sum > max_price):
                max_price=price_sum
                max_array=binary_array

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

# print(compute("inst/knap_4.inst.dat"))