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
    sample_logs = [
        "INFO App started",
        "WARNING Low disk space",
        "ERROR Database connection failed"
    ]

    result = analyze_logs(sample_logs)
    print(result)
