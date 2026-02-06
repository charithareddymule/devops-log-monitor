from app.log_monitor import analyze_logs


def test_analyze_logs_counts_correctly():
    logs = [
        "INFO App started",
        "WARNING Low memory",
        "ERROR Database failed",
        "INFO User logged in"
    ]

    result = analyze_logs(logs)

    assert result["INFO"] == 2
    assert result["WARNING"] == 1
    assert result["ERROR"] == 1
