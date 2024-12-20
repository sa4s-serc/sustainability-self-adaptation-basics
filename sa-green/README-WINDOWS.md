# Energy Usage Monitoring Tutorial

This tutorial will guide you through setting up a Python environment and running an energy usage monitoring system for machine learning tasks using Flask and pyRAPL.

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

Before starting, ensure the following are installed on your Windows system. If not, follow the instructions below:

1. **Git:**
  - Git is used to clone the repository.
  - If not installed go to [https://git-scm.com/downloads/win](https://git-scm.com/downloads/win)
  - Select `32 bit` or `64 bit` Standalone installer based on your system configuration.
    ![image](https://github.com/user-attachments/assets/346a7513-e4c3-4e4a-9a40-d86c6e419166)
  - An executable file will be installed.
  - Double click on the file and proceed with installation.
  - To verify the installation open the Command Prompt or PowerShell or Git Bash, and run:
    ```bash
    git --version
    ```
    
2. **Python:**
  - Python is required to run the application
  - If not installed go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
  - Download the `Python 3.12.8` version only.
    ![image](https://github.com/user-attachments/assets/f4b612c0-1dfc-47dc-9823-4492a8ae2be4)

  - An executable file will be installed.
  - Double click on the file and proceed with installation.
  - To verify the installation open the command prompt or PoweShell, and run:
    ```bash
    python --version
    ```
---

## Step-by-Step Instructions

### Step 1: Obtain the Project Files

This step is already done in the first task, if not done, follow [these steps](https://github.com/sa4s-serc/sustainability-self-adaptation-basics/blob/main/green-basics/README_LINUX.md#step-1-obtain-the-project-files)

- If you are in `green-basics` folder, go to `sa-green` folder in terminal.

### Step 2: Setup the Virtual Environment

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
  .\sa-green\Scripts\activate
  ```


### Step 3: Install Dependencies

- To install dependencies, run:
  ```bash
  pip install -r requirements.txt
  ```

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

- Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)


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
  
  


