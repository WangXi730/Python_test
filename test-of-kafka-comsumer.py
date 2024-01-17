from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic', bootstrap_servers='192.168.190.128:9092,192.168.190.128:9093,192.168.190.128:9094', group_id='my_group',auto_offset_reset='earliest')
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
