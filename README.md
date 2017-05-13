[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)app
====================

A small Django/Angular application that provides management
([CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)) of user bank accounts([IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)) for administartors logged in with the [google account](https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com.ua%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin).

## Getting Started

### Requirements

- [Ansible](http://docs.ansible.com/intro_installation.html) >= 2.3.0.0
- [Vagrant](http://www.vagrantup.com/downloads.html) >= 1.9.4
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) >= 5.1.22


```
$ vagrant up --provider=virtualbox
```

Wait a few minutes for the magic to happen.

### Required settings

- [google oauth2 credentials](https://developers.google.com/identity/protocols/OAuth2)

backend: `src/backend/backend/local_settings.py`
```
...
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "<KEY>"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "<SECRET>"
```
frontend: `src/frontend/local_constants.json`
```
{
  ...
  "GOOGLE_API_CLIENT_ID": "<KEY>"
}
```

### Run development servers

```sh
# ssh to the vagrant box
$ vagrant ssh
# inside the vagrant box
$ cd backend/
$ ./manage.py runserver 0.0.0.0:8000 
$ cd frontend/ 
$ grunt serve
```

You're able to get access to the app by going to this URLs:

frontend: http://localhost:9000/

backend (admin): http://localhost:8000/admin/
