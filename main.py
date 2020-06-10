from uuid import uuid4
from kiner.producer import KinesisProducer

def on_flush(count, last_flushed_at, Data=b'', PartitionKey='', Metadata=()):
    print(f"""
        Flushed {count} messages at timestamp {last_flushed_at}
        Last message was {Metadata['id']} paritioned by {PartitionKey} ({len(Data)} bytes)
    """)

def publish():
    p = KinesisProducer('wiley_stream', flush_callback=on_flush)

    for i in range(1000):

        someDict = {
            'name': 'bandara',
            'id': str(uuid4()),
        }

        p.put_record(someDict, metadata={'id': uuid4()}, partition_key='1')

    p.close()


publish()