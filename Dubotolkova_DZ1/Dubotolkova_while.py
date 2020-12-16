def pow_kilometrs(km):
    day = 0
    distance = 0
    while distance<km:
        day += 1
        distance += 2**day
    return (day)

def is_prime_number(number):
    i=2
    if number == 2:
        return True
    while i<number:
        if number%i == 0:
            return False
        else:
            i+=1
    return True

def prime_kilometrs(km):
    day = 0
    distance = 0
    number = 2
    while distance<km:
        if is_prime_number(number):
            distance+= number
            day+=1
            number+=1
        else:
            number+=1
    return day

def run_15_proc():
    end_day = 30
    day = 2
    Sumdistance = 20
    distance = 10
    while (day<end_day):
        distance *= 1.15
        Sumdistance += distance*2
        day += 2
    if end_day%2==0:
        return Sumdistance
    else:
        return Sumdistance - distance/1.15


def run_10_proc():
    day = 1
    Sumdistance = 10
    distance = 10
    day_100_km = 0
    day_20_km = 0
    while(distance<20):
        while (Sumdistance<100):
            distance *= 1.10
            Sumdistance += distance
            day +=1
            day_100_km = day
        distance *= 1.10
        Sumdistance += distance
        day += 1
        day_20_km = day
    return day_20_km, day_100_km


if __name__ == '__main__':
    print("While 1:")
    print(pow_kilometrs(1000))
    print(pow_kilometrs(10000))
    print("While 2:")
    print(prime_kilometrs(1000))
    print(prime_kilometrs(10000))
    print("While 3:")
    print(run_15_proc())
    print("While 4:")
    a,b = run_10_proc()
    print("a:",a)
    print("b:", b)