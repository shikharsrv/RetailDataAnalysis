import os

os.environ['envr'] = 'DEV'
os.environ['inferSchema'] = 'True'
os.environ['header'] = 'True'

header = os.environ['header']
inferSchema = os.environ['inferSchema']
envr = os.environ['envr']

appName = 'Youtube Pyspark'

current = os.getcwd()


src_olap = current + '/Source/olap'

src_oltp = current + '/Source/oltp'

