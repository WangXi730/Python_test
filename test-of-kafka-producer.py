#导入kafkaproducer
from kafka import KafkaProducer
#创建生产者对象
producer = KafkaProducer(bootstrap_servers='192.168.190.128:9092,192.168.190.128:9093,192.168.190.128:9094')
#循环发送消息
while True:
    str = input('请输入：')
    if str=='end':
        break
    producer.send('my_topic',value=str.encode('utf-8'))

#将所有缓冲区的消息发送
producer.flush()
#关闭producer
producer.close()

