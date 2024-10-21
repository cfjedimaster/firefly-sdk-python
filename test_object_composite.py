from firefly import FireflyServices
import os

ff_client_id = os.environ.get('CLIENT_ID')
ff_client_secret = os.environ.get('CLIENT_SECRET')

ff = FireflyServices(ff_client_id, ff_client_secret)

print("Uploading source image")
img = ff.upload("./source_sports_bottle_nobg.png")
print("Source uploaded")

print("Generating object composite")
placement = {
	"alignment": {
		"vertical": "center",
		"horizontal": "center"
	}	
}
res = ff.generateObjectComposite("a green grassy field on a sunny day", img, numVariations=2, placement=placement)

for output in res["outputs"]:
	filename = f"output/object_composite_{output['seed']}.jpg"
	ff.download(output["image"]["url"], filename)
	print(f"Saved {filename}")

