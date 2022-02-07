#Question 1: Start date for the Yellow taxi data
#What should be the start date for this dag?
default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),#answer for the question 
    "depends_on_past": False,
    "retries": 1,
}

#Question 2: Frequency for the Yellow taxi data
#How often do we need to run this DAG?
with DAG(
    dag_id="data_ingestion_gcs_dag",
    schedule_interval="@daily",#answer for the question 
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['dtc-de'],
) as dag:

#Question 3: DAG for FHV Data
#how many DAG runs are green for data in 2019 after finishing everything?
#answer is 12 because there are 12 months in the 2019 fhv dataset

    
#Question 4: DAG for Zones
#How often does it need to run?
#only once 
with DAG(
    dag_id="data_ingestion_gcs_zones_dag",
    schedule_interval="@once",#answer for the question 
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['dtc-de'],
) as dag:

