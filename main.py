"""

Author: RLuevano

"""


import user_information_capture
import tax_bracket_finder
import tax_calculator


def main():
    year, state, salary, hsa_gain, retirement_401k, employer_401k_percent, employer_401k_cap = \
        user_information_capture.gather_info()

    fed_tax_rate, fed_income_band, state_tax_rate, state_income_band = \
        tax_bracket_finder.find_tax_bracket(year, state)

    fed_tax_total, state_tax_total = \
        tax_calculator.calculate_tax(fed_tax_rate,
                                     fed_income_band,
                                     state_tax_rate,
                                     state_income_band,
                                     salary,
                                     hsa_gain,
                                     retirement_401k,
                                     employer_401k_percent,
                                     employer_401k_cap)


if __name__ == '__main__':
    print('done')
