from pyspark.sql import SparkSession
import logging.config
def get_spark_object(envr,appName):
    try:
        if envr == 'DEV':
            master = 'local'

        else:
            master = 'Yarn'

        spark = SparkSession.builder.master(master).appName(appName).getOrCreate()
        return spark


    except Exception as exp:
        print(str(exp))