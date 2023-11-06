#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Nov 1, 2023
# This program will ask the user
# for a integer and it will tell them the sum
# of all the numbers added to it with try catch


def main():
    # Get the user year as a string and display message about program

    print("This program will ask the user for a integer and it will ")
    print("tell them the sum of all the numbers added to it")
    user_num_string = input("Enter your integer: ")

    # initialize variables
    counter = 0
    sum = 0

    # Catch if the user num is something wrong

    try:
        # Convert user int as a string to int
        user_num_int = int(user_num_string)

        # Check if user num is negative
        if user_num_int < 0:
            print(
                "{} is a negative number, please enter a positive number".format(
                    user_num_int
                )
            )

        # loop for sum of user_number_as_int

        else:
            while counter <= user_num_int:
                # calculate sum
                sum = sum + counter
                # increment counter
                counter = counter + 1

                # display how many time it went through the loop
                print("{} time through the loop".format(counter))

            # display sum to user and counter to user
            print("The sum of the numbers from 0 to {} = {}".format(user_num_int, sum))

    # Display a message to the user if they entered something that is not valid

    except Exception:
        # Message for invalid user input
        print("\n{} is not a valid integer.".format(user_num_string))


if __name__ == "__main__":
    main()
