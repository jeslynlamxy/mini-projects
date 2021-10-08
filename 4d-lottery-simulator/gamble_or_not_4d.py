"""
Name: Olichuuwon / Lam Xin Yi, Jeslyn
Project: Gambling Simulator - 4D
"""
import random


def generate_4d_string():
    """
    Generates random 4 numbers joined together
    :return: a string of 4 numbers
    """
    result = ''
    for index in range(4):
        result += str(random.randrange(10))
    return result


def gambling_loop(target_number, number_of_times):
    """
    For set number of times, checks if generated number is the same as target value
    :param target_number: target goal value
    :param number_of_times: times to gamble
    :return: number of iterations taken if success, if fail -1
    """
    for number in range(number_of_times):
        generated_value = generate_4d_string()
        print("WINNING NUMBER:", target_number, "/ GENERATED NUMBER:", generated_value, "/ TIMES BROUGHT:", number)
        if generated_value == target_number:
            return number
    return -1


def main():
    results = []
    maximum_times_to_try = 100000

    # GAMBLING JUST A NUMBER
    your_lucky_number = '6666'
    result = gambling_loop(your_lucky_number, maximum_times_to_try)
    results.append((your_lucky_number, result))

    # GAMBLING A SERIES OF NUMBERS
    your_lucky_numbers = ['9898', '2607', '8080']
    for item in your_lucky_numbers:
        result = gambling_loop(item, maximum_times_to_try)
        results.append((item, result))

    # RESULTS
    print("RESULTS: ", results)

    # TO TRACK
    loss = 0
    gain = 0
    price = 5
    prize = 10000

    # CALCULATE
    for number, result in results:
        loss += result * price
        if result != -1:
            gain += prize
    overall = gain - loss

    # REPORTING
    print("AMOUNTS LOST $", loss, "AMOUNT WON $", gain)
    print("WHEN PRICE IS $", price, "AND PRIZE $", prize)
    print("OVERALL COSTS $", overall)


if __name__ == '__main__':
    main()
