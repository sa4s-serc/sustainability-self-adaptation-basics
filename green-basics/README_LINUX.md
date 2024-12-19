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

### Step 1: Obtain the Project Files

#### Option 1: using Git (Recommended)

1. Open the terminal.
2. Clone the project repository:
   ```bash
   git clone https://github.com/sa4s-serc/sustainability-self-adaptation-basics.git
   ```
3. Navigate to the Project Directory
   ```bash
   cd sustainability-self-adaptation-basics
   ```

#### Option 2: Download as ZIP File

1. Go the respoitory's webpage on GitHub [https://github.com/sa4s-serc/sustainability-self-adaptation-basics](https://github.com/sa4s-serc/sustainability-self-adaptation-basics)
2. Click the `Code` button and select `Download ZIP`
3. Extract the ZIP file into a folder on your system, once the download is complete:
   ```bash
   cd Downloads
   unzip sustainability-self-adaptation-basics.zip
   cd sustainability-self-adaptation-basics
   ```
   ![image](https://github.com/user-attachments/assets/d4c3a401-ee8a-4f2d-b749-3b2add491613)

#### Option 3: Using Wget (Command-Line)

1. Make sure you have the `wget` command in your system. If not there, run:
2. Download the repository as a ZIP file using `wget`:
   ```bash
   wget https://github.com/sa4s-serc/sustainability-self-adaptation-basics/archive/main.zip -O sustainability-self-adaptation-basics.zip
   ```
   ![image](https://github.com/user-attachments/assets/4bad6b18-6f07-4ba8-9c5f-0c6cc9b49ca3)

4. Extract the ZIP file, once the download is complete:
   ```bash
   unzip sustainability-self-adaptation-basics.zip
   cd sustainability-self-adaptation-basics
   ```
   ![image](https://github.com/user-attachments/assets/d4c3a401-ee8a-4f2d-b749-3b2add491613)

### Step 2: Run the Dashboard

1. Navigate to the task folder.
   ```bash
   cd green-basics
   ```
   ![image](https://github.com/user-attachments/assets/fd4aaefb-c18b-47c4-8ddc-05dc34bd6e58)

2. To install the Dependencies as required, run:
   ```bash
   pip install -r requirements.txt
   ```
   ![image](https://github.com/user-attachments/assets/503f06fc-789a-41b1-ae2b-566668b1f403)

3. To start the application, run:
   ```bash
   python3 app.py
   ```
4. You should see the output indicating the server is running:
   ![image](https://github.com/user-attachments/assets/edae9a80-5ff7-4281-ac8b-f6377ce3c16f)

5. Run the Model, as follows:
  - Open the new terminal window or tab.
  - Navigate to the project folder if not already there
    ![image](https://github.com/user-attachments/assets/fd4aaefb-c18b-47c4-8ddc-05dc34bd6e58)
  - Run the model script:
    ```bash
    python3 monitor_model.py
    ```
    ![image](https://github.com/user-attachments/assets/61261a9e-1cd2-4279-ba46-002a056b3e43)

    

