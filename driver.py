import sys

import get_env_variable as gav
from create_spark import get_spark_object
from validate import get_current_date
import logging
import logging.config

logging.config.fileConfig('Properties/Configuration/logging.config')


def main():
    try:
        logging.info('i am in the main  method')
        #print(gav.header)
        #print(gav.inferSchema)
        logging.info('calling spark object')

        spark = get_spark_object (gav.envr , gav.appName)

        logging.info('object created..', spark)
        logging.info('validating spark object')
        get_current_date(spark)

    except Exception as exp:
        logging.error("An error ocurred when calling main() please check the trace == ", str(exp))
        sys.exit(1)


if __name__ == '__main__':
    main()
    logging.info('Application done')