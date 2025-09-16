# services/api_client.py
import time

class APIClient:
    """
    Mock API client for case study.
    Simulates project creation and deletion without real backend.
    """

    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url
        self._fake_db = {}  # in-memory dict to hold projects

    def create_project(self, tenant_id: str, project_name: str):
        """Simulate project creation."""
        fake_id = str(int(time.time()))
        self._fake_db[fake_id] = {"id": fake_id, "tenant_id": tenant_id, "name": project_name}
        print(f"[MOCK API] Created project {project_name} for tenant {tenant_id}")
        return self._fake_db[fake_id]

    def delete_project(self, tenant_id: str, project_id: str):
        """Simulate project deletion."""
        if project_id in self._fake_db:
            del self._fake_db[project_id]
            print(f"[MOCK API] Deleted project {project_id} for tenant {tenant_id}")
            return True
        return False
