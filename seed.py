"""Seed file to make sample data for picslink db."""

from flask.templating import Environment
from models import db, User, Post
from app import app


db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()

u1 = User(
    first_name="Amy",
    last_name="Hemsworth",
    username="AmazingAmy25",
    # password="awesome1234"
    password="$2b$12$YnzqYD9N3B1VPrsGvsc3Wut1s1kATallKMK9vfN.ZbK90biNv/Mim"
)

u2 = User(
    first_name="Marvin",
    last_name="Garvin",
    username="StarvinMarvin55",
    # password="secret123"
    password="$2b$12$g3j/4X0rdHOUFQ4baWS3wuFA4Jk3RvEl7CsXc622QNGnOSQqX5y36"
)

u3 = User(
    first_name="Rose",
    last_name="Smith",
    username="RosyMaid",
    # password="lovesrose23"
    password="$2b$12$HfEoLHkLzjIw3fW8TguBI.e.yvx1ZTw1hYw/zZFYjdvKUTlMzeOwC"
)

amy = Post(
    title="Butterfly wall",
    photo_url="https://img.ltwebstatic.com/images3_pi/2020/03/19/1584607766e1634741d4fc0f69ad9bcadb6d8d8b35_thumbnail_900x.webp",
    purchase_url="https://us.shein.com/12pcs-Hollow-Butterfly-Wall-Decor-p-1060702-cat-2520.html?url_from=adplashwallart16200319968B_ssc&gclid=CjwKCAjwn6GGBhADEiwAruUcKhl3EIALpw58hJ_ZOjDNACer1mJZOoxOsWcOfWrL7xNmGKI70RwdkxoCX-sQAvD_BwE",
    caption="Rose gold butterflies",
    user_id=3
)

marvin = Post(
    title="Kaloh Pasta Bowl",
    photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202115/0468/img42o.jpg",
    purchase_url="https://www.westelm.com/products/kaloh-pasta-bowls-set-of-4-white-e1902/?sku=8457041&cm_ven=PLA&cm_ite=8457041&cm_cat=Google&cm_pla=Local&gclid=CjwKCAjwn6GGBhADEiwAruUcKl8clEz7900I5K1987oOylkGrs4MiIsQvLGPiIINzABIrKkkeKjSOBoCcToQAvD_BwE",
    caption="Colors are golden oak, Charleston Grey, and white.",
    user_id=2
)

rose = Post(
    title="Tiny cobalt blue sea",
    photo_url="https://i.etsystatic.com/10451613/r/il/e81a7a/1072027519/il_1588xN.1072027519_hcfh.jpg",
    purchase_url="https://www.etsy.com/listing/458754514/9-15mm-04-06-tiny-cobalt-blue-sea-glass?ref=pla_sameshop_listing_top-1&frs=1",
    caption="cobalt seaglass blue small sea glass mosaic glass jewelry glass",
    user_id=1
)


db.session.add_all([u1, u2, u3])

db.session.commit()

db.session.add_all([rose, marvin, amy])

db.session.commit()

# to run:
# python3 seed.py

# only works OUTSIDE of the venv environment