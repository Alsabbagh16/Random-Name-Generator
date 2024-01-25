import random

def read_names_from_file(file_path):
    with open(file_path, 'r') as file:
        names = file.read().splitlines()
    return names

def generate_random_names(first_names, family_names, num_names):
    random_names = []
    for _ in range(num_names):
        random_first_name = random.choice(first_names)
        random_family_name = random.choice(family_names)
        full_name = f"{random_first_name} {random_family_name}"
        random_names.append(full_name)
    return random_names

def write_names_to_file(output_file_path, names):
    with open(output_file_path, 'w') as file:
        for name in names:
            file.write(name + '\n')

if __name__ == "__main__":
    first_names_file = "first_names.txt"  # Replace with the actual path to your first names file
    family_names_file = "family_names.txt"  # Replace with the actual path to your family names file
    output_file = "output_names.txt"  # Replace with the desired output file path
    num_names_to_generate = 4444  # Change this to the desired number of random names

    first_names = read_names_from_file(first_names_file)
    family_names = read_names_from_file(family_names_file)

    random_names = generate_random_names(first_names, family_names, num_names_to_generate)

    write_names_to_file(output_file, random_names)

    print(f"{num_names_to_generate} random names generated and saved to {output_file}.")
