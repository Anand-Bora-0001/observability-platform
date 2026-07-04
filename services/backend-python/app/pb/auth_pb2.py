# Placeholder for auth_pb2.py
class ValidateTokenRequest:
    def __init__(self, token=None):
        self.token = token

class ValidateTokenResponse:
    def __init__(self, is_valid=False, user_id="", email="", roles=None, organization_id="", error_message=""):
        self.is_valid = is_valid
        self.user_id = user_id
        self.email = email
        self.roles = roles or []
        self.organization_id = organization_id
        self.error_message = error_message
