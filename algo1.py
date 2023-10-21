import random


def generate_random_data(M, k):
    data = []

    for _ in range(k):
        table = [random.randint(1, 1000) for _ in range(M)]
        data.append(table)

    return data


def save_to_text(data, filename):
    with open(filename, 'w') as file:
        for M, table in data:
            file.write(f"data for M={M} : {table}\n{'#' * 40}\n")


def main():
    M_values = [10, 100, 1000, 10000]
    k = 5  # Change this to the number of repetitions

    data_for_all_M = []

    for M in M_values:
        random_data = generate_random_data(M, k)
        data_for_all_M.append((M, random_data))

    filename = 'random_data.txt'

    # Save the generated data to a text file
    save_to_text(data_for_all_M, filename)

    print(f"Data saved to {filename}")


if __name__ == "__main__":
    main()
