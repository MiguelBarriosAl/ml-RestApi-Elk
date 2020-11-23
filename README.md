# ml_restApi_elk
Machine learning model integration with Elasticsearch in Api Rest
    
Do you like wines but you don't know how to give your opinion about their quality?
The solution to this problem has been the integration of a machine learning model as an Api Rest full, in which, by introducing the different quality parameters, the model returns a number and a comment indicating whether it is high, medium or low quality.

After that, the information of the parameters and quality are saved in database with Elastic Search(just in case).

Rest: is any interface between systems that uses HTTP to obtain data or generate operations on that data in all possible formats, such as XML and JSO.
Supervised Model: the algorithms used for this type of learning require that each one of the instances used during the training process has an attribute
ElasticSearch: is a search engine based on Lucene:
   - ES implements a distributed search server, in which a single server can respond to
     multiple clients.
   - Documents and settings can be modified and manipulated via HTTP queries.
   - It also works with JSON format files.
   
   
The project is composed by:

  - Model.py: Machine Learning model development and training with the tagged data. Later the model is stored in rf_model.pickle
  - app/rf_model.pickle:  Random Forest Regression model stored for later implementation in main.py
  - app/main.py: Development of Api Rest with implementation of Machine Learning Random Forest model and subsequent storage in ElasticSearch
  - data: winequality-red.csv
  - requirements.txt
  
Data:
Input variables (based on physicochemical tests):
  1 - fixed acidity

  2 - volatile acidity

  3 - citric acid

  4 - residual sugar

  5 - chlorides

  6 - free sulfur dioxide

  7 - total sulfur dioxide

  8 - density

  9 - pH

  10 - sulphates

  11 - alcohol

  Output variable (based on sensory data):

  12 - quality (score between 0 and 10)



