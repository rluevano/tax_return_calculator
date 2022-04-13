def gather_info():
    print("This program will calculate the total income tax owed for both the federal government as well as state\n")
    year = input("Enter the year in which to calculate your income tax: ")
    state = input("Enter the state in which you resided during the year " + year + ": ")
    salary = input("Enter your gross income for the year " + year + ": ")
    hsa_gain = input("Enter the gain for the year " + year + " :")
    retirement_401k = input("Enter your contribution % to your 401k retirement amount for the year " + year + ": ")
    employer_401k_percent = input("Enter the % your employer contributes to your 401k retirement account: ")
    employer_401k_cap = input("Enter the % your employer contributes towards your 401k retirement account: ")

    return year, state, salary, hsa_gain, retirement_401k, employer_401k_percent, employer_401k_cap

