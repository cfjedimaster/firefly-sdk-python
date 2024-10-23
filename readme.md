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

You can then call the methods defined below.

## A Note on Source Images

In order to make things simpler, you can pass the ID returned from the `upload` method (which is automatic) or a URL from supported
cloud storage providers as your input. The SDK will determine what's what and use the appropriate parameters. However, this only
applies in cases where the image is the main argument to the method, like `Generate Similar` and `Expand`. If you want to use an image as a style reference in `Text to Image`, you need to pass it "complete" per the spec, `style.imageReference.source.*`.

Depending on how well this works for real folks in the wild (let me know!), I may adjust accordingly.

### Text To Image:

To use [Text to Image](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/api/image_generation/V3/), pass a prompt and any optionally supported arguments.

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

## Generate Similar

To use [Generate Similar]([https://develo](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/api/generate-similar/)), pass a image source and any optional arguments. The SDK supports an upload method:

```
img = ff.upload("./source_cat.jpg")
```

Which can then be passed to the method:

```
res = ff.generateSimilar(img, numVariations=2)
```

## Generate Object Composite

The [Generate Object Composite](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/api/generate-object-composite/) API requires either an image and a mask, or an image with a transparent background. Here's an example:

```
img = ff.upload("./source_sports_bottle_nobg.png")

placement = {
	"alignment": {
		"vertical": "center",
		"horizontal": "center"
	}	
}
res = ff.generateObjectComposite("a green grassy field on a sunny day", uploadId=img, numVariations=2, placement=placement)
```

## Fill Image

The [Fill Image](https://developer.adobe.com/firefly-services/docs/firefly-api/guides/api/generative_fill/V3/) API requires an image and a mask. Here's an example:

```
img = ff.upload("./source_dog_original.png")
mask = ff.upload("./source_dog_mask.png")

res = ff.fillImage(img, mask)
```

## Remove Background

The [Remove Background](https://developer.adobe.com/firefly-services/docs/photoshop/api/photoshop_removeBackground/) API requires
you to use external storage. In it's simplest form, given imageInput and imageOutput are S3 URLs, you can do this:

```
result = ff.removeBackground(imageInput, imageOutput)
```

The SDK, internally, polls the job result every two seconds and returns the final result. Note that for Azure and Dropbox, you
must pass the first two arguments as dictionary and set `storage` to the right value, for example:

```
imageInput = {
	"href":"the signed url", 
	"storage":"azure"
}
```


## To Do

Currently, the internal call to get an access token will cache the result, but not check the expiration. I need to add that.

## Changelog

10/23/2024: Added Remove Background
10/21/2024: Added Generate Object Composite, Expand image, Fill, and reworked source images.
10/17/2024: Initial release. 
