# REST API written in Python

### This project showcases a very simple REST API that calls another REST API
#### It also focuses on introducing the _pattern matching_ feature using the `match` keyword offered in `Python 3.10`
* If you pass an invalid identifier, you will see an error message returned (even though the status code is a `200`)
  * _GraphQL style!_

## More information
* This uses the *Flask* framework - https://flask.palletsprojects.com/en/2.0.x/quickstart/#
* It calls one API (https://jsonplaceholder.typicode.com/) and returns fake user data.
* Two endpoints - one for getting a collection of users and another for retrieving specific user data.

## Running the API and testing it
* *Prerequisite* - make sure `Flask` is installed
* This is defined in the `requirements.txt` file
* in a terminal, run the following commands:
  * `set FLASK=development`
  * `set FLASK_APP=app.py`


* run the `flask run` command
* Invoke the API using your favorite API testing tool (OR, in the browser!).
    * I prefer _Postman_ 
    * `GET` all users - `http://127.0.0.1:5000/fun/users/`
    * `GET` one user - `http://127.0.0.1:5000/fun/users/<id>`