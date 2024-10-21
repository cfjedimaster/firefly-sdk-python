import requests 

class FireflyServices:
	
	def __init__(self, clientId, clientSecret):
		self.clientId = clientId
		self.clientSecret = clientSecret
		self.accessToken = ''

	def __getAccessToken(self):
		if self.accessToken != '':
			#print('in cache')
			return self.accessToken

		response = requests.post(f"https://ims-na1.adobelogin.com/ims/token/v3?client_id={self.clientId}&client_secret={self.clientSecret}&grant_type=client_credentials&scope=openid,AdobeID,session,additional_info,read_organizations,firefly_api,ff_apis")
		self.accessToken = response.json()['access_token']
		return self.accessToken

	def expandImage(self, img,  **kwargs):

		token = self.__getAccessToken()

		data = {
			"image": {
				"source": self.__sniffResouceType(img)	
			}
		}

		data.update(kwargs)

		response = requests.post("https://firefly-api.adobe.io/v3/images/expand", json=data, headers = {
			"X-API-Key":self.clientId, 
			"Authorization":f"Bearer {token}",
			"Content-Type":"application/json"
		}) 

		return response.json()

	def fillImage(self, source, mask, **kwargs):
		
		token = self.__getAccessToken()

		data = {
			"image": {
				"source": self.__sniffResouceType(source), 
				"mask": self.__sniffResouceType(mask)
			}
		}

		data.update(kwargs)

		response = requests.post("https://firefly-api.adobe.io/v3/images/fill", json=data, headers = {
			"X-API-Key":self.clientId, 
			"Authorization":f"Bearer {token}",
			"Content-Type":"application/json"
		}) 

		return response.json()
	
	def generateObjectComposite(self, prompt, img, **kwargs):
		
		token = self.__getAccessToken()

		data = {
			"image": {
				"source": self.__sniffResouceType(img)
			},
			"prompt":prompt
		}

		data.update(kwargs)

		response = requests.post("https://firefly-api.adobe.io/v3/images/generate-object-composite", json=data, headers = {
			"X-API-Key":self.clientId, 
			"Authorization":f"Bearer {token}",
			"Content-Type":"application/json"
		}) 

		return response.json()

	def generateSimilar(self, img, **kwargs):
		
		token = self.__getAccessToken()

		data = {
			"image": {
				"source": self.__sniffResouceType(img)	
			}
		}

		data.update(kwargs)

		response = requests.post("https://firefly-api.adobe.io/v3/images/generate-similar", json=data, headers = {
			"X-API-Key":self.clientId, 
			"Authorization":f"Bearer {token}",
			"Content-Type":"application/json"
		}) 

		return response.json()

	def textToImage(self, prompt, **kwargs):
		token = self.__getAccessToken()

		data = {
			"prompt":prompt
		}

		data.update(kwargs)
		
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

	def upload(self, path):
		token = self.__getAccessToken()

		with open(path,'rb') as file:

			response = requests.post("https://firefly-api.adobe.io/v2/storage/image", data=file, headers = {
				"X-API-Key":self.clientId, 
				"Authorization":f"Bearer {token}",
				"Content-Type": "image/jpeg"
			}) 

			# Simplify the return a bit... 
			return response.json()["images"][0]["id"]

	# In order to simplify usage, I want to allow you to pass an ID or url to the methods.
	# This will determine what you passed, and either return { url: input } or { uploadId: input }	
	def __sniffResouceType(self, x):
		if x.startswith("http"):
			return { "url": x }
		else:
			return { "uploadId": x }
		
		
