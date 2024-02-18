
import json
import logging



def json_serializer(data):
    return json.dumps(data).encode('utf-8')

def send_msg():
    from kafka import KafkaProducer
    from faker import Faker
    fake = Faker()

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_block_ms=5000,value_serializer=json_serializer)
    try:
        producer.send('simple-kafka-msg', {
            'name': fake.name(), 
        })
    except Exception as e:
        logging.error(f'An error simple-kafka-msg occured: {e}')


send_msg()