#in: weight
#out:ship cost
#ship rate is 25 cents per pound  above 10 pounds, else 10 cents per pound.
#use functions.
#globals
total_weight = 0.0 #track the sum of weights across all inputs

#functions
def find_ship_rate(wt):
    if wt > 10.0:
        rt = 0.25
    else:
        rt = 0.1

    return rt


def find_ship_cost(wt,rt):
    cost = wt * rt

    return cost


def submit():
    global total_weight
    #inputs
    weight = 100.0
    #computations
    #process current inputs
    # 1.  find ship rate   out:  ship rate  float  in: weight
    ship_rate = find_ship_rate(weight)
    # 2.  find ship cost. out: ship cost  float  in: weight, rate
    ship_cost = find_ship_cost(weight, ship_rate)
    #update totals
    total_weight = total_weight + weight

    #outputs
    print(weight, ship_rate, ship_cost, total_weight)


#main
submit()
submit()