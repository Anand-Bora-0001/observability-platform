import json
import logging
import asyncio
from confluent_kafka import Consumer, Producer
import os
import threading

logger = logging.getLogger(__name__)

def start_kafka_consumer():
    consumer = Consumer({
        'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092'),
        'group.id': 'ai-ops-group',
        'auto.offset.reset': 'earliest'
    })
    
    producer = Producer({
        'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
    })

    consumer.subscribe(['observability-events'])
    logger.info("AI Ops Consumer started listening to 'observability-events'")

    while True:
        msg = consumer.poll(1.0)
        
        if msg is None:
            continue
        if msg.error():
            logger.error(f"Consumer error: {msg.error()}")
            continue

        try:
            payload = json.loads(msg.value().decode('utf-8'))
            if payload.get("event_type") == "ALERT_TRIGGERED":
                alert_id = payload.get("alert_id")
                desc = payload.get("description", "")
                
                logger.info(f"Received ALERT_TRIGGERED for {alert_id}")
                
                # Mock RCA generation
                rca_result = {
                    "event_type": "RCA_COMPLETED",
                    "alert_id": alert_id,
                    "hypothesis": f"AI Hypothesis for: {desc}"
                }
                
                producer.produce("observability-rca", json.dumps(rca_result).encode('utf-8'))
                producer.poll(0)
                logger.info(f"Published RCA_COMPLETED for {alert_id}")
                
        except Exception as e:
            logger.error(f"Error processing message: {e}")

def run_consumer_in_background():
    thread = threading.Thread(target=start_kafka_consumer, daemon=True)
    thread.start()
