import requests 

class FireflyServices:
	
	def __init__(self, clientId, clientSecret):
		self.clientId = clientId
		self.clientSecret = clientSecret
		self.accessToken = ''

	def __getAccessToken(self):
		if self.accessToken != '':
			print('in cache')
			return self.accessToken

		response = requests.post(f"https://ims-na1.adobelogin.com/ims/token/v3?client_id={self.clientId}&client_secret={self.clientSecret}&grant_type=client_credentials&scope=openid,AdobeID,session,additional_info,read_organizations,firefly_api,ff_apis")
		self.accessToken = response.json()['access_token']
		return self.accessToken

	def textToImage(self, prompt, **kwargs):
		token = self.__getAccessToken()

		data = {
			"prompt":prompt
		}

		data.update(kwargs)
		#print(data)
		
		response = requests.post("https://firefly-api.adobe.io/v3/images/generate", json=data, headers = {
			"X-API-Key":self.clientId, 
			"Authorization":f"Bearer {token}",
			"Content-Type":"application/json"
		}) 

		return response.json()

	def download(self, url, path):
		with open(path,'wb') as output:
			bits = requests.get(url, stream=True).content
			output.write(bits)
