import os
from auth0.authentication import GetToken
from auth0.management import Auth0
from gooddata_sdk import GoodDataSdk, CatalogUserGroup, CatalogDeclarativeWorkspacePermissions, CatalogUser
from typing import List

auth0_domain = os.getenv("AUTH0_DOMAIN")
auth0_non_interactive_client_id = os.getenv("AUTH0_CLIENT_ID")
auth0_non_interactive_client_secret = os.getenv("AUTH0_SECRET")
auth0_token = GetToken(
    auth0_domain,
    auth0_non_interactive_client_id,
    client_secret=auth0_non_interactive_client_secret
).client_credentials("https://{}/api/v2/".format(auth0_domain))
auth0_mgmt_api_token = auth0_token["access_token"]
auth0 = Auth0(auth0_domain, auth0_mgmt_api_token)

gooddat_host = os.getenv("GOODDATA_HOST")
gooddata_token = os.getenv("GOODDATA_TOKEN")
gooddata_workspace_id = os.getenv("GOODDATA_WORKSPACE_ID")
gooddata_sdk = GoodDataSdk.create(gooddat_host, gooddata_token)


def get_auth0_users():
    return auth0.users.list()


def get_auth0_user_role(auth_id: str):
    return auth0.users.list_roles(auth_id)


def create_user_groups():
    # adminGroup already exists, it means that only userGroup needs to be created
    user_group = CatalogUserGroup.init(user_group_id="userGroup")
    gooddata_sdk.catalog_user.create_or_update_user_group(user_group=user_group)


def create_permissions():
    admin_group_permissions = {
        "name": "MANAGE",
        "assignee": {
            "id": "adminGroup",
            "type": "userGroup"
        }
    }
    user_group_permissions = {
        "name": "VIEW",
        "assignee": {
            "id": "userGroup",
            "type": "userGroup"
        }
    }
    permissions_for_admins = CatalogDeclarativeWorkspacePermissions.from_dict(admin_group_permissions)
    permissions_for_users = CatalogDeclarativeWorkspacePermissions.from_dict(user_group_permissions)

    gooddata_sdk.catalog_permission.put_declarative_permissions(gooddata_workspace_id, permissions_for_admins)
    gooddata_sdk.catalog_permission.put_declarative_permissions(gooddata_workspace_id, permissions_for_users)


def create_or_update_user(user_id: str, authentication_id: str, user_group_ids: List[str]):
    gooddata_sdk.catalog_user.create_or_update_user(
        CatalogUser.init(
            user_id,
            authentication_id,
            user_group_ids
        )
    )


def provision_users():
    users = get_auth0_users()

    for user in users["users"]:
        # user_id is the authentication_id in this case, it is auth0|<user_id>
        auth_id = user["user_id"]
        user_id = auth_id.replace("auth0|", "")
        # user can have assigned more roles, I assigned just one
        role = get_auth0_user_role(auth_id)["roles"][0]
        role_name = role["name"]

        # if user has an admin role, it is assigned to adminGroup
        if role_name == "Admin":
            create_or_update_user(user_id, auth_id, ["adminGroup"])
        else:
            create_or_update_user(user_id, auth_id, ["userGroup"])


create_user_groups()
create_permissions()
provision_users()
