"""
Configuration file. Please prefix application specific config values with
the application name.
"""
EXTENSIONS = [
    'adsws.ext.ratelimiter'
]

FEEDBACK_SLACK_END_POINT = 'https://hooks.slack.com/services/TOKEN/TOKEN'
GOOGLE_RECAPTCHA_ENDPOINT = 'https://www.google.com/recaptcha/api/siteverify'
GOOGLE_RECAPTCHA_PRIVATE_KEY = 'MY_PRIVATE_KEY'
CORS_DOMAINS = ['https://ui.adsabs.harvard.edu']
CORS_HEADERS = []
CORS_METHODS = ['POST', 'GET']