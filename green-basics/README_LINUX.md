# Energy Monitoring Dashboard with pyRAPL

This tutorial explains how to set up and run the energy monitoring dashboard for Linux users.

---

## Overview

This project demonstrates how to monitor energy consumption, CPU usage, and memory usage of a machine learning model using `pyRAPL` and `psutil`. The results are displayed on a live dashboard.

---

## Prerequisites

- **Operating System**: Linux
- **Git(Optional)**: Command
- **Python Version(Required)**: 3.10 or later
- **Dependencies(Later part)**:
  - Flask
  - pyRAPL
  - psutil
  - scikit-learn
  - numpy
 
Before starting, ensure the following are installed on your Linux system. If not, follow the instructions below:

1. **Git:**
  - Git is used to clone the repository. If not installed, run:
    ```bash
    sudo apt update
    sudo apt install git -y
    ```
  - To verify the installation, run:
    ```bash
    git --version
    ```
    
2. **Python:**
  - Python is required to run the application
  - Check the Python Version:
    ```bash
    python3 --version
    ```
  - If Python is not installed, run:
    ```bash
    sudo apt install python3.12 python3-pip -y
    ```
---

## Step-by-Step Instructions

### Step 1: Clone the Repository

1. Open the terminal.
2. Clone the project repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
