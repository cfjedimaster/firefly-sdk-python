from firefly import FireflyServices
import os

ff_client_id = os.environ.get('CLIENT_ID')
ff_client_secret = os.environ.get('CLIENT_SECRET')

ff = FireflyServices(ff_client_id, ff_client_secret)

print("Generating 2 images for a prompt...")
res = ff.textToImage("cat under sunset", numVariations=2)
for output in res["outputs"]:
	filename = f"output/{output['seed']}.jpg"
	ff.download(output["image"]["url"], filename)
	print(f"Saved {filename}")

print("Generating one image")
res = ff.textToImage("cat under the moon", size={"width":2688,"height":1536})
for output in res["outputs"]:
	filename = f"output/widescreen-{output['seed']}.jpg"
	ff.download(output["image"]["url"], filename)
	print(f"Saved {filename}")

