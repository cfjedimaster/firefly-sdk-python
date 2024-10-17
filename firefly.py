class FireflyServices:
	
	def __init__(self, clientId, clientSecret):
		self.clientId = clientId
		self.clientSecret = clientSecret

	

	def getFFAccessToken(id, secret):
		#response = requests.post(f"https://ims-na1.adobelogin.com/ims/token/v3?client_id={id}&client_secret={secret}&grant_type=client_credentials&scope=openid,AdobeID,session,additional_info,read_organizations,firefly_api,ff_apis")
		#return response.json()['access_token']
