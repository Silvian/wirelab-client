import os
import json

import settings


class Config:

    def __init__(self, config=settings.CONFIG_FILE, root_dir=settings.ROOT_DIR):
        self.config = config
        self.root_dir = root_dir

    def load(self):
        with open(os.path.join(self.root_dir, self.config), 'r') as file:
            config = json.load(file)
            return config

    def save(self, config):
        with open(os.path.join(self.root_dir, self.config), 'w') as file:
            json.dump(config, file)
            return True
