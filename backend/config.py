from authx import AuthXConfig


jwt_config = AuthXConfig()
jwt_config.JWT_SECRET_KEY = 'your_secret_key'
jwt_config.JWT_ACCESS_COOKIE_NAME = 'access_token'
jwt_config.JWT_TOKEN_LOCATION = ['cookies']

