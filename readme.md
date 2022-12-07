# DJANGO_FERTISOFT_BACKEND

Prerequisites:
1) Install python version 3.10.0 or above.

2) Run server using
   python manage.py runserver

Django admin page:
http://127.0.0.1:8000/admin/

### SUPERUSER Credentials:-
#### Username:- SUPERUSER
#### Password:- SUPERUSER

GET request to retrieve all plans data
http://127.0.0.1:8000/plans/  
  
POST request to generate recharge information
http://127.0.0.1:8000/recharge/

## For creating data for recharged plans
### Request
`{
    "recharged_pack_id": "1"
}`

### Response
`{
  "id": 3,
  "recharged_pack_id": 1
}`
