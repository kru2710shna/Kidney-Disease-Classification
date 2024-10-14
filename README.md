# Kidney-Tumor Image Classification 

# Kidney Tumor

A kidney tumor is an abnormal growth of tissue in the kidneys. These tumors can be benign (non-cancerous) or malignant (cancerous). Understanding kidney tumors is essential for early diagnosis and effective treatment.

## Types of Kidney Tumors

1. **Benign Tumors**
   - **Angiomyolipoma**: Composed of blood vessels, muscle, and fat; often does not require treatment unless large.
   - **Oncocytoma**: A rare tumor that is typically slow-growing and usually requires no treatment unless symptomatic.

2. **Malignant Tumors**
   - **Renal Cell Carcinoma (RCC)**: The most common type of kidney cancer in adults, often diagnosed in advanced stages.
   - **Wilms Tumor**: A type of kidney cancer that primarily affects children, typically occurs in children aged 3 to 4 years.
   - **Transitional Cell Carcinoma**: A cancer that can occur in the kidney and the urinary tract.

## Symptoms

Symptoms of kidney tumors may vary but can include:
- Blood in urine (hematuria)
- Persistent back pain or side pain
- A lump in the abdomen or side
- Unexplained weight loss
- Fatigue

## Diagnosis

Diagnosing kidney tumors typically involves:
- **Imaging Tests**: Ultrasound, CT scans, or MRIs to visualize the kidneys.
- **Biopsy**: Taking a small tissue sample to determine whether a tumor is benign or malignant.

## Treatment Options

Treatment depends on the type and stage of the tumor:
- **Surgery**: Often the first line of treatment for malignant tumors; may involve partial or complete removal of the kidney.
- **Radiation Therapy**: May be used for tumors that cannot be surgically removed.
- **Chemotherapy**: Usually employed for advanced cases of kidney cancer.

## Conclusion

Kidney tumors require prompt medical attention for proper diagnosis and treatment. Regular check-ups and imaging can help in early detection, improving the chances of successful treatment.

## Step 1: Automated Python Folder and File Generator

### Overview
This step involves creating an automated script that generates a predefined folder structure and necessary files for the Kidney Image Classifier project. The script also incorporates logging to track the creation of directories and files.

### Features
- **Automated Folder and File Generation**: Automatically creates the required directories and files for the project.
- **Logging**: Logs activities such as directory creation and file creation to provide insight into the script's operations.

### Project Template
A project template is provided in the file named `template.py`. This template serves as a reference for structuring the Kidney Image Classifier project.

### Usage
To use the automated folder and file generator, run the script associated with this step. Ensure you have the necessary permissions to create directories and files on your system.

## Step 2: Tech Stack

The following libraries and frameworks are utilized in the Kidney Image Classifier project:

- **TensorFlow**: For building and training machine learning models.
- **Pandas**: For data manipulation and analysis.
- **DVC (Data Version Control)**: For managing data and model versions.
- **MLflow**: For tracking experiments and managing machine learning workflows.
- **Jupyter Notebook**: For interactive coding and data exploration.
- **NumPy**: For numerical operations and handling arrays.
- **Matplotlib**: For data visualization.
- **Seaborn**: For statistical data visualization.
- **Python-box**: For nested dictionary management.
- **PyYAML**: For YAML file parsing and writing.
- **TQDM**: For progress bar displays in loops.
- **Ensure**: For type-checking and validation.
- **Joblib**: For lightweight pipelining in Python.
- **Types-PyYAML**: For type annotations for PyYAML.
- **SciPy**: For scientific computing and technical computing.
- **Flask**: For creating a web application.
- **Flask-CORS**: For handling Cross-Origin Resource Sharing in Flask.
- **Gdown**: For downloading files from Google Drive.
- **-e .**: For installing the package in editable mode.

## Transfer Learning

VGG16 is a convolutional neural network (CNN) model that is used to classify images: 

Layers: VGG16 is a 16-layer deep network that consists of 13 convolution layers and three fully connected layers 

Image size: The input image size for VGG16 is 224-by-224 

Training: VGG16 was trained on the ImageNet database, which contains over 14 million images from almost 1000 classes 

Accuracy: VGG16 can achieve almost 92.7% top-5 test accuracy on ImageNet 

Model name: VGG stands for Visual Geometry Group, which is the name of the University of Oxford group that developed the model 

Parameters: VGG16 has about 138 million parameters 


## Step 3: Packaging Script + Virtual Environment + Logging + Exception Hnadling 

# Overview of `setup.py`

