import time
from google.cloud import bigtable

project_id='speedy-victory-336109'
instance_id='ssdinstance'
table_id='my-table'

client = bigtable.Client(project=project_id, admin=True)
instance = client.instance(instance_id)
table = instance.table(table_id)

row_key = "phone#4c410523#20190573"


for i in range(1,2000):
    time.sleep(0.5)
    print(str(i))
    print(table.read_row(row_key))
