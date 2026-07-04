import json
import logging
from confluent_kafka import Producer
from app.core.config import settings

logger = logging.getLogger(__name__)

class EventPublisher:
    def __init__(self):
        self.producer = None
        # Mock bootstrap servers for dev
        bootstrap_servers = "kafka:9092"
        
        try:
            self.producer = Producer({'bootstrap.servers': bootstrap_servers})
            logger.info("Successfully connected to Kafka")
        except Exception as e:
            logger.error(f"Failed to connect to Kafka: {e}")

    def publish_alert_triggered(self, alert_id: str, description: str, severity: str):
        if not self.producer:
            logger.warning("Kafka Producer not initialized, dropping event.")
            return

        event = {
            "event_type": "ALERT_TRIGGERED",
            "alert_id": alert_id,
            "description": description,
            "severity": severity
        }
        
        try:
            self.producer.produce("observability-events", json.dumps(event).encode('utf-8'))
            self.producer.poll(0)
            logger.info(f"Published alert event {alert_id} to Kafka")
        except Exception as e:
            logger.error(f"Error publishing to Kafka: {e}")

event_publisher = EventPublisher()
