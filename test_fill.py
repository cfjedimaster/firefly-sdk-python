from firefly import FireflyServices
import os

ff_client_id = os.environ.get('CLIENT_ID')
ff_client_secret = os.environ.get('CLIENT_SECRET')

ff = FireflyServices(ff_client_id, ff_client_secret)

print("Uploading source image")
img = ff.upload("./source_dog_original.png")
print("Source uploaded")

print("Uploading mask image")
mask = ff.upload("./source_dog_mask.png")
print("Mask uploaded")

print("Generating filled image")
placement = {
	"alignment": {
		"vertical": "center",
		"horizontal": "center"
	}	
}
res = ff.fillImage(img, mask)

for output in res["outputs"]:
	filename = f"output/filled_{output['seed']}.jpg"
	ff.download(output["image"]["url"], filename)
	print(f"Saved {filename}")

res = ff.fillImage(img, mask, prompt="An forest filled with butterflies.")

for output in res["outputs"]:
	filename = f"output/filled_prompt_{output['seed']}.jpg"
	ff.download(output["image"]["url"], filename)
	print(f"Saved {filename}")

