
def read_input(input_file):
    try:
        with open(input_file, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("Input file not found.")
        return []


def filter_lines(lines, keyword):
    return [line.strip() for line in lines if keyword in line]


def write_output(filtered_lines, output_file):
    try:
        with open(output_file, 'w') as f:
            for line in filtered_lines:
                f.write(line + '\n')
        print(f"Filtered lines were written to '{output_file}'.")
    except:
        print("Error occurred while writing to the output file.")


def filter_file(input_file, output_file, keyword):
    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f if keyword in line]
    except FileNotFoundError:
        print("Input file not found.")
        raise

    write_output(lines, output_file)



