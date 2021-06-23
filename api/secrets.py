from imgurpython import ImgurClient

# If you already have an access/refresh pair in hand
client_id = '9b315a3d4a73278'
client_secret = '6ea5304b64c0ce2d995277b3a125f752a059ca1c'
access_token = 'bf69af937f3e5a129dfa5d0b665f6eefff6e1af2'
refresh_token = 'a892e7545a3174914f55ecf4b1e210fc78f27f2c'

# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
client = ImgurClient(client_id, client_secret, access_token, refresh_token)