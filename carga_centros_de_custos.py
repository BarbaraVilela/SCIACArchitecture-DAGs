# Importando as Bibliotecas necessárias
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# Definindo alguns argumentos básicos
default_args = {
   'owner': 'Bárbara Vilela',
   'depends_on_past': False,
   'start_date': datetime(2022, 1, 1),
   'retries': 0,
   }
   
# Nomeando a DAG e definindo quando será executada
with DAG(
   'carga_centros_de_custos',
   schedule_interval=timedelta(minutes=1),
   catchup=False,
   default_args=default_args
   ) as dag:   

   # Definindo as tarefas a serem executadas

   t1 = BashOperator(
      task_id='busca_centros_de_custos',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etl_scripts/
      python3 busca_centros_de_custos.py
      """)

   t2 = BashOperator(
      task_id='first_etl',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etl_scripts/
      python3 my_first_etl_script.py
      """)

   # Definindo o padrão de execução
   t1 >> t2