import os

DEVELOPMENT = "development"
PRODUCTION = "production"
print("Reading environment variables")
env = os.environ.get("ENV_NAME", DEVELOPMENT)

print(env)
