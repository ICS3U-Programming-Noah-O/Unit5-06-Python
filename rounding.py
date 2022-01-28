#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 26, 2022
# This program accepts decimals and then rounds them to a
# given number of decimal places

import math


def round_decimal(decimal_num, dec_place):
    # This function rounds the user number to
    # the specific number of decimal places
    decimal_num[0] = decimal_num[0] * 10 ** dec_place
    decimal_num[0] = decimal_num[0] + 0.5
    decimal_int = int(decimal_num[0])
    decimal_int = decimal_int / 10 ** dec_place
    decimal_num[0] = decimal_int


def main():
    # This function asks the user for a number and a  number of decimals
    print("This program can round a number with " +
          "decimals to a specific decimal.")
    print(" ")
    decimal_number = input("Enter a number that has a decimal: ")
    # Make sure that the user input is a number
    try:
        decimal_number_float = float(decimal_number)

        decimal_places = input("Enter the number of decimal places: ")
        # Make sure that the user input is a number
        try:
            decimal_places_int = int(decimal_places)

            number_var = []
            number_var.append(decimal_number_float)
            round_decimal(number_var, decimal_places_int)
            print(number_var[0])
        # If the input is not a number display error message
        except Exception:
            print("{} is not a valid input.".format(decimal_places) +
                  "The input must be an integer.")

    # If the input is not a number display error message
    except Exception:
        print("{} is not a valid input. The input must be a number.".format(
            decimal_number))


if __name__ == "__main__":
    main()
