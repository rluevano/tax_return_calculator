"""

Author: RLuevano

"""


def find_tax_bracket(year, state):
    # federal income bracket dictionary
    federal_brackets = {2021: ((10, 12, 22, 24, 32, 35, 37), (9950, 40525, 86375, 164925, 209425, 523600, 523601))}

    # below is a dictionary that contains the tax rate for its equivalent income brackets
    # each key represents a year and the value is a set of tuples nested within a tuple
    # the first tuple is the tax rate
    # the second tuple is the income bracket upper band (the last income bracket is the lower bound however)
    california_brackets = {2021: ((1, 2, 4, 6, 8, 9.3, 10.3, 11.3, 12.3),
                                  (9325, 22107, 34892, 48435, 61214, 312686, 375221, 625369, 625370))}

    # dictionary that contains the state as the key and the
    state_dict = {"california": california_brackets}

    for year_key in federal_brackets:
        if year == year_key:
            fed_bracket_tuple = federal_brackets[year_key]
            fed_tax_rate = fed_bracket_tuple[0]
            fed_income_band = fed_bracket_tuple[1]

    for state_key in state_dict:
        if state.lower() == state_key:
            for year_key, state_bracket_tuple in state_dict[state_key].items():
                if year_key == year:
                    state_tax_rate = state_bracket_tuple[0]
                    state_income_band = state_bracket_tuple[1]

    # print(fed_tax_rate)
    # print(fed_income_band)
    # print(state_tax_rate)
    # print(state_income_band)

    return fed_tax_rate, fed_income_band, state_tax_rate, state_income_band





