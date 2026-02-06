def analyze_logs(log_lines):
    info = 0
    warning = 0
    error = 0

    for line in log_lines:
        if "INFO" in line:
            info += 1
        elif "WARNING" in line:
            warning += 1
        elif "ERROR" in line:
            error += 1

    return {
        "INFO": info,
        "WARNING": warning,
        "ERROR": error
    }


if __name__ == "__main__":
    with open("app.log", "r") as file:
        log_lines = file.readlines()

    result = analyze_logs(log_lines)
    print(result)
