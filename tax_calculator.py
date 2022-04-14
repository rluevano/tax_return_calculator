"""

Author: RLuevano

"""


def calculate_tax(fed_tax_rate,
                  fed_income_band,
                  state_tax_rate,
                  state_income_band,
                  salary,
                  hsa_gain,
                  retirement_401k,
                  employer_401k_percent,
                  employer_401k_cap):

    print("hello - lets get started with calculating your tax liability")
    fed_tax_total = 0
    state_tax_total = 0

    salary_fed_calc = salary
    salary_state_calc = salary
    # first we calculate the state tax total

    for i in range(0, len(state_tax_rate)):
        print(i)
        if i == 0:
            state_tax_total += (state_income_band[i] * state_tax_rate[i])
            salary_state_calc -= state_income_band[i]
            print("state tax total so far is: " + str(state_tax_total))
            print("income left to tax is: " + str(salary_state_calc))
        elif i == (len(state_tax_rate) - 1):
            # logic for the last tax bracket
            # print("too much money")
            state_tax_total += ((salary - state_income_band[i - 1]) * state_tax_rate[i])
            salary_state_calc -= salary_state_calc
            print("state tax total so far is: " + str(state_tax_total))
            print("income left to tax is: " + str(salary_state_calc))
        else:
            state_tax_total += ((state_income_band[i] - state_income_band[i - 1]) * state_tax_rate[i])
            salary_state_calc -= (state_income_band[i] - state_income_band[i - 1])
            print("state tax total so far is: " + str(state_tax_total))
            print("income left to tax is: " + str(salary_state_calc))
        i += 1
        print()
        if salary_state_calc <= 0:
            print("I've run out of bread")
            break
        else:
            print("the feds still have some bread")




    #while salary_fed_calc > 0:
    #return fed_tax_total, state_tax_total

    return

fed_tax_rate = (10, 12, 22, 24, 32, 35, 37)
fed_income_band = (9950, 40525, 86375, 164925, 209425, 523600, 523601)
state_tax_rate = (1, 2, 4, 6, 8, 9.3, 10.3, 11.3, 12.3)
state_income_band = (9325, 22107, 34892, 48435, 61214, 312686, 375221, 625369, 625370)
salary = 80000
hsa_gain = 5000
retirement_401k = 4
employer_401k_percent = 0.50
employer_401k_cap = 4

calculate_tax(fed_tax_rate,
                  fed_income_band,
                  state_tax_rate,
                  state_income_band,
                  salary,
                  hsa_gain,
                  retirement_401k,
                  employer_401k_percent,
                  employer_401k_cap)
