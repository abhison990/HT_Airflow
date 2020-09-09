export spark_version=2.3
USER_HOME=/home/airflow/wifi_uc

spark2-submit --master yarn --deploy-mode cluster --files $USER_HOME/config_param.json \
			  --driver-memory 4g --num-executors 3 --executor-cores 6 --executor-memory 12g \
			  --keytab /home/airflow/keytab/tsystems_asondkar.keytab \
		      --principal tsystems_asondkar@CDHDEV1.DC.HT.HR \
             $USER_HOME/customerfacingservice.py
			 