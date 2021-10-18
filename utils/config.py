import json


class Config:
    CONF_FILE = "config.json"

    def load(self):
        with open(self.CONF_FILE, 'r') as f:
            config = json.load(f)
            return config

    def save(self, config):
        with open(self.CONF_FILE, 'w') as f:
            json.dump(config, f)
            return True
