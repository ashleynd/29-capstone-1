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

u4 = User(
    first_name="Violet",
    last_name="Miller",
    username="MyNameIsViolet",
    # password="purple123"
    password="$2b$12$JLNg50pdRXI6PORmkpPWa.ZqdUA1dg0xdsnb5TBJ5exS9JWaHTjQ6"
)

u5 = User(
    first_name="Teddy",
    last_name="Bear",
    username="BestFriend103",
    # password="abcd123"
    password="$2b$12$JLNg50pdRXI6PORmkpPWa.ZqdUA1dg0xdsnb5TBJ5exS9JWaHTjQ6"
)

u6 = User(
    first_name="Sarah",
    last_name="Perkins",
    username="SarahP99",
    # password="peaches45"
    password="$2b$12$g5fsMH1MuHUUIttfGIDJxuuoSgeBXTV2KrbDPx1r1G7sV6WDD90RO"
)

u7 = User(
    first_name="Mark",
    last_name="Wilkins",
    username="MarkyMark300",
    # password="mark600"
    password="$2b$12$g5fsMH1MuHUUIttfGIDJxuuoSgeBXTV2KrbDPx1r1G7sV6WDD90RO"
)

u8 = User(
    first_name="Vanessa",
    last_name="Cooper",
    username="HappyGoLucky23",
    # password="amazing88"
    password="$2b$12$9X3V2cEI.CD045i9RnvyHer5c5E18yvQ/Rg4GZUkLBQ3AzmWhbR2y"
)

amy1 = Post(
    title="Butterfly wall",
    photo_url="https://img.ltwebstatic.com/images3_pi/2020/03/19/1584607766e1634741d4fc0f69ad9bcadb6d8d8b35_thumbnail_900x.webp",
    purchase_url="https://us.shein.com/12pcs-Hollow-Butterfly-Wall-Decor-p-1060702-cat-2520.html?url_from=adplashwallart16200319968B_ssc&gclid=CjwKCAjwn6GGBhADEiwAruUcKhl3EIALpw58hJ_ZOjDNACer1mJZOoxOsWcOfWrL7xNmGKI70RwdkxoCX-sQAvD_BwE",
    caption="Rose gold butterflies",
    user_id=1
)

amy2 = Post(
    title="Bliss garden succulents",
    photo_url="https://cdn.shopify.com/s/files/1/0715/7597/products/20200324-Bliss_720px_1024x1024.jpg?v=1613315139",
    purchase_url="https://www.lulasgarden.com/products/bliss-garden?variant=375915184144&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_campaign=gs-2021-04-12&utm_source=google&utm_medium=smart_campaign&gclid=CjwKCAjwn6GGBhADEiwAruUcKmv3whVesWhvjBbz9zwDulB1lR8SAFRGlhmGm9ePPthkGJnqBFIO3BoCWQYQAvD_BwE",
    caption="Perfect gift. The unique colors of the succulents will make their face light up.",
    user_id=1
)

amy3 = Post(
    title="Beach bag",
    photo_url="https://i.etsystatic.com/8617622/r/il/d8ebd2/2966175412/il_1588xN.2966175412_mhjv.jpg",
    purchase_url="https://www.etsy.com/listing/682631150/personalized-bag-beach-bag-bridesmaid?gpla=1&gao=1&",
    caption="Personalized beach bag available.",
    user_id=1
)

amy4 = Post(
    title="Straw tote bag",
    photo_url="https://cdn.shopify.com/s/files/1/0334/6579/4604/products/2780210876-V1_1230x.jpg?v=1623703526",
    purchase_url="https://verabradley.com/products/straw-tote-bag-27802v36?variant=34830122352684&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9G74Fdxsy-eFDI-1seRPK2OXtw0AnD5WIRQLNPPnUU9q4_YrO_cQKYaAhcwEALw_wcB&gclsrc=aw.ds",
    caption="Carrying sunscreen and beach reads just got so much cuter.",
    user_id=1
)

marvin1 = Post(
    title="Tokyo Chopstick",
    photo_url="https://cdn.shopify.com/s/files/1/0091/0707/9226/products/product-image-524241600.jpg?v=1568823983",
    purchase_url="https://articture.com/products/tokyo-chopstick?currency=USD&utm_medium=cpc&utm_source=google&utm_campaign=Google%20Shopping&gclid=CjwKCAjwn6GGBhADEiwAruUcKkHGyvCqRLnfAUQEOffQpco3m4B5WfyMmoPlTU0ns2PAHL2UifVlHxoCNtMQAvD_BwE&variant=13421469827130",
    caption="A totally different kind of feel for chopstick use.",
    user_id=2
)

