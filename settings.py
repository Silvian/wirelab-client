"""Wirelab Client Settings."""
import os

from dotenv import load_dotenv

# load_dotenv will look for a .env file and if it finds one
# it will load the environment variables from it

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()

# Config file:
CONFIG_FILE = "config.json"

# AWS QUEUE
AWS_QUEUE = os.getenv("AWS_QUEUE", default="https://example.com/queue")

# AWS access configurations
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME", default="eu-west-1")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", default="AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", default="AWS_SECRET_KEY")

# Devices configurations
DEVICES_URL = os.getenv("DEVICES_URL", default="https://example.com/list-devices")
DEVICES_KEY = os.getenv("DEVICES_KEY", default="secret-key")

# Status configuration
STATUS_URL = os.getenv("STATUS_URL", default="https://example.com/update-status")
STATUS_KEY = os.getenv("STATUS_KEY", default="secret-key")

# House code configurations
HOUSE_CODE = os.getenv("HOUSE_CODE", default="12345")
