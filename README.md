# Practical 09 – Continuous Testing Pipeline Using Jenkins

## Objective
Automatically test a Python calculator application every time code is pushed to GitHub, using Jenkins as the CI automation server.

---

## Project Structure

```
Prac9/
├── calculator.py          # Application code (add, subtract, multiply, divide)
├── test_calculator.py     # Automated test cases using PyTest
├── requirements.txt       # Python dependencies (pytest, pytest-html)
├── pytest.ini             # PyTest configuration
├── Jenkinsfile            # Jenkins pipeline script (for Pipeline from SCM)
└── README.md              # This file
```

---

## Files

### `calculator.py`
Contains four arithmetic functions: `add`, `subtract`, `multiply`, `divide`.  
`divide` raises a `ValueError` if the divisor is zero.

### `test_calculator.py`
Eight test cases covering all four functions, including edge cases (negatives, zero, divide-by-zero).

### `requirements.txt`
```
pytest
pytest-html
```

### `Jenkinsfile`
Pipeline stages:
1. **Checkout** – Clones the latest code from GitHub
2. **Install Dependencies** – Runs `pip install -r requirements.txt`
3. **Run Tests** – Runs `pytest`

---

## Step-by-Step Setup

### Step 1 – Test Locally
```bash
cd Prac9
pip install -r requirements.txt
pytest
```
Expected: **8 passed**

### Step 2 – Push to GitHub
```bash
git init
git add .
git commit -m "Prac9: Add calculator project with Jenkins pipeline"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 3 – Install Jenkins (Windows)
1. Install **JDK 17 or 21** from https://adoptium.net
2. Download Jenkins from https://www.jenkins.io/download/
3. Run the installer – Jenkins starts automatically on `http://localhost:8080`
4. Follow the setup wizard: unlock with initial password, install suggested plugins, create admin user.

### Step 4 – Create a Jenkins Pipeline Job
1. Open `http://localhost:8080` → **New Item**
2. Name: `STQA-Continuous-Testing` → Select **Pipeline** → Click **OK**
3. Scroll to **Pipeline** section → Under **Definition** choose **Pipeline script**
4. Paste the pipeline script (from Jenkinsfile), replacing `YOUR_GITHUB_REPOSITORY_URL`
5. Click **Save**

**Pipeline Script (Windows):**
```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}
```

### Step 5 – Run the Pipeline
1. Click **Build Now**
2. Click the build number (e.g., **#1**) under Build History
3. Click **Console Output** to see live output
4. Expected result: `8 passed` → **Finished: SUCCESS**

---

## Demonstrate a Failed Test (Defect Demo)

### Introduce a Defect
Edit `calculator.py` – change `add` to return `a - b`:
```python
def add(a, b):
    return a - b  # BUG: should be a + b
```

Push to GitHub and click **Build Now**.

Expected Console Output:
```
FAILED test_calculator.py::test_add - AssertionError: assert -1 == 5
1 failed, 7 passed
Finished: FAILURE
```

### Fix the Defect
Revert the change:
```python
def add(a, b):
    return a + b
```
Push and run pipeline again → **SUCCESS**

---

## Key Concepts

| Tool    | Role                                           |
|---------|------------------------------------------------|
| Git     | Tracks code changes on your laptop             |
| GitHub  | Stores code online (remote repository)         |
| Jenkins | Automation server – runs checkout, install, test |
| PyTest  | Testing framework that executes test functions |

> **Remember:** Jenkins does NOT test your code by itself. It runs `pytest`, which does the actual testing.

---

## Conclusion
The continuous testing pipeline successfully automates: obtaining source code from GitHub → installing dependencies → executing automated test cases → reporting pass/fail results through Jenkins.