marvin2 = Post(
    title="Lavendar Latte",
    photo_url="https://cdn.shopify.com/s/files/1/0004/7769/1968/products/CCC-Lavender-Contents-OnGray.png?v=1611620893",
    purchase_url="https://coppercowcoffee.com/products/lavender-latte-pour-over-vietnamese-coffee-with-organic-lavender-with-milk?variant=15842539339847&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=CjwKCAjwn6GGBhADEiwAruUcKgQK4XeZxA9NpMh_X_4koBuhZLkL9Zce_GRoJegfMmvOC1dVNEoCRxoCbiMQAvD_BwE",
    caption="Take a moment to unwind with Lavender Latte.",
    user_id=2
)

marvin3 = Post(
    title="Pattern Pop Bowl",
    photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202111/0026/hand-painted-pattern-pop-bowls-small-o.jpg",
    purchase_url="https://www.westelm.com/products/hand-painted-pattern-pop-bowls-small-e2402/?catalogId=71&sku=3127244&cm_ven=PLA&cm_cat=Google&cm_pla=Kitchen%20%2B%20Dining%20%3E%20Bowls&region_id=708530&cm_ite=3127244&gclid=CjwKCAjwn6GGBhADEiwAruUcKgjbhjUWz-ABEMXk1Zuc2kRzTW5PKPG5l9Eyk1Mifgu17KXW6BBahRoCCDsQAvD_BwE",
    caption="Hand-painted for perfect ramen.",
    user_id=2
)

marvin4 = Post(
    title="Cereal Bowls",
    photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202112/0088/la-jolla-dinnerware-9-o.jpg",
    purchase_url="https://www.westelm.com/products/la-jolla-dinnerware-e2801/?catalogId=71&sku=9193676&cm_ven=PLA&cm_cat=Google&cm_pla=Kitchen%20%2B%20Dining%20%3E%20Outdoor%20Dinnerware%20%2B%20Drinkware&region_id=708530&cm_ite=9193676&gclid=CjwKCAjwwqaGBhBKEiwAMk-FtMiLXCHck-8mH_dCZZ5zT1BT-svllBSMv0gWWoOo0kyitkk7gi6VORoCSqMQAvD_BwE",
    caption="Admirable dinnerware with other colors.",
    user_id=2
)

rose1 = Post(
    title="Tiny cobalt blue sea",
    photo_url="https://i.etsystatic.com/10451613/r/il/e81a7a/1072027519/il_1588xN.1072027519_hcfh.jpg",
    purchase_url="https://www.etsy.com/listing/458754514/9-15mm-04-06-tiny-cobalt-blue-sea-glass?ref=pla_sameshop_listing_top-1&frs=1",
    caption="cobalt seaglass blue small sea glass mosaic glass jewelry glass",
    user_id=3
)

rose2 = Post(
    title="Rose gold candle holders",
    photo_url="https://cdn.shopify.com/s/files/1/1832/6341/products/CAND_HOLD_006_S_M054__02_1000x.jpg?v=1614015618",
    purchase_url="https://tableclothsfactory.com/products/6-pack-antique-rose-gold-mercury-glass-candle-holders-votive-tealight-holders-with-geometric-design?variant=39006427054265&gclid=CjwKCAjwn6GGBhADEiwAruUcKkgb-KjnyvizzKkZerVp3L7SRpleXDGtOPnlKsDR1e-FRqcb17qljBoC7skQAvD_BwE",
    caption="Votive Tealight Holders With Geometric Design",
    user_id=3
)

rose3 = Post(
    title="Rose Gold fairy lights",
    photo_url="https://cdn.shopify.com/s/files/1/1832/6341/products/CAND_HOLD_006_S_M054__02_1000x.jpg?v=1614015618",
    purchase_url="https://www.macys.com/shop/product/cocus-pocus-rose-gold-fairy-lights?ID=10500413&pla_country=US&CAGPSPN=pla&cm_mmc=Google_SH_PLA_Tabletop-_-GS_Home_Decor_PLA_Restructure_Cocus_Pocus-_-520677615358-_-pg1052191498_c_kclickid_d149d6ed-adae-484f-a4e7-8e1f1fd06df5_KID_EMPTY_13048677288_125737515281_520677615358_pla-1260045957825_850009997012USA__c_KID_&trackingid=509x1052191498&m_sc=sem&m_sb=Google&m_tp=PLA&m_ac=Google_SH_PLA_Tabletop&m_ag=CocusPocus&m_cn=GS_Home_Decor_PLA_Restructure&m_pi=go_cmp-13048677288_adg-125737515281_ad-520677615358_pla-1260045957825_dev-c_ext-_prd-850009997012USA&gclid=CjwKCAjwn6GGBhADEiwAruUcKqt_1csNYA1erhpd4zai-Az__mJn1ToKrcI3Vtco2ARWIAM50PS-_BoCvWIQAvD_BwE",
    caption="Pretty mood lighting for the bedroom",
    user_id=3
)

