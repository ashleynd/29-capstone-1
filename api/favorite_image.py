from auth import authenticate
from datetime import datetime

album = None # You can also enter an album ID here
image_id = 'YHaaBCi'

def favorite_image(client):
    """
    Favorites an image on imgur.
    """


    print("Favoriting image...")
    image = client.favorite_image(image_id)
    print("Done")
    print()

    return image


# To run this as a standalone script
if __name__ == "__main__":
    # Authenticate 
    client = authenticate()
    image = favorite_image(client)

    print("Image was favorited!")
    print("You can view the favorited image here: {0}".format(image['link']))



