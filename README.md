#Dependencies to be installed

apt-get install mysql-server mysql-client

apt-get install python-dev libmysqlclient-dev

pip install MySQL-python

pip install Django

#To set up schema

python manage.py makemigrations

python manage.py migrate

Application is Team

Project is assignmentdjango

#Below are the curl requests to test the API's

List all team members - Request:

curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/team/teammembers/

Add a team member - Request:

curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/team/member/ -d '{"member": {"phone_no": "1234567890", "email": "abcd@gmail.com", "first_name": "Test", "last_name": "Last", "role": "regular"}}'

Modify a team member - Request:

http://127.0.0.1:8000/team/member/<memberid>

Replace memberid with id of the team member to be modified

curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/team/member/5EUJ2J/ -d '{"member": {"phone_no": "1234567890", "email": "test@gmail.com", "first_name": "Allen", "last_name": "Dar", "role": "regular"}}'

Delete a team member - Request:

http://127.0.0.1:8000/team/member/<memberid>

Replace memberid with id of the team member to be modified

curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/team/member/3F4KEM/ -d '{"member": {}}'