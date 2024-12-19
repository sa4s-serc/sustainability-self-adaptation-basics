# Energy Monitoring Dashboard with pyRAPL

This tutorial explains how to set up and run the energy monitoring dashboard for Windows users.

---

## Overview
This project demonstrates how to monitor energy consumption, CPU usage, and memory usage of a machine learning model using pyRAPL and psutil. The results are displayed on a live dashboard.

---

## Prerequisites

- **Operating System**: Windows 10 or Later
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

### Step 1: Obtain the Project Files

#### Option 1: using Git (Recommended)

1. Open the Command prompt or PowerShell
2. Clone the project repository:
   ```bash
   cd Downloads/
   git clone https://github.com/sa4s-serc/sustainability-self-adaptation-basics.git
   ```
3. Navigate to the Project Directory
   ```bash
   cd sustainability-self-adaptation-basics
   ```

#### Option 2: Download as ZIP File

1. Go the respoitory's webpage on GitHub [https://github.com/sa4s-serc/sustainability-self-adaptation-basics](https://github.com/sa4s-serc/sustainability-self-adaptation-basics)
2. Click the `Code` button and select `Download ZIP`
3. Open the terminal
4. Extract the ZIP file into a folder on your system, once the download is complete:
   ```bash
   cd Downloads
   unzip sustainability-self-adaptation-basics.zip
   cd sustainability-self-adaptation-basics
   ```

### Step 2: Run the Dashboard

1. Navigate to the task folder.
   ```bash
   cd green-basics
   ```

2. To install the Dependencies as required, run:
   ```bash
   pip install -r requirements.txt
   ```

3. To start the application, run:
   ```bash
   python3 app.py
   ```
4. You should see the output indicating the server is running:

5. Run the Model, as follows:
  - Open the new terminal window or tab.
  - Navigate to the project folder if not already there
  - Run the model script:
    ```bash
    python3 monitor_model.py
    ```

### Step 3: View the Dashboard:

1. Open your browser
2. Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. You will see real-time metrics for:
  - Energy usage
  - CPU usage
  - Memory Usage

---

## Next Steps (Explore out of own interest)

- Modifying the dashboard to display additional metrics.
- Integrating your own machine learning models.

---
