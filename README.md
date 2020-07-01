### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Web Application](#webapp)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The only requirements are Python 3.* and Jupyter Notebooks.

Libraries used:
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- sklearn
- scipy
- flask
- joblib

## Project Motivation<a name="motivation"></a>

Buying and selling a home is an important part of most people's life and can often be a stressful and confusing time. Understanding the true value of a home is paramount in determing when to go forward with a sale. Realtors often use comps of recent sales to set a baseline for the pricing. These calculations often ignore many features of the home and only focus on the location and square footage. This project examines whether or not there is a data driven way of calculating the value of a home using comprehensive features of a home. The dataset used is the Ames housing dataset. It is a modernized and expanded version of the often cited Boston Housing dataset. The dataset includes 79 variables describing residential homes in Ames, Iowa. A Jupyter notebook is included to explore the data, clean it, visualize it, create/evaulate an optimal model, and evaluate the results. A web application is included in this project for testing the generated model.

The project follows the following strategy to solve the problem:

- Data understanding
  - Explore the data
  - What features do we have available in the dataset
  - Look for missing values and outliers
- Prepare the data
  - Convert invalid data types
  - Remove extraneous columns
  - Imputation on missing values
  - Remove outliers.
- Create a model
  - Split the cleaned dataset into training and testing dataframes
  - Select 5-6 model types and evaulate them using the default parameters
  - Once the best model is select, use hyperparameter tuning to further improve the results
- Evaluate the results
  - Is the model sufficient in solving the problem defined above?

The following metrics will be used to determine the accuracy of the models:
- `mean_absolute_error`: The mean error when comparing our predicted test values versus observed values from our model. This metric is useful in determing the accuracy of regression predictions.
- `explained_variance_score`: The proportion to which a model accounts for the variation (dispersion) of a given dataset. That is, how well does the model explain our dataset, ignoring error variance.

## Results

The dataset had multiple columns that were using incorrect data types and these were converted. Extraneous columns were removed and missing values were replaced. Outliers for multiple continuous features were removed using z-scores above 2. Our dataset was split on a 75% training 25% test split. 5 models were evaluated:

`HuberRegressor` Mean absolute error: 28645.7134<br/>
`HuberRegressor` Explained variance score: 0.6690

`TheilSenRegressor` Mean absolute error: 16422.3780<br/>
`TheilSenRegressor` Explained variance score: 0.8734

`GradientBoostingRegressor` Mean absolute error: 17265.7066<br/>
`GradientBoostingRegressor` Explained variance score: 0.8658

`RandomForestRegressor` Mean absolute error: 18778.2564<br/>
`RandomForestRegressor` Explained variance score: 0.8431

`AdaBoostRegressor` Mean absolute error: 22949.2128<br/>
`AdaBoostRegressor` Explained variance score: 0.7968

The `TheilSenRegressor` model was the best performing using the default parameters. After hyperparameter tuning the final parameters used were:

```
{'max_iter': 500, 'max_subpopulation': 1000, 'tol': 0.0001}
```

The final trained model produced a mean absolute error of 16298.2640. This is 9% of the median sale price. In the real world this means our model has a mean error of approximately $16,300 for each prediction. This number seem reasonable given the smallish dataset (~1500). The explained variance score of 0.8739 shows our model does well in accounting for the variation of our given data set. It accounts for 87.39% of the variance in our test dataset. Our model can be used as a baseline for initially evaluating the price of a house to rule out outliers. In future analysis, we could use a larger dataset or explore other classifier types or ensemble methods to improve the results.


The model was exported and can be used by end users in the included web application to predict housing prices based on multiple house features.

## File Descriptions <a name="files"></a>

- `dsnd-capstone.ipynb`
  Jupyter Notebook showing all calculations, visualizations, and models
- `README.md`
  Read me file that communications the project motivation
- `data/data_description.txt`
  Describes the columns and available values in the dataset
- `data/data.csv`
  Ames housing dataset
- `models/classifier.pkl`
  Generated model
- `columns.json`
  List of final column names used by the model
- `parameters.json`
  JSON version of `data_description.txt` for programmatic use
- `webapp/run.py`
  Web application backend
- `webapp/templates/index.html`
  Web application home page
- `webapp/templates/run.html`
  Web application results page

## Web Application<a name="webapp"></a>

To run the web application, traverse to the `webapp` directory and run `python run.py`.

## Github Link

https://github.com/kfrost-ibm/dsnd-capstone

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

License and information about the dataset can be found [here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data).
