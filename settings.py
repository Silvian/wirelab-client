"""Wirelab Client Settings."""
import os

from dotenv import load_dotenv

# load_dotenv will look for a .env file and if it finds one
# it will load the environment variables from it

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()

# AWS QUEUE
AWS_QUEUE = os.getenv("AWS_QUEUE", default="https://example.com/queue")

# AWS access configurations
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME", default="eu-west-1")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", default="AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", default="AWS_SECRET_KEY")

# Webhook configurations
WEBHOOK_URL = os.getenv("WEBHOOK_URL", default="https://example.com/webhook")
WEBHOOK_KEY = os.getenv("WEBHOOK_KEY", default="secret-key")
