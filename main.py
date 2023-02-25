from functions import *


def menu():
    try:
        airCode = input("Enter the airport code: ")
        timeRange = int(input("Enter a time range: "))
        soup = get_data_from_URL(airCode, timeRange)
        data = parse_data(soup)
        create_graph(data[0], data[1])
    except Exception as ex:
        # print(ex)
        print("Incorrect arguments have been entered, try again later...")


if __name__ == '__main__':
    menu()

