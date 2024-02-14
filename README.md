![Screenshot 2024-02-14 140917](https://github.com/DivyanshKushwaha/Wine-Quality-Prediction/assets/121238698/525ae684-ca40-4f58-81c9-823d032e76f7 )



<h1 align="center">Wine Quality Prediction</h1>

This repository contains a machine learning project for predicting the quality of Wine using the dataset with 11 features. A Web App is built where you can input some feature values and get the wine quality prediction.

## About the Dataset


 The Dataset is available on : 

                       https://github.com/DivyanshKushwaha/datasets/blob/master/winequality-data.zip)

This dataset have 11 features :
  - fixed acidity
  - volatile acidity
  - citric acid
  - residual sugar
  - chlorides
  - free sulfur
  - dioxide
  - total sulfur dioxide
  - density
  - pH
  - sulphates
  - alcohol

## Model Used

- ElasticNet Regression model.




## Project Structure
This project is organized as follows:

- #### .gitignore
  This file specifies which files and directories should be ignored by Git.
- #### artifacts
     This folder contains the train,test and raw csv files along with the preprocessed and best model pickle file. These files are in this folder:
    - data_ingestion.py
    - data_transformation.py
    - data_validation.py
    - model_evaluation.py
    - model_trainer.py
- #### config
    This folder contains the artifacts files parameters like root directory, file path where the data is to be stored.
- #### logs
    This file helps us to record and manage application events and information, facilitating debugging and monitoring.
- #### research
    This directory contains Jupyter notebooks used for data exploration, visualization and model training. The coding of Data Ingestion to Model Training is done in this directory.
- #### src
    - This directory contains the source code for the project. The envoirement 'projectml' is created under this directory.  
    - Under the directory 'projectml' , there subdirectories are given:
        - components : Source coding of artifacts files is done here. Many classes are created here like logging status , downloading , unzipping etc.
        - config : All config classes are created here.
        - constants : Constants like config_file_path, parameter_file_path are created here that we can use anywhere in the envoirement.
        - entity : All dataclasses of config.yaml are created here.
        - pipeline : This directory contains data processing or machine learning pipelines used in the project, including:
            -  data_ingestion_pipeline.py : Handles the process of loading and preparing the dataset.
            -  data_validation_pipeline.py : Validate the ingestion process.
            -  data_transformation_pipeline.py : Performs data preprocessing and feature engineering.
            -  model_trainer_pipeline.py : Defines the training pipeline for model development.
            -  model_prediction_pipeline.py : Defines the pipeline for making predictions using the trained model.
        - utils : Contains utility functions used throughout the project.

 - #### static
     All helping files to build the application functional is here.

 - #### templates
     This folder contains the HTML files used for obtaining user input via form and flask uses these files as a rendering template

 - #### app.py
     This is the Flask application file responsible for hosting the web application.

 - #### main.py
     By running this file in terminal we can start the pipeline or the whole developement that initates from data_ingestion and ends with model_prediction. 

 - #### params.yaml
     It stores the parameter of the machine learning model or algorithm.

  - #### README.md
     This file is an outcome of displaying the projects documentation.

  - #### requirements.txt
     This file lists all the Python libraries and dependencies required to run the project.

  - #### setup.py
     This is the setup file for the project, which may include additional configuration settings.
   
  - #### template.py
     By running this file in terminal we can create a file or folder throughout the project by adding in the list.


## Getting started
 To get started with this project, follow these steps:
 

Clone the repository to your local machine using the following command:
git clone https://github.com/rachitdani/Breast-Cancer-Prediction.git
Navigate to the project directory:
cd Breast-Cancer-Prediction
Install the required dependencies using pip:
pip install -r requirements.txt
Run the Flask application:
python application.py
Open your web browser and go to
http://127.0.0.1:5001/ - to access the home page

http://127.0.0.1:5001/predict - to perform prediction on the Breast Cancer Prediction web application.

Usage
Once you have the web application running, you can use it to predict the occurence of breast cancer based on the input features. Simply provide the required information, and the application will provide you with the prediction.

Additionally, you can explore the Jupyter notebooks named EDA and Model Training in the notebooks directory to understand the data analysis and model development process.

Screenshots
Breast-Cancer-Prediction-Input Breast-Cancer-Prediction-Output
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature-name.
Make your changes and commit them: git commit -m 'Description of your changes'.
Push your changes to your fork: git push origin feature-name.
Create a pull request on the original repository.

Usage
Once you have the web application running, you can use it to predict the occurence of breast cancer based on the input features. Simply provide the required information, and the application will provide you with the prediction.

Additionally, you can explore the Jupyter notebooks named EDA and Model Training in the notebooks directory to understand the data analysis and model development process.
