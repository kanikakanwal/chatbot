import requests

url = 'https://api.api.ai/api/query?v=20150910'

def api_request(query):
	req = dict()
	req['query'] = []
	req['query'].append(query) 
	#con = dict()
	#con['name']='weather'
	#con['lifespan']=4
	#req['contexts'] = [con]

	loc=dict()
	loc['latitude']= 37.459157
	loc['longitude']= -122.17926
	req['location'] = [loc]
	req['timezone'] = 'America/New_York'
	req['lang'] = 'en'
	req['sessionId'] = '5dc7a18d-ddb2-40c8-a508-bb0729a897cd'

	token = 'Bearer 1bb44d594b7b49a89554d9d0864a5f51'
	headers = {'Authorization': token, 'Content-Type': 'application/json; charset=utf-8'}
	#response = requests.post(url, data=str(req), auth=('user', 'pass'))

	response = requests.post(url, data=str(req), headers=headers)
	#print response.status_code
	#print response
	#print response.json()
	return response.json()

