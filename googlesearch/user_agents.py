import random
from fake_useragent import UserAgent

# Create a UserAgent object
user_agent = UserAgent()

def get_useragent():
    return user_agent.random

