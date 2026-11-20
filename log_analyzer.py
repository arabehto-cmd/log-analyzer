def count_errors(filename):
    with open("server.log.txt", "r") as file:
        error_count = 0
        for line in file:
            clean_line = line.strip()
            if "ERROR" in clean_line:
                error_count += 1
    return error_count
result1 = count_errors("server.log.txt")
print(f"total errors found {result1}")