rose4 = Post(
    title="Rose Gold Printable",
    photo_url="https://i.etsystatic.com/21550101/r/il/49ac93/2475705026/il_1588xN.2475705026_rl07.jpg",
    purchase_url="https://www.etsy.com/listing/856953237/rose-gold-printable-abstract-prints-rose?gpla=1&gao=1&",
    caption="Living Room Decor | Bedroom Prints",
    user_id=3
)

rose5 = Post(
    title="Abstract art frame",
    photo_url="https://i.etsystatic.com/11577301/r/il/815757/1774100642/il_1588xN.1774100642_3bxg.jpg",
    purchase_url="https://www.etsy.com/listing/512610222/rose-gold-printable-brushstroke-abstract?ref=landingpage_similar_listing_top-3",
    caption="Decor for the living room",
    user_id=3
)

rose6 = Post(
    title="Cosmetics organizer",
    photo_url="https://images-na.ssl-images-amazon.com/images/I/61yUAt6V%2BsL._AC_SL1001_.jpg",
    purchase_url="https://www.amazon.com/Cosmetics-Bathroom-Organizer-Assembled-Seasoning/dp/B082Z1KBW2/ref=asc_df_B082Z1KBW2/?tag=hyprod-20&linkCode=df0&hvadid=416801038319&hvpos=&hvnetw=g&hvrand=11715931584947198712&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9051962&hvtargid=pla-897524605629&psc=1&tag=&ref=&adgrpid=94717454540&hvpone=&hvptwo=&hvadid=416801038319&hvpos=&hvnetw=g&hvrand=11715931584947198712&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9051962&hvtargid=pla-897524605629",
    caption="Desktop Cosmetics Storage Rack Rose Gold",
    user_id=3
)

violet1 = Post(
    title="Swirled Movement Glass Vase",
    photo_url="https://images-na.ssl-images-amazon.com/images/I/61yUAt6V%2BsL._AC_SL1001_.jpg",
    purchase_url="https://www.anthropologie.com/shop/swirled-movement-glass-vase?color=053&size=Small&inventoryCountry=US&countryCode=US&type=STANDARD&quantity=1",
    caption="Color in lavender, and made of glass.",
    user_id=4
)

violet2 = Post(
    title="Purple sunset canvas",
    photo_url="https://cdn.shopify.com/s/files/1/1568/8443/products/living_room_331_0b029dd8-4e14-4c94-a22e-fad9b69a3e0b_1200x1200.jpg?v=1618900839",
    purchase_url="https://www.elephantstock.com/products/sand-harbor-purple-sunset-multi-panel-canvas-wall-art?variant=39320519442515",
    caption="Very pretty and ready to hang.",
    user_id=4
)

violet3 = Post(
    title="Purple and gold plate",
    photo_url="https://cdn.shopify.com/s/files/1/1552/7691/products/CHRG_PLST0004_PURP__01_760x760.jpg?v=1586372063",
    purchase_url="https://www.efavormart.com/products/set-of-6-13-round-purple-gold-plastic-charger-plates-with-gold-brushed-waved-scalloped-rim?variant=31912073035822&gclid=CjwKCAjwwqaGBhBKEiwAMk-FtIUTTzOMixVqEIHfMFJSXgUvUM62MOgXcd3GRbOHkASmBOqums7lehoC5fwQAvD_BwE",
    caption="With scalloped rim.",
    user_id=4
)

violet4 = Post(
    title="Lavendar blackout curtains",
    photo_url="https://cdn.shopify.com/s/files/1/1552/7691/products/CUR_PANEMBS01_52108_LAV_D22_760x760.jpg?v=1586394976",
    purchase_url="https://www.efavormart.com/products/pack-of-2-52x108-lavender-embossed-thermal-blackout-curtains-with-chrome-grommet-window-treatment-panels?variant=1772067029010&gclid=CjwKCAjwwqaGBhBKEiwAMk-FtEEdjQH-kqXJMOtkAA5GtjSYMmU42VyduqIr0BeU3GTv_gJWRV1IDBoCueAQAvD_BwE",
    caption="Curtain panels.",
    user_id=4
)

