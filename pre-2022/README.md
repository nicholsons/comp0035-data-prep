# Data cleansing activity for COMP0035

## Getting started
This activity uses a Jupyter notebook. You can either install code that allows you to use Jupyter notebooks locally on your computer or use a cloud-hosted version. 

Once you have the notebook open using one of the following methods, you should follow the instructions in the notebook itself.

### 1. Using the notebook in the Binder cloud service
Binder does not require you to create an account nor do you need to install any software on your computer. You can access the notebook using [Binder](https://mybinder.org) at [https://mybinder.org/v2/gh/nicholsons/comp0035_cleansing.git/master](https://mybinder.org/v2/gh/nicholsons/comp0035_cleansing.git/master).  

Be patient, Binder takes a few minutes to start the container. Once it is ready, click on data_cleaning.ipynb to start. Once the Jupyter notebook is open, read and follow the instructions in the notebook.

You will be able to make changes to the code during your Binder sessions and see the effect of your changes, however when you exit Binder any changes that you have made will not be saved. If you wish to save changes that you make to access at another time then the menu bar within the Binder session provides an option to download the notebook to your computer.

### 2. Using the notebook in PyCharm
Clone the repository in PyCharm
Go to preferences and add a new venv
Install jupyter, numpy, pandas, matplotlib and xlrd in the venv


### 3. Using a locally installed Python Jupyter notebook environment (not PyCharm)
If you already have a locally installed Python development environment and code editor then you may be able to work out how to use Jupyter notebooks on your own machine. 
For example, if you are using [Visual Studio Code, you can work with Jupyter notebooks in the IDE](https://code.visualstudio.com/docs/python/jupyter-support). 
You will need to investigate options for doing this yourself depending on your own setup. 
You may need to install numpy, pandas and matplotlib in your local environment which you should be able to do with pip, e.g. 
```python
pip install jupyter
pip install numpy
pip install pandas
pip install matplotlib
pip install xlrd
```

## Feedback and corrections
This notebook is maintained at [https://github.com/nicholsons/comp0035_cleansing](https://github.com/nicholsons/comp0035_cleansing). 

Please report suggestions or errors at [https://github.com/nicholsons/comp0035_cleansing/issues](https://github.com/nicholsons/comp0035_cleansing/issues).

This notebook was developed by [Sarah Sanders](mailto:sarah.sanders@ucl.ac.uk).

## Acknowledgements
The idea for this activity was inspired by an artile published in the Centre for Global Development by Shelby Carvalho and Lee Crawfurd on 25th March 2020 called [School’s Out: Now What?](https://www.cgdev.org/blog/schools-out-now-what).

The data set used is that referred to in the article and was made [publicly available here by the Centre for Global Development]( https://docs.google.com/spreadsheets/d/1ndHgP53atJ5J-EtxgWcpSfYG8LdzHpUsnb6mWybErYg/edit?ts=5e6f893e#gid=0). The data set builds on UNESCO data on global school closures and gives detail about the closures and other support countries are providing whilst schools are closed.

## Data protection and privacy
You should not put any personal data in an online notebook, that is, do not include details that could allow you to be identified or information about yourself that you would not wish to be seen by others.

[Information on privacy for the Binder service can be found here](https://mybinder.readthedocs.io/en/latest/faq.html).