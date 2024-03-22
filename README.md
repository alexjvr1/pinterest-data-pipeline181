# pinterest-data-pipeline181

## Project Description

Aim: Extract, transform and load data from pinterest using batch processing (AWS MWAA) and streaming (Kinesis)

This pipeline extracts data in batches from an RDS database using Kafka. These data are stored in an AWS S3 bucket. 
The data are then transformed in Databricks, and a batch processing pipeline is set up in AWS MWAA to manage a scheduled (daily) triggering of the pipeline. The final tables are queried for various questions of interest to the business. 

A second pipeline is created as a streaming alternative to the batch processing above. Here data are retrieved from the RDS database and sent to Kinesis streams. The data are then imported to Databricks to be transformed and cleaned, and saved as delta tables to be queried. 

## Quick start

Clone the repository: 
```
git clone https://github.com/alexjvr1/pinterest-data-pipeline181/tree/main
```

Python modules required for dowloading data: 
```
## The pipeline was created in Python 3.9.5 
Package            Version
------------------ ------------
boto3              1.34.2
json               2.0.9
multiprocessing    0.70.16
pandas             2.1.4
psycopg2           2.9.9
SQLAlchemy         2.0.23
requests           2.31.0
yaml               6.0.1
```


## Usage instructions

The src/ directory contains all the scripts. The step by step pipeline is documented in __main__.py.

```
python __main__.py
```

## Data processing and querying in Databricks is shown in two iPython Notebooks: 

Pinterest_Data_Processing_Batch_Data.ipynb: Batch processing, transforming, and querying the data

Pinterest_Data_Processing_Streaming_Data.ipynb: Streaming and transforming the data, and saving the output as Delta tables





## Licence information

GNU GPLv3

