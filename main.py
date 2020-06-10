from uuid import uuid4
from kiner.producer import KinesisProducer

def on_flush(count, last_flushed_at, Data=b'', PartitionKey='', Metadata=()):
    print(f"""
        Flushed {count} messages at timestamp {last_flushed_at}
        Last message was {Metadata['id']} paritioned by {PartitionKey} ({len(Data)} bytes)
    """)

p = KinesisProducer('stream-name', flush_callback=on_flush)

for i in range(10000):
    p.put_record(i, metadata={'id': uuid4()}, partition_key=1)

p.close()