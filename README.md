# 🚀 DevOps Log Monitor

![CI Pipeline](https://github.com/charithareddymule/devops-log-monitor/actions/workflows/ci.yml/badge.svg)

A lightweight DevOps-style log monitoring tool built with Python.  
This project demonstrates how automated testing, linting, and CI pipelines are used to maintain code quality in real-world DevOps workflows.

---

## 📌 Project Overview

In production systems, logs are critical for monitoring application health.  
This project simulates a **log monitoring utility** that:

- Reads application logs from a file
- Counts log levels (INFO, WARNING, ERROR)
- Ensures correctness through automated tests
- Enforces coding standards using linting
- Runs fully automated CI using GitHub Actions

All development and automation are done **entirely on GitHub**.

---

## ⚙️ Features

- 📄 Reads and analyzes real log files
- 📊 Counts INFO, WARNING, and ERROR logs
- 🧪 Unit testing using `pytest`
- 🧹 Code linting using `flake8`
- 🔁 Continuous Integration with GitHub Actions
- ✅ Quality gates: tests + lint must pass before success

---

## 🛠 Tech Stack

- **Python**
- **Pytest** (testing)
- **Flake8** (linting)
- **GitHub Actions** (CI)
- **GitHub** (version control & automation)

---

## 📁 Project Structure

---

## ▶️ How It Works

1. Logs are read from `app.log`
2. The script analyzes log severity levels
3. Results are returned as structured output
4. Tests validate the logic
5. CI pipeline runs automatically on every push

Example output:

---

## 🔄 CI Pipeline Workflow

On every push to the `main` branch, GitHub Actions automatically:

1. Sets up Python
2. Installs dependencies
3. Runs unit tests
4. Runs flake8 linting
5. Fails the pipeline if any step fails

This ensures **code reliability and quality enforcement**.

---

## 🎯 Why This Project Matters

This project demonstrates:
- Practical DevOps thinking
- CI/CD fundamentals
- Testing and quality gates
- Debugging and fixing pipeline failures
- Clean and maintainable project structure

It reflects **real-world DevOps practices**, not just theoretical concepts.

---

## 📌 Future Enhancements

- Dockerize the application
- Generate HTML reports from logs
- Add log threshold alerts
- Extend CI with deployment steps

---

## 👩‍💻 Author

**Charitha Reddy**  
Aspiring Cloud & DevOps Engineer  



