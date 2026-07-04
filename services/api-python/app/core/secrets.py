import logging
import json
from app.core.config import settings

logger = logging.getLogger(__name__)

class AWSSecretsManagerMock:
    def __init__(self):
        self.region = "us-east-1"
        logger.info("Initialized AWS Secrets Manager client (Mock)")

    def get_database_credentials(self):
        try:
            # Mock retrieving credentials from AWS Secrets Manager
            logger.info("Fetching database credentials from AWS Secrets Manager...")
            mock_secret = {
                "username": "admin",
                "password": "adminpassword",
                "engine": "postgres",
                "host": "observability-db",
                "port": 5432,
                "dbname": "observability"
            }
            return mock_secret
            
        except Exception as e:
            logger.error(f"Failed to fetch secrets from AWS Secrets Manager: {e}")
            return None

secrets_manager = AWSSecretsManagerMock()