violet5 = Post(
    title="French lavender calendar",
    photo_url="https://assets.wsimgs.com/wsimgs/ab/images/dp/wcm/202113/0423/img37o.jpg",
    purchase_url="https://www.williams-sonoma.com/products/french-lavender-essential-oils-collection-boxed-candle/?catalogId=79&sku=2462208&cm_ven=PLA&cm_cat=Google&cm_pla=Homekeeping%20%3E%20Candles%2C%20Diffusers%20%26%20Room%20Sprays&region_id=708530&cm_ite=2462208&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9EdJPV-6HEYqVPyqDcWk3AkMHgvSxQmZiTJVqneFECt51aqgFvxDbEaAsk4EALw_wcB",
    caption="Williams Sonoma candle",
    user_id=4
)

teddy1 = Post(
    title="Cuddly friends",
    photo_url="https://i5.walmartimages.com/asr/b11bafda-ea1a-4c55-ad9c-92f798b25bd8.6bf26330f7e545e15fa5e9db87566de8.jpeg?odnWidth=1000&odnHeight=1000&odnBg=ffffff",
    purchase_url="https://www.walmart.com/ip/Aurora-Cuddly-Friends-8-Bear/631671562?wmlspartner=wlpa&selectedSellerId=101004606",
    caption="8 inch teddy bear.",
    user_id=5
)

teddy2 = Post(
    title="Forest Plush Bear",
    photo_url="https://cdn.shopify.com/s/files/1/0416/0149/products/woodland-forest_plush_a_1024x1024.jpg?v=1595589729",
    purchase_url="https://lambsivy.com/products/woodland-forest-plush-bear-oscar",
    caption="Meet Oscar. He is a friendly charcoal gray furry bear.",
    user_id=5
)

teddy3 = Post(
    title="Giant Soft Plush Teddy Bear",
    photo_url="https://target.scene7.com/is/image/Target/GUEST_27556c59-356f-44c0-9142-0bf4465e116c?fmt=webp&wid=1400&qlt=80",
    purchase_url="https://www.target.com/p/best-choice-products-38in-giant-soft-plush-teddy-bear-stuffed-animal-toy-w-bow-tie-footprints-brown/-/A-82323459?ref=tgt_adv_XS000000&AFID=google_pla_df_free_online&CPNG=Toys&adgroup=86-2",
    caption="Cute while wearing a red bowtie.",
    user_id=5
)

sarah1 = Post(
    title="Beach towel",
    photo_url="https://s7.landsend.com/is/image/LandsEnd/501758_A518_LF_95A?$1960x2940$",
    purchase_url="https://www.landsend.com/products/rugby-stripe-beach-towel/id_325863?attributes=5575&source=GS&currency=USD&geo=US&skumv=5024281&promotion-code=KITE&promotion-pin=0&cm_mmc=139971612&SC=pla_brand&CMPGN=11304131253&ADGRP=113761308191&KYW=&MT=&DV=c&PID=5024281&TRGT=pla-1114290338360&CH=Google%20AdWords&_cclid=Google_Cj0KCQjw5auGBhDEARIsAFyNm9Eab2jfVji4Biy6REzfc2qWdPjWOcfxRCJDGMpKSozO4rxn1YCcMAMaAr9tEALw_wcB&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9Eab2jfVji4Biy6REzfc2qWdPjWOcfxRCJDGMpKSozO4rxn1YCcMAMaAr9tEALw_wcB",
    caption="Perfect for the beach days",
    user_id=6
)

sarah2 = Post(
    title="Palm Leaf Beach towel",
    photo_url="https://assets.ptimgs.com/ptimgs/rk/images/dp/wcm/202115/0273/img59o.jpg",
    purchase_url="https://www.pbteen.com/products/the-emily-and-meritt-palm-leaf-beach-towel/?catalogId=21&sku=5438309&cm_ven=PLA&cm_cat=Google&cm_pla=Bath%20%26%20Beach%20%3E%20Beach%20Towels%20%26%20Accessories&region_id=708530&cm_ite=5438309_11182394393&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9GJHiTB56-beW7QcGQP-CPcvJ8XP8vxdRLjOXhPnakmHuHAFiCTSwMaAmAJEALw_wcB",
    caption="Palm leaves and on pink background.",
    user_id=6
)

