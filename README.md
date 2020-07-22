# Data cleansing activity for COMP0035

## Getting started
This activity uses a cloud service Jupyter notebook. When you open one of the following links, the cloud service creates a virtual coding environment in the cloud for you to use so you don't need to install anything on your machine. It will take a few minutes for this 'environment' to be created, once it is ready you will see a page that looks a little like this one.

Once you have the notebook open using one of the following methods, you should follow the instructions in the notebook itself.

### 1. Using the notebook in the Binder cloud service (no account required, no ability to save changes)
If you do not want to create an account then you can access the notebook using [Binder](https://mybinder.org) at [https://mybinder.org/v2/gh/nicholsons/cs_incoming_datavis.git/master?filepath=incoming_students_data_visualisation.ipynb](https://mybinder.org/v2/gh/nicholsons/cs_incoming_datavis.git/master?filepath=incoming_students_data_visualisation.ipynb).  

You will be able to make changes to the code during your Binder sessions and see the effect of your changes, however when you exit Binder any changes that you have made will not be saved. If you wish to save changes that you make to access at another time then the menu bar within the Binder session provides an option to download the notebook to your computer.

**Azure is being retired on 9th October, need to find an alternative**
### 2. Using the notebook in the Microsoft Azure Notebook cloud service (free account required, ability to save changes)
To use the notebook interactively and save your changes, create an account on [https://notebooks.azure.com](https://notebooks.azure.com). 

Access the notebook hosted on the Microsoft Azure cloud service at:
[https://notebooks.azure.com/snicholson/projects/data-cleaning](https://notebooks.azure.com/snicholson/projects/data-cleaning)

First you should 'clone' the notebook. To do this, after clicking the above link, click on the link to the notebook ('incoming_students_data_visualisation.ipynb'). You should see a button towards the top of the screen with the word 'clone'. Press this to create a copy. If you are not already logged in to Microsoft Azure Notebooks and you didn't already create an account, then you will be prompted to create an account now. You may need to wait a few minutes during which a copy of the notebook is made and the 'environment' is created for you. This process may be quite quick and it may not be obvious that the clone has completed, when it has finished you should see a message near the top of the screen that says '```Cloned from https://github.com/nicholsons/cs_incoming_datavis'```.

### 3. Using a locally installed Python Jupyter notebook environment
If you already have a locally installed Python development environment and code editor then you may be able to work out how to use Jupyter notebooks on your own machine. For example, if you are using [Visual Studio Code, you can work with Jupyter notebooks in the IDE](https://code.visualstudio.com/docs/python/jupyter-support). 
You will need to investigate options for doing this yourself depending on your own setup. 
You will need to install numpy, pandas and matplotlib in your local environment which you should be able to do with pip, e.g. 
```python
pip install numpy
pip install pandas
pip install matplotlib
```

## Feedback and corrections
This notebook is maintained at [https://github.com/nicholsons/comp0035_cleansing](https://github.com/nicholsons/comp0035_cleansing). 

Please report suggestions or errors at [https://github.com/nicholsons/comp0035_cleansing/issues](https://github.com/nicholsons/comp0035_cleansing/issues).

This notebook was developed by [Sarah Sanders](mailto:sarah.sanders@ucl.ac.uk).

## Acknowledgements
The idea for this activity was inspired by an artile published in the Centre for Global Development by Shelby Carvalho and Lee Crawfurd on 25th March 2020 called [School’s Out: Now What?](https://www.cgdev.org/blog/schools-out-now-what).

The data set used is that referred to in the article and was made [publicly available here by the Centre for Global Development]( https://docs.google.com/spreadsheets/d/1ndHgP53atJ5J-EtxgWcpSfYG8LdzHpUsnb6mWybErYg/edit?ts=5e6f893e#gid=0). The data set builds on UNESCO data on global school closures and gives detail about the closures and other support countries are providing whilst schools are closed.

## Data protection and privacy
You should not put any personal data in your notebook, that is, do not include details that could allow you to be identified or information about yourself that you would not wish to be seen by others.

[Information on privacy for the Binder service can be found here](https://mybinder.readthedocs.io/en/latest/faq.html).

[Information on privacy for the Microsoft Azure Notebooks service can be found here](https://privacy.microsoft.com/en-gb/privacystatement).

