from kafka import KafkaConsumer

consumer = KafkaConsumer("simple-kafka-msg", bootstrap_servers='localhost:9092', auto_offset_reset='earliest', enable_auto_commit=False)

for message in consumer:
    print(message.value.decode())