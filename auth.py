from google_auth_oauthlib.flow import InstalledAppFlow
from config import GOOGLE_REDIRECT_URI  # Ensure this is correctly defined

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
CLIENT_SECRETS_FILE = 'client_secret.json'

flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    scopes=SCOPES
)

# Optionally, you can set it this way too:
flow.redirect_uri = GOOGLE_REDIRECT_URI

# Now also pass it explicitly to authorization_url()
auth_url, _ = flow.authorization_url(prompt='consent', redirect_uri=GOOGLE_REDIRECT_URI)

print("Please visit this URL to authenticate:")
print(auth_url)
