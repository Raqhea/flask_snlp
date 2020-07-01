# Introduction
I created this application using Flask.
The communication between web application and NLP model is constructed by tensorflow serving.
The model structure and development phase of the model can be found in [this colab notebook](https://github.com/Raqhea/DL-DS-ML/blob/master/Tensorflow%202/NLP/Sentiment%20Analysis%20RNN%20TF2.ipynb)

# Using the application

### requirements
* Tensorflow 2
* numpy
* Flask
* Flask-bootstrap
* Pickle
* Docker (with Hyper-V enabled)

After installing all the requirements, install the Tensorflow serving docker image and create an instance of the docker that points out to the model:

`docker run -p 8501:8501 --name=sentimental_analysis -v “[path to model]:/v1/models/sentimental_analysis/” -e MODEL_NAME=sentimental_analysis tensorflow/serving`

__explaination__:

`-p 8501:8501`: specifies the port that Tensorflow Server works, the part after ":" is for Docker serving,

`--name=sentimental_analysis`: the name for the docker instance,

`-v "[path to model]:/v1/models/sentimental_analysis/" `: mount given path to `/v1/models/sentimental_analysis/` in docker container

`-e MODEL_NAME=sentimental_analysis`: set MODEL_NAME environment variable to model name. MODEL_NAME must be same with the name in /v1/models/__sentimental_analysis__/

and at last specify the tensorflow serving docker image to download

When you done with setting the docker instance, it's time to run the flask server.
It can be done by running `python app.py` in command line inside of the application directory.
Then you should be able to use the application.
