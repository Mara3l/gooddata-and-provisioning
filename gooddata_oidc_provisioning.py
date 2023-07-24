from auth0.authentication import GetToken
from auth0.management import Auth0

domain = "dev-26ul4jwh.us.auth0.com"
non_interactive_client_id = "umbPo7gVESWX3uztvJ1I4pxWyGcjMjEd"
non_interactive_client_secret = "zUQeJwNzBB8chWRPIN5kA3Z1ogE3DvBshmRkf-J8Q4p5ZdXyrLsry7afFW3YIimW"

get_token = GetToken(domain, non_interactive_client_id, client_secret=non_interactive_client_secret)
token = get_token.client_credentials("https://{}/api/v2/".format(domain))
mgmt_api_token = token["access_token"]

auth0 = Auth0(domain, mgmt_api_token)
users = auth0.users

print(users.list())