mark1 = Post(
    title="Whole bean coffee",
    photo_url="https://images.food52.com/MD9mtYvym_STLz9E_Wxdfsr3e5c=/2000x0/e48c4bb0-7fca-4aeb-a180-aaf1113034d9--2019-0225_coffee-manufactory_whole-bean-single-coffee-blends_12-oz-2-pack_espresso-01_silo_ty-mecham_001.jpg",
    purchase_url="https://food52.com/shop/products/5770-coffee-manufactory-whole-bean-coffee-blends-2-pack?sku=17068",
    caption="From Coffee Manufactory, the very best one out there.",
    user_id=7
)

mark2 = Post(
    title="Medium Roast",
    photo_url="https://cdn.shopify.com/s/files/1/1475/5488/products/MediumRoast-Front_1024x1024@2x.jpg?v=1559143447",
    purchase_url="https://www.bonescoffee.com/products/bones-coffee-company-medium-roast-coffee?variant=25983152705&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic",
    caption="Provides a rich and smooth taste.",
    user_id=7
)

mark3 = Post(
    title="Coffee from Jamaica",
    photo_url="https://cdn.shopify.com/s/files/1/1475/5488/products/MediumRoast-Front_1024x1024@2x.jpg?v=1559143447",
    purchase_url="https://www.coffeeam.com/products/jamaica-blue-mountain-blend-coffee?variant=31128683315302&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9Ga56WlN_1XGdud-45lCfZGLBwtep4GG5dwveHC-zvudmxnaMyVA6YaAtZiEALw_wcB",
    caption="Jamaica Blue Mountain Blend Coffee",
    user_id=7
)

vanessa1 = Post(
    title="Hello Sunflower",
    photo_url="https://secure.img1-fg.wfcdn.com/im/84593557/resize-h800%5Ecompr-r85/3854/38549984/Hello+Sunflower+by+Catherine+Fitzgerald+-+Wrapped+Canvas+Print.jpg",
    purchase_url="https://www.wayfair.com/Artist-Lane--Hello-Sunflower-by-Catherine-Fitzgerald-Wrapped-Canvas-Print-75CF-P26-L1318-K~RTLA2659.html?refid=GX431921220665-RTLA2659&device=c&ptid=898501776691&network=g&targetid=pla-898501776691&channel=GooglePLA&ireid=38549984&fdid=1817&PiID%5B%5D=21018434&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9GIE-XroajRJt1eR2P9UOOzMdgmmIyAHhL1u6knRMgYW5esPCcf5ZsaAvDfEALw_wcB",
    caption="Artwork by Catherine Fitzgerald",
    user_id=8
)

vanessa2 = Post(
    title="Box of Sunshine",
    photo_url="https://www.openblooms.com/wp-content/uploads/2018/09/OB18-SS06.jpg",
    purchase_url="https://www.openblooms.com/product/box-of-sunshine/?gclid=Cj0KCQjw5auGBhDEARIsAFyNm9GuIA9TxRN33EUJYLudx1JL87jKqJ0ED84TVl1Wmay8fC67_Pa1ch4aAniNEALw_wcB",
    caption="Like lightning in a bottle, but sunshine in a box!",
    user_id=8
)

vanessa3 = Post(
    title="Perfect Sunflowers",
    photo_url="https://cdn2.1800flowers.com/wcsstore/Flowers/images/catalog/161952stjv3x.jpg?width=545&height=597&quality=80&auto=webp&optimize={medium}",
    purchase_url="https://www.1800flowers.com/southern-living-sunflowers-161952?adid=161952STJV3&adtype=pla",
    caption="Arrangement from Southern Living",
    user_id=8
)

vanessa4 = Post(
    title="Obsessed with orchids",
    photo_url="https://www.plants.com/images/1567116573346_20190829-1567116576103.webp",
    purchase_url="https://www.plants.com/p/small-phalenopsis-orchid-pink-157694-2?pla=9386",
    caption="Small Phalaenopsis orchid in pink.",
    user_id=8
)


db.session.add_all([u1, u2, u3, u4, u5, u6, u7, u8])

db.session.commit()

db.session.add_all([amy2, teddy1, vanessa1, mark1, 
sarah2, rose5, amy3, marvin4, 
rose3, marvin2, violet2, vanessa2, 
mark2, marvin3, rose1, violet4, 
amy4, rose2, vanessa3, rose4, 
rose6, violet1, vanessa4, violet5, 
marvin1, teddy2, mark3, violet3, 
teddy3, amy1, sarah1])

db.session.commit()

# to run:
# python3 seed.py

# only works OUTSIDE of the venv environment