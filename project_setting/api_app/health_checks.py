from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException
from health_check.plugins import plugin_dir


class HealthCheckBackendVersion(BaseHealthCheckBackend):
    critical_service = False

    def check_status(self):
        return super().check_status()
    
    def pretty_status(self):
        return super().pretty_status()
    
    def identifier(self):
        return super().identifier()

def register_health_checks():
    plugin_dir.register(HealthCheckBackendVersion)