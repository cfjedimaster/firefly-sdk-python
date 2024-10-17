from firefly import FireflyServices

ff_client_id = os.environ.get('CLIENT_ID')
ff_client_secret = os.environ.get('CLIENT_SECRET')


ff = FireflyServices(ff_client_id, ff_client_secret)
