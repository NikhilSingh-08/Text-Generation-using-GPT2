# text-generation-using-gpt-2

### Step 1: Clone the repository
```bash
git clone https://github.com/Deep-Learning-01/text-generation-using-gpt-2.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.7.6 -y
```
```bash
conda activate venv
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

```

### Step 5 - Run the application server
```bash
python main.py
```

### Step 6. Train application
```bash
http://localhost:8080/train

```

### Step 7. Prediction application
```bash
http://localhost:8080/predict

```
