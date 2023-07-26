# GoodData Users Provisioning

The example repository of users provisioning. Users are maintained in Auth0, and provisioned to GoodData. You can find the details in the script [gooddata_oidc_provisioning.py](./gooddata_oidc_provisioning.py).

### Setup Virtual Environment

```bash
# Create virtual env
$ python -m virtualenv venv
# Activate virtual env
$ source venv/bin/activate
# You should see a `(venv)` appear at the beginning of your terminal prompt indicating that you are working inside the `virtualenv`.
# Deactivate virtual env once you are done
$ deactivate
```

### Install Dependencies

```bash
$ pip install -r requirements.txt
```

### Setup Environment Variables

```bash
export AUTH0_DOMAIN=''
export AUTH0_CLIENT_ID=''
export AUTH0_SECRET=''
export GOODDATA_HOST=''
export GOODDATA_TOKEN=''
export GOODDATA_WORKSPACE_ID=''
```