The `setup.py` file is a script used for packaging the Kidney Image Classifier project as a Python package. It utilizes the `setuptools` library to define package metadata and configuration.

## Usage
To package the Kidney Image Classifier project, run this script. It prepares the package for distribution, making it easy to install and share.


# Virtual Environment

### 1. Install `virtualenv`
If you don't have `virtualenv` installed, you can install it using pip

```bash
pip install virtualenv
```

### 2. Create a Virtual Environment
Navigate to your project directory and create a virtual environment by running

```bash
cd path/to/your/project/directory
virtualenv venv
```

### 3. Activate the Virtual Environment
Activate the virtual environment using the following command

```bash
source venv/bin/activate
```

### 4. Install Dependencies 
After activating the virtual environment, install the required dependencies for the project. You can do this using the requirements.txt file 

```bash
pip install -r requirements.txt
```

### 4. Deactivate
When you are finished working, you can deactivate the virtual environment by running

```bash
deactivate
```

## Set Up Logging
Logging is crucial for tracking the behavior of your application and troubleshooting issues. To enable logging in your Python project, you can use Python's built-in logging module.

```bash
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

logging.info("Virtual environment is successfully set up and activated.")
```

##  Implement Error Handling
Proper error handling helps prevent crashes and improves debugging. Below is an example of how to implement basic exception handling in Python

```bash
try:
    # Code that might cause an exception
    logging.info("Attempting to install dependencies.")
    # Example: Install a package
    import some_nonexistent_package
except ImportError as e:
    logging.error(f"Error occurred: {e}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
else:
    logging.info("Dependencies installed successfully.")
finally:
    logging.info("Script execution completed.")
```

### 5. Run the Pipeline 
```bash
dvc repro
```

### 6. Run Flask App

```bash
python app.py
```

# End-to-End Data Pipeline Summary - Step-1 For the Project

## Step-1.1 Updating Configuration

We started by updating the config/config.yaml file to define the paths and configurations for each pipeline stages.

This is a configuration file, typically in YAML format, used for defining paths, URLs, and parameters for different stages of an end-to-end data pipeline. It centralizes the configurations so the code can easily reference these settings, which is important in projects following MLOps practices. Each section specifies settings related to different parts of the pipeline: Data Ingestion, Base Model Preparation, and Model Training.

Reason: Centralized configuration management enables easy parameterization and changes, making the pipeline more adaptable.

## Step-1.2 Updating params.yaml

The params.yaml file allows us to store hyperparameters or other configuration values, promoting modular and reusable code.

## Step-1.3 Defining Entity Class (config_entity.py)
Entities represent standardized inputs for pipeline stages.

The DataIngestionConfig class is a configuration object used in the data ingestion phase of a pipeline. It holds essential paths and URLs related to data ingestion, including where the data is stored, where it is downloaded from, and where it will be extracted. By using a data class, this configuration is structured and immutable, making it easy to pass around and use throughout the pipeline without risk of modification. This ensures that the data ingestion stage is well-configured and organized.

## Step-1.4 Configuration Manager (configuration.py)

The configuration manager handles the reading of YAML files and directory creation. It encapsulates how configuration is fetched and allows different pipeline components to access configuration details easily.

## Step-1.5 Data Ingestion Component (components/data_ingestion.py)
Components execute the actions based on configuration inputs, forming the backbone of the end-to-end pipeline.

In MLOps, components are individual units of the pipeline that execute specific tasks like data ingestion, model training, or evaluation. Unlike configurations, components are responsible for executing actions based on configurations provided by the manager.

### Step 1.6: Preparing a Base Model
It initializes a configuration manager to retrieve model preparation settings, then creates an instance of the `PrepareBaseModel` class to obtain and update the base model.

### Step 1.7: Training Pipeline
This code implements a training pipeline for a kidney image classifier, initializing a `ConfigurationManager` to fetch the training configuration.


### Step 1.8: Evaluation Pipeline
This code defines an evaluation pipeline for a kidney image classifier, executing the evaluation process, saving the evaluation score, and including a commented-out line for logging results to MLflow.


## DVC Configuration
The `dvc.yaml` file defines a multi-stage pipeline for a kidney image classification project, specifying the commands to execute, dependencies, parameters, and outputs for each stage.

## Flask App
This Flask application provides a web interface for a kidney image classification project. It includes:
- A home route that renders an HTML template.
- A training route that triggers the model training process.
- A prediction route that accepts an image, decodes it, and returns classification results as JSON.

## Thanks 
