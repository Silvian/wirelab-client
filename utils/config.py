import os
import json

import settings


class Config:
    CONF_FILE = "config.json"

    def load(self):
        with open(os.path.join(settings.ROOT_DIR, self.CONF_FILE), 'r') as f:
            config = json.load(f)
            return config

    def save(self, config):
        with open(os.path.join(settings.ROOT_DIR, self.CONF_FILE), 'w') as f:
            json.dump(config, f)
            return True
