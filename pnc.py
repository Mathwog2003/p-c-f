import os
import time
import sys

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def measure_time_space(program_path):
    start_time = time.time()

    try:
        with open(program_path, "r") as f:
            program_code = f.read()
            exec(program_code, globals())

        end_time = time.time()
        execution_time = end_time - start_time

        space_complexity = sys.getsizeof(program_code)

        return program_code, execution_time, space_complexity
    except Exception as e:
        print(f"Error executing program {program_path}: {str(e)}")
        return None, None, None

def get_best_program(folder):
    best_program = None
    best_time = -1
    best_space = -1
    omitted_programs = []

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path) and file.endswith(".py"):
            program_code, execution_time, space_complexity = measure_time_space(file_path)

            if program_code is not None and "is_prime" in program_code:
                program_output = None
                try:
                    program_output = eval("is_prime(7)")  # Customize the input for testing
                except Exception as e:
                    print(f"Error executing program {file}: {str(e)}")
                    omitted_programs.append(file)
                    continue

                print(f"Running program: {file}")
                print("Program output:")
                print(program_output)
                print(f"Execution Time: {execution_time} seconds")
                print(f"Space Complexity: {space_complexity} bytes")
                print("-----------------------")

                if execution_time > best_time or best_time == -1:
                    best_program = file
                    best_time = execution_time
                    best_space = space_complexity
            else:
                omitted_programs.append(file)

    print("Omitted programs:")
    for omitted_program in omitted_programs:
        print(omitted_program)

    return best_program, best_time, best_space

def main():
    folder = input("Enter the folder path: ")
    best_program, best_time, best_space = get_best_program(folder)

    print("Best Prime Checker Program:")
    print(f"Program: {best_program}")
    print(f"Execution Time: {best_time} seconds")
    print(f"Space Complexity: {best_space} bytes")

if __name__ == "__main__":
    main()
