import json
import os

class Storage:
    def __init__(self):
        self.file_path = "data/users.json"
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.users = self._load_data()
    
    def _load_data(self):
        try:
            with open(self.file_path) as f:
                return json.load(f).get('users', [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def add_user(self, user_id):
        if user_id not in self.users:
            self.users.append(user_id)
            self._save_data()
    
    def get_users(self):
        return self.users
    
    def _save_data(self):
        with open(self.file_path, 'w') as f:
            json.dump({'users': self.users}, f)
