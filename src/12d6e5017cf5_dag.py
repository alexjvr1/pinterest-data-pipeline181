from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator, DatabricksRunNowOperator
#from datetime import datetime as dt
#from datetime import timedelta 
import datetime as dt

#Define params for Submit Run Operator
notebook_task = {
    'notebook_path': '/Users/alexjvr@gmail.com/Pinterest_Data_Processing',
}


#Define params for Run Now Operator
notebook_params = {
    "Variable":5
}


default_args = {
    'owner': '12d6e5017cf5',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': dt.timedelta(minutes=2)
}


with DAG('12d6e5017cf5_dag',
    # should be a datetime format
    start_date=dt.datetime(2024, 3, 17),
    # check out possible intervals, should be a string
    schedule_interval='@daily',
    catchup=False,
    default_args=default_args
    ) as dag:


    opr_submit_run = DatabricksSubmitRunOperator(
        task_id='submit_run',
        # the connection we set-up previously
        databricks_conn_id='databricks_default',
        existing_cluster_id='1108-162752-8okw8dgg',
        notebook_task=notebook_task
    )
    opr_submit_run
