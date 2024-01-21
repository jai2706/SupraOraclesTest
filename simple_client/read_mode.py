def run_read_mode():
    # Read the average price from the file and print it
    with open("data/average_price.txt", "r") as file:
        average_price = file.read()
    print(average_price)
