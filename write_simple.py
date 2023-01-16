import datetime
import time
from google.cloud import bigtable

project_id='speedy-victory-336109'
instance_id='ssdinstance'
table_id='my-table'

client = bigtable.Client(project=project_id, admin=True)
instance = client.instance(instance_id)
table = instance.table(table_id)
column_family_id = "cf1"

for i in range(1,2000):
    timestamp = datetime.datetime.utcnow()
    row_key = "phone#4c410523#" + str(20190501+i)
    row = table.direct_row(row_key)
    row.set_cell(column_family_id, "connected_cell", 1, timestamp)
    row.set_cell(column_family_id, "connected_wifi", 1, timestamp)
    row.set_cell(column_family_id, "os_build", "PQ2A.190405.003", timestamp)
    row.commit()
    print(str(i))
    print("Successfully wrote row {}.".format(row_key))
    time.sleep(0.5)
