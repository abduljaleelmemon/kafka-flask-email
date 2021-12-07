from app import *
import smtplib
from threading import Thread 
import datetime
from app.model.email import email_db
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

temp = redis_client.get('name')
print(temp)

@app.route('/')
def index():
    return 'hello world'

@app.route('/about')
def about():
    return 'abdul jalil'

def add_email(sender, reciever, website, status):
    email = email_db(sender = sender, recipient = reciever, status = status, time = datetime.datetime.now(), website = website)
    db.session.add(email)
    db.session.commit()
    
def send_email(username, reciever, website, status):
    # content
    add_email(sender = 'anon.non.exe@gmail.com', reciever = reciever, website = website, status = status)
    sender = "anon.non.exe@gmail.com"
    password = ""
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender, password)
    alert_msgs = 'Hello, {}\nStatus: {}\nWebsite: {}'.format(username, 
                                            str(status),
                                            website)
    mail.sendmail(sender, reciever, str(alert_msgs))
    mail.close()

def consumer():
    from kafka import KafkaConsumer
    import json
    consumer = KafkaConsumer("registered_user", 
    bootstrap_servers='localhost:9092',
    api_version=(0,11,5),
    auto_offset_reset='earliest',
    group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        temp = json.loads(msg.value)
        send_email(temp['username'], temp['email'], temp['website'], temp['status'])

threadz = Thread(target = consumer, args = [])
threadz.start()
print("thread finished...exiting")
