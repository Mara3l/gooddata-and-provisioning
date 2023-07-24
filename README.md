# gooddata-and-provisioning

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

### Change log

- Created users in auth0 (with roles)
- Installed auth0-python (added to requirements)
- Simple auth0 code to get users
- Decided that I create one simple way (just csv with users) and more advanced with OIDC (it is not for trial)

### Database gooddata-and-provisioning

- Load users from CSV or Database.
- Create groups in GD according to customers groups - it can be just admins and users
- Create permissions for these groups
- Create users in GD based on users from CSV or Database
