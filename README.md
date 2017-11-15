Insta Member Api
----------------------------

This project indicates the team member management HTTP API built in Django Framework and MySQL databases

Backend
---------------------------


 Dependencies
 --------------------------
* Python 3.x
* Django
* MySQL

Data Model
--------------------------

A member in the database has this model:
* id (unique)
* First name
* Last name
* Email
* Phone
* Role ('general user' or 'admin user' ONLY)

Listing all members in database
--------------------------------

Listing a member can be done with the following request:

    GET http://127.0.0.1:8000/MemberManagement
    
Will return `200: OK` and a json response (example):

    [
    {
      "id": 1,
      "first_name": "Debashis",
      "last_name": "Satapathy",
      "email_address": "satapathydebashis@live.com",
      "phone_number": "7353693260",
      "role": "admin"
    },
    {
      "id": 2,
      "first_name": "Lalit",
      "last_name": "Patel",
      "email_address": "lalitpatel@gmail.com",
      "phone_number": "7353693261",
      "role": "regular"
    },
    ...
    
Listing a single member by id
------------------------------

A single member from the db can be retreived with:

    GET http://127.0.0.1:8000/MemberManagement/2/

Response `200: OK` and will return a single object:

    {
    "id": 2,
    "first_name": "Lalit",
    "last_name": "Patel",
    "email_address": "lalitpatel@gmail.com",
    "phone_number": "7353693261",
    "role": "regular"
    }
    
or `404` and empty if no content exists for that id:
    
Adding a team member
-------------------------------

Adding a team member using below post method:

    POST http://127.0.0.1:8000/MemberManagement/
    
and adding json to the body of the request:

    {"first_name":"Naresh","last_name":"Rudani","email_address":"nareshrudani@gmail.com","phone_number":"7353693263","role":"general"}
    
http reponse `201: Created` with the created object will be returned.
    
Editing a team member
------------------------------

Changing a team members data can be done with the following request:
    
    PATCH http://127.0.0.1:8000/MemberManagement/2/
    
Adding a json object to the body:
   
    {"role": "admin"}

Http reponse `200: OK` and json object:
 
    {
    "id": 2,
    "first_name": "Lalit",
    "last_name": "Patel",
    "email_address": "lalitpatel@gmail.com",
    "phone_number": "7353693261",
    "role": "admin"
    }

Deleting an object
--------------------------------

Deleting by member id:
  
    DELETE http://127.0.0.1:8000/MemberManagement/3/
 
Reponse `202: Accepted`





