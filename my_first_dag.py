# Importando as bibliotecas que vamos usar nesse exemplo

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

# Definindo alguns argumentos básicos

default_args = {
   'owner': 'pablo_brenner',
   'depends_on_past': False,
   'start_date': datetime(2019, 1, 1),
   'retries': 0,
   }
   
# Nomeando a DAG e definindo quando ela vai ser executada (você pode usar argumentos em Crontab também caso queira que a DAG execute por exemplo todos os dias as 8 da manhã) 

with DAG(
   'my-first-dag-Alterada',
   schedule_interval=timedelta(minutes=1),
   catchup=False,
   default_args=default_args
   ) as dag:   

   # Definindo as tarefas que a DAG vai executar, nesse caso a execução de dois programas Python, chamando sua execução por comandos bash

   t1 = BashOperator(
      task_id='first_etl',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etl_scripts/
      python3 my_first_etl_script.py
      """)

   t2 = BashOperator(
      task_id='second_etl',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etl_scripts/
      python3 my_second_etl_script.py
      """)

   # Definindo o padrão de execução, nesse caso executamos t1 e depois t2
   t1 >> t2