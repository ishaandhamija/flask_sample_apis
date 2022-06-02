# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,jsonify,request
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/user/data', methods = ['GET'])
def get_user_data():
	if (request.method == 'GET'):
		user_data = {
			"id" : 9178,
			"name" : "Rishabh Sharma",
			"college": "IIT Delhi",
			"pictureUrl": "https://picsum.photos/200"
		}
		response = {
			"statusCode": 0,
			"statusMessage": "user data fetched successfully",
			"data": user_data
		}

		response = jsonify(response)
		response.headers.add('Access-Control-Allow-Origin', '*')

		return response

@app.route('/job/openings', methods = ['GET'])
def get_jobs_data():
	if (request.method == 'GET'):
		jobs_list = [
			{
				"id": 5231,
				"designation": "Frontend Developer",
				"company": "Flipkart",
				"location": "Bengaluru",
				"min_experience": 1,
				"skills": ["HTML", "CSS", "Bootstrap", "jQuery", "Javascript", "React JS"]
			},
			{
				"id": 5344,
				"designation": "Android Developer",
				"company": "Microsoft",
				"location": "Noida",
				"min_experience": 2,
				"skills": ["Java", "Kotlin", "XML", "Android Studio"]
			},
			{
				"id": 6012,
				"designation": "Software Developer",
				"company": "Amazon",
				"location": "Gurugram",
				"min_experience": 0,
				"skills": ["Java", "Sprint Boot", "SQL", "Kafka"]
			},
			{
				"id": 6638,
				"designation": "Senior Software Engineer",
				"company": "Swiggy",
				"location": "Bengaluru",
				"min_experience": 5,
				"skills": ["Go", "Java", "Node JS"]
			},
			{
				"id": 4256,
				"designation": "iOS Developer",
				"company": "Urban Company",
				"location": "Gurugram",
				"min_experience": 0,
				"skills": ["C++", "Swift", "XCode"]
			},
			{
				"id": 5634,
				"designation": "Software Engineer",
				"company": "Adobe",
				"location": "Noida",
				"min_experience": 2,
				"skills": ["Java", "Sprint Boot", "SQL", "Kafka"]
			}
		]
		response = {
			"statusCode": 0,
			"statusMessage": "jobs data fetched successfully",
			"data": jobs_list
		}

		response = jsonify(response)
		response.headers.add('Access-Control-Allow-Origin', '*')

		return response

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
