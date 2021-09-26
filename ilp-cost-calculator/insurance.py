'''
Name: Olichuuwon
Project: Insurance AXA WH Calculation
'''


def main():
    # TIME PERIODS
    MONTHS_PER_YEAR = 12
    YEARS = 11

    # CHARGES INVOLVED
    CHARGES_PER_YEAR = 3.5 / 100
    CHARGES_PER_MONTH = CHARGES_PER_YEAR / 12

    # PREMIUMS YOU HAVE CHOSEN
    PREMIUMS = 300

    # SIMULATED RETURN ON INVESTMENT
    ESTIMATE_ROI_PER_YEAR = 15 / 100
    ESTIMATE_ROI_PER_MONTH = ESTIMATE_ROI_PER_YEAR / 12 + 1

    # FINAL VALUES
    TOTAL_COST = 0  # TOTAL COST FROM THE MONTHLY DEDUCTIONS
    TOTAL_PREMIUMS = 0  # TOTAL WORTH IN ACCOUNT
    RAW = 0  # IF YOU NEVER INVESTED

    # for amount of months, do a cumulative calculation
    for year in range(YEARS):
        for month in range(MONTHS_PER_YEAR):
            # for every month, premium is paid
            print("YEAR", year + 1, "MONTH", month + 1)
            RAW += PREMIUMS
            TOTAL_PREMIUMS += PREMIUMS
            print("AFTER PAYING PREMIUMS", "{:.2f}".format(TOTAL_PREMIUMS))
            # amount of cost that is incurred based on their policy
            COST = TOTAL_PREMIUMS * CHARGES_PER_MONTH
            TOTAL_COST += COST
            print("COSTS TO BE DEDUCTED", "{:.2f}".format(COST))
            # after deductions
            TOTAL_PREMIUMS = TOTAL_PREMIUMS - COST
            print("MONEY IN BANK AFTER DEDUCTIONS", "{:.2f}".format(TOTAL_PREMIUMS))
            # roi from funds
            TOTAL_PREMIUMS = TOTAL_PREMIUMS * ESTIMATE_ROI_PER_MONTH
            print("INVESTMENT RETURNS", "{:.2f}".format(TOTAL_PREMIUMS), "RAW", "{:.2f}".format(RAW))
            print("")
    # in summary
    PER_MONTH_CHARGE = TOTAL_COST / YEARS / MONTHS_PER_YEAR
    print("TOTAL 'COST' OF INVESTMENT FOR THE", YEARS, "YEAR PERIOD", "{:.2f}".format(TOTAL_COST))
    print("TOTAL 'COST' OF INVESTMENT PER MONTH", "{:.2f}".format(PER_MONTH_CHARGE), "WHEN PREMIUMS ARE", PREMIUMS)
    print("PERCENTAGE THAT IS ACTUALLY COST GIVEN TO COMPANY", "{:.2f}".format(PER_MONTH_CHARGE / PREMIUMS * 100), "%")


if __name__ == '__main__':
    main()
