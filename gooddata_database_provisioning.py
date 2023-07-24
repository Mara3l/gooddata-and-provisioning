from gooddata_sdk import GoodDataSdk, CatalogUserGroup
import pandas as pd

host = "https://odd-bobcat.trial.cloud.gooddata.com"
token = "N2Q4NWQyYmUtMzUzOS00ZWM5LWEwZjAtOTc3ZTVhODY2MjUwOmdvb2RkYXRhX3B5dGhvbl9zZGs6eC9oVlcrVlNKRmVBVjZMMmZHeUxPSFZyQklxOGRlNHQ="
sdk = GoodDataSdk.create(host, token)

def load_users():
    return pd.read_csv("users.csv")

def create_user_groups():
    # adminGroup already exists, it means that only userGroup needs to be created
    user_group = CatalogUserGroup.init(user_group_id="userGroup")
    sdk.catalog_user.create_or_update_user_group(user_group=user_group)

def create_permissions():
    print(sdk.catalog_permission.get_declarative_permissions())

create_permissions()
