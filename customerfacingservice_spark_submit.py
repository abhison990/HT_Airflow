from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.utils.dates import days_ago
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import halo_variables

environment_default_args = {
	"owner": "airflow",
	"depends_on_past": False,
	#"start_date": date(2020, 7, 24),
	"start_date": days_ago(1),
	"retries":0,
    "schedule_interval": "* */2 * * *",
}


dag = DAG("customerfacingservice_spark_submit", default_args=environment_default_args, concurrency=5, max_active_runs=1)


create_command = "/home/airflow/wifi_uc/cfs.sh "

task1 = SSHOperator(
	    ssh_conn_id="ssh_dev_conn",
	    command=create_command,
	    task_id="spark_ssh",
        dag=dag
)
