# Python Firefly Services SDK

This is a very simple wrapper to Adobe's [Firefly Services](https://developer.adobe.com/firefly-services/docs/guides/) APIs. My current focus is on Firefly APIs, but I hope to add Photoshop and Lightroom soon. 

You will need Firefly credentials to use this library. 

## Usage

Given you've got your credentials in the environment, you begin by creating an instance of the class:

```
ff_client_id = os.environ.get('CLIENT_ID')
ff_client_secret = os.environ.get('CLIENT_SECRET')

ff = FireflyServices(ff_client_id, ff_client_secret)
```

You can then call methods. Currently, only [Text to Image](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/api/image_generation/V3/) is supported.

```
res = ff.textToImage("cat under sunset", numVariations=2)
```

The result is the same as calling the API directly via a REST call. To help, a utility method, `download`, is available in the SDK:

```
for output in res["outputs"]:
	filename = f"output/{output['seed']}.jpg"
	ff.download(output["image"]["url"], filename)
	print(f"Saved {filename}")
```

## To Do

Currently, the internal call to get an access token will cache the result, but not check the expiration. I need to add that.

## Changelog

10/17/2024: Initial release. 