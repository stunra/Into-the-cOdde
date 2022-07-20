import random
import pandas as pd

while 1 == 1:
    # roll d8 d4 times, re-roll duplicates
    d4_roll = random.randint(1, 4)
    d8_rolls = random.sample((1, 8), d4_roll)
    d8_rolls.sort()
    # read table .csv, loop through each table needed rolling the d20
    results = []
    df = pd.read_csv('randomMonster.csv')
    # r_rolls = []
    for x in d8_rolls:
        if x == 1:
            y = random.randint(1, 12)
        elif x == 7:
            y = random.randint(1, 12)
        elif x == 8:
            y = random.randint(1, 10)
        else:
            y = random.randint(1, 20)
        # r_rolls.append(y)
        data = df.iloc[y - 1, x - 1]
        results.append(data)
    # Test rolls
    # print(d4_roll)
    # print(d8_rolls)
    # print(r_rolls)

    # add monster form to list
    # should shape-shifting be restricted to human + other
    f_roll = random.randint(1, 20)
    # print(f_roll)
    form = []
    if f_roll == 19 or f_roll == 20:
        new_rolls = random.sample(range(1, 18), 2)
        # print(new_rolls)
        form.append(df.iloc[new_rolls[0] - 1, 8])
        form.append(df.iloc[new_rolls[1] - 1, 8])
    else:
        form.append(df.iloc[f_roll - 1, 8])


    print("The monster is ")
    print(results)
    if f_roll == 19:
        print("chimeric ", form)
    elif f_roll == 20:
        print("shape-shifting ", form)
    else:
        print("form = ", form)
    print("\n")
    input("Press enter to generate another...")

