# Machine learning model integration with Elasticsearch in Api Rest
    
Do you like wines but you don't know how to give your opinion about their quality?
The solution to this problem has been the integration of a machine learning model as an Api Rest full, in which, by introducing the different quality parameters, the model returns a number and a comment indicating whether it is high, medium or low quality.

After that, the information of the parameters and quality are saved in database with Elastic Search(just in case).

- Rest: is any interface between systems that uses HTTP to obtain data or generate operations on that data in all possible formats, such as XML and JSON.
- Supervised Model: the algorithms used for this type of learning require that each one of the instances used during the training process has an attribute
- ElasticSearch: is a search engine based on Lucene:
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
  
  - fixed acidity

  - volatile acidity

  - citric acid

  - residual sugar

  - chlorides

  - free sulfur dioxide

  - total sulfur dioxide

  - density

  - pH

  - sulphates

  - alcohol
  
Output variable (based on sensory data):

  - quality (score between 0 and 10)
  
 - RUN 'python3 main.py'
 - curl -X POST http://0.0.0.0:5000/model -H 'content-type: application/json' -d\ '{"fixed acidity": 7.4, "volatile acidity": 0,6, "citric acid": 0, "residual sugar": 1, "chlorides": 0.02, "free sulfur dioxide": 11, "total sulfur dioxide": 11, "density": 0.99, "ph": 3, "sulphates": 0.5, "alcohol": 9,4}'
- output: {"quality":"Medium Quality","value":4.32}




