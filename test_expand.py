from firefly import FireflyServices
import os

ff_client_id = os.environ.get('CLIENT_ID')
ff_client_secret = os.environ.get('CLIENT_SECRET')

ff = FireflyServices(ff_client_id, ff_client_secret)

print("Uploading source image")
img = ff.upload("./source_cat.jpg")
print("Source uploaded")

print("Generating expanded image")
res = ff.expandImage(img, size={"width":3500, "height":3000})

for output in res["outputs"]:
	filename = f"output/expanded_{output['seed']}.jpg"
	ff.download(output["image"]["url"], filename)
	print(f"Saved {filename}")

print("Generating expanded image (with prompt)")
res = ff.expandImage(img, prompt="pirate ship in the distance", size={"width":3500, "height":3000})

for output in res["outputs"]:
	filename = f"output/expanded_ff_{output['seed']}.jpg"
	ff.download(output["image"]["url"], filename)
	print(f"Saved {filename}")
