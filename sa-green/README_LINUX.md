#Energy Usage Monitoring Tutorial

This tutorial will guide you through setting up a Python environment and running an energy usage monitoring system for machine learning tasks using Flask and pyRAPL.

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
  - opencv-python-headless
  - tensorflow
 
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

### Step 1: Setup the Virtual Environment

- Deactivate any virtual environment if present.
  ```bash
  deactivate
  ```
- To create a virtual environment for this task, run:
  ```bash
  python -m venv sa-green
  ```
- To activate the virtual environent, run:
  ```bash
  source sa4s-env/bin/activate
  ```
  ![image](https://github.com/user-attachments/assets/d541cb7c-29d1-4200-ac00-0ea0ac3516bb)

### Step 2: Obtain the Project Files

This step is already done in the first task, if not done, follow [these steps](https://github.com/sa4s-serc/sustainability-self-adaptation-basics/blob/main/green-basics/README_LINUX.md#step-1-obtain-the-project-files)

- If you are in `green-basics` folder, go to `sa-green` folder in command prompt or Power Shell.
  ![image](https://github.com/user-attachments/assets/3924fd4d-dd1b-4f50-b382-176055b1a6fb)


### Step 3: Installl Dependencies

- To install dependencies, run:
  ```bash
  pip install -r requirements.txt
  ```
  ![image](https://github.com/user-attachments/assets/787d9b2c-1237-4016-91f0-e13e3c599193)

### Step 4: Project Structure

  project/
  ├── mape_k/
  │   ├── __init__.py
  │   ├── monitor.py
  │   ├── analyze.py
  │   ├── plan.py
  │   ├── execute.py
  │   ├── knowledge.py
  │
  ├── dashboard.py
  │
  ├── templates/
  │   ├── dashboard.html
  │
  ├── main.py

### Step 5: Run the Dashboard

- Start the Application:
  ```bash
  python dashboard.py
  ```
  ![image](https://github.com/user-attachments/assets/47f7759c-1740-4924-98fe-7a1cde138922)

- Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
  ![image](https://github.com/user-attachments/assets/736ec72a-5efa-474f-b505-cde9cff02fc8)


### Step 6: Run the main.py

- To start MAPE-K loop, run:
  ```bash
  python main.py
  ```
  ![image](https://github.com/user-attachments/assets/e633e522-dc7c-4e0f-9b39-4ff36aa08e12)

---

## Next Steps (Explore out of own interest)

- Create the dashboard to display additional metrics.
- Integrating your own machine learning models.

---
  
  


