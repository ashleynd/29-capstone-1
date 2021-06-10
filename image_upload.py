from auth import authenticate
from datetime import datetime

album = None # You can also enter an album ID here
image_path = 'static/images/daisy.jpg'

def upload_image(client):
    """
    Uploads an image to imgur.
    """

	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
    config = {
        'album': album,
        'name': 'A lonely pink daisy',
        'title': 'A pink daisy',
        'description': 'When this flower sprouted: {0}'.format(datetime.now())
    }

    print("Uploading image...")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image


# To run this as a standalone script
if __name__ == "__main__":
    # Authenticate 
    client = authenticate()
    image = upload_image(client)

    print("Image was posted!")
    print("You can find the image here: {0}".format(image['link']))