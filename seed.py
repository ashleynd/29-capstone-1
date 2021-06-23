"""Seed file to make sample data for picslink db."""
# # to run:
# # python3 seed.py

# from flask.templating import Environment
# from models import db, User, Post
from models import db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# User.query.delete()
# Post.query.delete()

# u1 = User(
#     first_name="Amy",
#     last_name="Hemsworth",
#     username="AmazingAmy25",
#     # password="awesome1234"
#     password="$2b$12$YnzqYD9N3B1VPrsGvsc3Wut1s1kATallKMK9vfN.ZbK90biNv/Mim"
# )

# u2 = User(
#     first_name="Marvin",
#     last_name="Garvin",
#     username="StarvinMarvin55",
#     # password="secret123"
#     password="$2b$12$g3j/4X0rdHOUFQ4baWS3wuFA4Jk3RvEl7CsXc622QNGnOSQqX5y36"
# )

# u3 = User(
#     first_name="Rose",
#     last_name="Smith",
#     username="RosyMaid",
#     # password="lovesrose23"
#     password="$2b$12$HfEoLHkLzjIw3fW8TguBI.e.yvx1ZTw1hYw/zZFYjdvKUTlMzeOwC"
# )

# u4 = User(
#     first_name="Violet",
#     last_name="Miller",
#     username="MyNameIsViolet",
#     # password="purple123"
#     password="$2b$12$JLNg50pdRXI6PORmkpPWa.ZqdUA1dg0xdsnb5TBJ5exS9JWaHTjQ6"
# )

# u5 = User(
#     first_name="Teddy",
#     last_name="Bear",
#     username="BestFriend103",
#     # password="abcd123"
#     password="$2b$12$JLNg50pdRXI6PORmkpPWa.ZqdUA1dg0xdsnb5TBJ5exS9JWaHTjQ6"
# )

# u6 = User(
#     first_name="Sarah",
#     last_name="Perkins",
#     username="SarahP99",
#     # password="peaches45"
#     password="$2b$12$g5fsMH1MuHUUIttfGIDJxuuoSgeBXTV2KrbDPx1r1G7sV6WDD90RO"
# )

# u7 = User(
#     first_name="Mark",
#     last_name="Wilkins",
#     username="MarkyMark300",
#     # password="mark600"
#     password="$2b$12$g5fsMH1MuHUUIttfGIDJxuuoSgeBXTV2KrbDPx1r1G7sV6WDD90RO"
# )

# u8 = User(
#     first_name="Vanessa",
#     last_name="Cooper",
#     username="HappyGoLucky23",
#     # password="amazing88"
#     password="$2b$12$9X3V2cEI.CD045i9RnvyHer5c5E18yvQ/Rg4GZUkLBQ3AzmWhbR2y"
# )

# u9 = User(
#     first_name="Rachel",
#     last_name="Hawkin",
#     username="CouchPotato45",
#     # password="potato4"
#     password="$2b$12$hoPfb9r7O/fGGb8fcMc8aOF9f7Hswv5uS7R4sYwwuXiueYC7urzpu"
# )

# u10 = User(
#     first_name="Gina",
#     last_name="Nelson",
#     username="CrazyCatLady80",
#     # password="cats10"
#     password="$2b$12$gLPFfwcvCjHTsz.iV0wTTu7yXlEw4y7dDQ2b433lhBVSGSvz8zwZm"
# )

# u11 = User(
#     first_name="Bob",
#     last_name="Baker",
#     username="BakerBob300",
#     # password="cookie12"
#     password="$2b$12$BBAKwxYiZLe2AFM/kTWfVOyYpUsntqCzrJkrk37Ix4LFsLLLmLWye"
# )

# u12 = User(
#     first_name="Molly",
#     last_name="Appleseed",
#     username="MollyIsLucky",
#     # password="molly1234"
#     password="$2b$12$ixPbX3mYxDCKwqNnpsELW.rDYicsh5Jnk/fM8Dvc.P8Nz/tMyI0r2"
# )

# u13 = User(
#     first_name="Patty",
#     last_name="Anderson",
#     username="GirlWithAGreenThumb",
#     # password="green1"
#     password="$2b$12$VxYpulRVD7ScUxOhQzEwcOgc9NG9eDZyjvFtcdwYp4zzfhq6/8wdq"
# )

# amy1 = Post(
#     title="Butterfly wall",
#     photo_url="https://img.ltwebstatic.com/images3_pi/2020/03/19/1584607766e1634741d4fc0f69ad9bcadb6d8d8b35_thumbnail_900x.webp",
#     purchase_url="https://us.shein.com/12pcs-Hollow-Butterfly-Wall-Decor-p-1060702-cat-2520.html?url_from=adplashwallart16200319968B_ssc&gclid=CjwKCAjwn6GGBhADEiwAruUcKhl3EIALpw58hJ_ZOjDNACer1mJZOoxOsWcOfWrL7xNmGKI70RwdkxoCX-sQAvD_BwE",
#     caption="Rose gold butterflies",
#     user_id=1
# )

# amy2 = Post(
#     title="Bliss garden succulents",
#     photo_url="https://cdn.shopify.com/s/files/1/0715/7597/products/20200324-Bliss_720px_1024x1024.jpg?v=1613315139",
#     purchase_url="https://www.lulasgarden.com/products/bliss-garden?variant=375915184144&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_campaign=gs-2021-04-12&utm_source=google&utm_medium=smart_campaign&gclid=CjwKCAjwn6GGBhADEiwAruUcKmv3whVesWhvjBbz9zwDulB1lR8SAFRGlhmGm9ePPthkGJnqBFIO3BoCWQYQAvD_BwE",
#     caption="Perfect gift. The unique colors of the succulents will make their face light up.",
#     user_id=1
# )

# amy3 = Post(
#     title="Beach bag",
#     photo_url="https://i.etsystatic.com/8617622/r/il/d8ebd2/2966175412/il_1588xN.2966175412_mhjv.jpg",
#     purchase_url="https://www.etsy.com/listing/682631150/personalized-bag-beach-bag-bridesmaid?gpla=1&gao=1&",
#     caption="Personalized beach bag available.",
#     user_id=1
# )

# amy4 = Post(
#     title="Straw tote bag",
#     photo_url="https://cdn.shopify.com/s/files/1/0334/6579/4604/products/2780210876-V1_1230x.jpg?v=1623703526",
#     purchase_url="https://verabradley.com/products/straw-tote-bag-27802v36?variant=34830122352684&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9G74Fdxsy-eFDI-1seRPK2OXtw0AnD5WIRQLNPPnUU9q4_YrO_cQKYaAhcwEALw_wcB&gclsrc=aw.ds",
#     caption="Carrying sunscreen and beach reads just got so much cuter.",
#     user_id=1
# )

# amy5 = Post(
#     title="Wine Cork Holder",
#     photo_url="https://www.vivaterra.com/medias/sys_master/images/images/hc7/h55/11559876362270/11559876362270.jpg",
#     purchase_url="https://www.vivaterra.com/p/V5297?aff=6443&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9Hv_73UcyLX1e0YiR5TE7XSO7uAAsmVcMiSjGWZOEN28gOH4KC4AS0aAvMOEALw_wcB",
#     caption="toss the cork into the frame for an added textured look.",
#     user_id=1
# )

# marvin1 = Post(
#     title="Tokyo Chopstick",
#     photo_url="https://cdn.shopify.com/s/files/1/0091/0707/9226/products/product-image-524241600.jpg?v=1568823983",
#     purchase_url="https://articture.com/products/tokyo-chopstick?currency=USD&utm_medium=cpc&utm_source=google&utm_campaign=Google%20Shopping&gclid=CjwKCAjwn6GGBhADEiwAruUcKkHGyvCqRLnfAUQEOffQpco3m4B5WfyMmoPlTU0ns2PAHL2UifVlHxoCNtMQAvD_BwE&variant=13421469827130",
#     caption="A totally different kind of feel for chopstick use.",
#     user_id=2
# )

# marvin2 = Post(
#     title="Lavendar Latte",
#     photo_url="https://cdn.shopify.com/s/files/1/0004/7769/1968/products/CCC-Lavender-Contents-OnGray.png?v=1611620893",
#     purchase_url="https://coppercowcoffee.com/products/lavender-latte-pour-over-vietnamese-coffee-with-organic-lavender-with-milk?variant=15842539339847&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=CjwKCAjwn6GGBhADEiwAruUcKgQK4XeZxA9NpMh_X_4koBuhZLkL9Zce_GRoJegfMmvOC1dVNEoCRxoCbiMQAvD_BwE",
#     caption="Take a moment to unwind with Lavender Latte.",
#     user_id=2
# )

# marvin3 = Post(
#     title="Pattern Pop Bowl",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202111/0026/hand-painted-pattern-pop-bowls-small-o.jpg",
#     purchase_url="https://www.westelm.com/products/hand-painted-pattern-pop-bowls-small-e2402/?catalogId=71&sku=3127244&cm_ven=PLA&cm_cat=Google&cm_pla=Kitchen%20%2B%20Dining%20%3E%20Bowls&region_id=708530&cm_ite=3127244&gclid=CjwKCAjwn6GGBhADEiwAruUcKgjbhjUWz-ABEMXk1Zuc2kRzTW5PKPG5l9Eyk1Mifgu17KXW6BBahRoCCDsQAvD_BwE",
#     caption="Hand-painted for perfect ramen.",
#     user_id=2
# )

# marvin4 = Post(
#     title="Cereal Bowls",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202112/0088/la-jolla-dinnerware-9-o.jpg",
#     purchase_url="https://www.westelm.com/products/la-jolla-dinnerware-e2801/?catalogId=71&sku=9193676&cm_ven=PLA&cm_cat=Google&cm_pla=Kitchen%20%2B%20Dining%20%3E%20Outdoor%20Dinnerware%20%2B%20Drinkware&region_id=708530&cm_ite=9193676&gclid=CjwKCAjwwqaGBhBKEiwAMk-FtMiLXCHck-8mH_dCZZ5zT1BT-svllBSMv0gWWoOo0kyitkk7gi6VORoCSqMQAvD_BwE",
#     caption="Admirable dinnerware with other colors.",
#     user_id=2
# )

# rose1 = Post(
#     title="Tiny cobalt blue sea",
#     photo_url="https://i.etsystatic.com/10451613/r/il/e81a7a/1072027519/il_1588xN.1072027519_hcfh.jpg",
#     purchase_url="https://www.etsy.com/listing/458754514/9-15mm-04-06-tiny-cobalt-blue-sea-glass?ref=pla_sameshop_listing_top-1&frs=1",
#     caption="cobalt seaglass blue small sea glass mosaic glass jewelry glass",
#     user_id=3
# )

# rose2 = Post(
#     title="Rose gold candle holders",
#     photo_url="https://cdn.shopify.com/s/files/1/1832/6341/products/CAND_HOLD_006_S_M054__02_1000x.jpg?v=1614015618",
#     purchase_url="https://tableclothsfactory.com/products/6-pack-antique-rose-gold-mercury-glass-candle-holders-votive-tealight-holders-with-geometric-design?variant=39006427054265&gclid=CjwKCAjwn6GGBhADEiwAruUcKkgb-KjnyvizzKkZerVp3L7SRpleXDGtOPnlKsDR1e-FRqcb17qljBoC7skQAvD_BwE",
#     caption="Votive Tealight Holders With Geometric Design",
#     user_id=3
# )

# rose3 = Post(
#     title="Rose Gold fairy lights",
#     photo_url="https://cdn.shopify.com/s/files/1/1832/6341/products/CAND_HOLD_006_S_M054__02_1000x.jpg?v=1614015618",
#     purchase_url="https://www.macys.com/shop/product/cocus-pocus-rose-gold-fairy-lights?ID=10500413&pla_country=US&CAGPSPN=pla&cm_mmc=Google_SH_PLA_Tabletop-_-GS_Home_Decor_PLA_Restructure_Cocus_Pocus-_-520677615358-_-pg1052191498_c_kclickid_d149d6ed-adae-484f-a4e7-8e1f1fd06df5_KID_EMPTY_13048677288_125737515281_520677615358_pla-1260045957825_850009997012USA__c_KID_&trackingid=509x1052191498&m_sc=sem&m_sb=Google&m_tp=PLA&m_ac=Google_SH_PLA_Tabletop&m_ag=CocusPocus&m_cn=GS_Home_Decor_PLA_Restructure&m_pi=go_cmp-13048677288_adg-125737515281_ad-520677615358_pla-1260045957825_dev-c_ext-_prd-850009997012USA&gclid=CjwKCAjwn6GGBhADEiwAruUcKqt_1csNYA1erhpd4zai-Az__mJn1ToKrcI3Vtco2ARWIAM50PS-_BoCvWIQAvD_BwE",
#     caption="Pretty mood lighting for the bedroom",
#     user_id=3
# )

# rose4 = Post(
#     title="Rose Gold Printable",
#     photo_url="https://i.etsystatic.com/21550101/r/il/49ac93/2475705026/il_1588xN.2475705026_rl07.jpg",
#     purchase_url="https://www.etsy.com/listing/856953237/rose-gold-printable-abstract-prints-rose?gpla=1&gao=1&",
#     caption="Living Room Decor | Bedroom Prints",
#     user_id=3
# )

# rose5 = Post(
#     title="Abstract art frame",
#     photo_url="https://i.etsystatic.com/11577301/r/il/815757/1774100642/il_1588xN.1774100642_3bxg.jpg",
#     purchase_url="https://www.etsy.com/listing/512610222/rose-gold-printable-brushstroke-abstract?ref=landingpage_similar_listing_top-3",
#     caption="Decor for the living room",
#     user_id=3
# )

# rose6 = Post(
#     title="Cosmetics organizer",
#     photo_url="https://images-na.ssl-images-amazon.com/images/I/61yUAt6V%2BsL._AC_SL1001_.jpg",
#     purchase_url="https://www.amazon.com/Cosmetics-Bathroom-Organizer-Assembled-Seasoning/dp/B082Z1KBW2/ref=asc_df_B082Z1KBW2/?tag=hyprod-20&linkCode=df0&hvadid=416801038319&hvpos=&hvnetw=g&hvrand=11715931584947198712&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9051962&hvtargid=pla-897524605629&psc=1&tag=&ref=&adgrpid=94717454540&hvpone=&hvptwo=&hvadid=416801038319&hvpos=&hvnetw=g&hvrand=11715931584947198712&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9051962&hvtargid=pla-897524605629",
#     caption="Desktop Cosmetics Storage Rack Rose Gold",
#     user_id=3
# )

# rose7 = Post(
#     title="Light Pink Tree Lamp",
#     photo_url="https://sp.apolloboxassets.com/vendor/product/productImages/2020-09-16/8J1TYArray_11.jpg",
#     purchase_url="https://www.theapollobox.com/product/sku1017200/light-pink-tree-lamp?gclid=Cj0KCQjw5auGBhDEARIsAFyNm9GVhXy5gv4c48Z2M87m13q4GSP3PYoZRL3dcg6cDcmUN12pO_tuqqQaArMJEALw_wcB",
#     caption="Functional Light and Decor",
#     user_id=3
# )

# violet1 = Post(
#     title="Swirled Movement Glass Vase",
#     photo_url="https://s7d5.scene7.com/is/image/Anthropologie/60624079_053_b?$a15-pdp-detail-shot$&fit=constrain&fmt=webp&qlt=80&wid=1080",
#     purchase_url="https://www.anthropologie.com/shop/swirled-movement-glass-vase?color=053&size=Small&inventoryCountry=US&countryCode=US&type=STANDARD&quantity=1",
#     caption="Color in lavender, and made of glass.",
#     user_id=4
# )

# violet2 = Post(
#     title="Purple sunset canvas",
#     photo_url="https://cdn.shopify.com/s/files/1/1568/8443/products/living_room_331_0b029dd8-4e14-4c94-a22e-fad9b69a3e0b_1200x1200.jpg?v=1618900839",
#     purchase_url="https://www.elephantstock.com/products/sand-harbor-purple-sunset-multi-panel-canvas-wall-art?variant=39320519442515",
#     caption="Very pretty and ready to hang.",
#     user_id=4
# )

# violet3 = Post(
#     title="Purple and gold plate",
#     photo_url="https://cdn.shopify.com/s/files/1/1552/7691/products/CHRG_PLST0004_PURP__01_760x760.jpg?v=1586372063",
#     purchase_url="https://www.efavormart.com/products/set-of-6-13-round-purple-gold-plastic-charger-plates-with-gold-brushed-waved-scalloped-rim?variant=31912073035822&gclid=CjwKCAjwwqaGBhBKEiwAMk-FtIUTTzOMixVqEIHfMFJSXgUvUM62MOgXcd3GRbOHkASmBOqums7lehoC5fwQAvD_BwE",
#     caption="With scalloped rim.",
#     user_id=4
# )

# violet4 = Post(
#     title="Lavendar blackout curtains",
#     photo_url="https://cdn.shopify.com/s/files/1/1552/7691/products/CUR_PANEMBS01_52108_LAV_D22_760x760.jpg?v=1586394976",
#     purchase_url="https://www.efavormart.com/products/pack-of-2-52x108-lavender-embossed-thermal-blackout-curtains-with-chrome-grommet-window-treatment-panels?variant=1772067029010&gclid=CjwKCAjwwqaGBhBKEiwAMk-FtEEdjQH-kqXJMOtkAA5GtjSYMmU42VyduqIr0BeU3GTv_gJWRV1IDBoCueAQAvD_BwE",
#     caption="Curtain panels.",
#     user_id=4
# )

# violet5 = Post(
#     title="French lavender calendar",
#     photo_url="https://assets.wsimgs.com/wsimgs/ab/images/dp/wcm/202113/0423/img37o.jpg",
#     purchase_url="https://www.williams-sonoma.com/products/french-lavender-essential-oils-collection-boxed-candle/?catalogId=79&sku=2462208&cm_ven=PLA&cm_cat=Google&cm_pla=Homekeeping%20%3E%20Candles%2C%20Diffusers%20%26%20Room%20Sprays&region_id=708530&cm_ite=2462208&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9EdJPV-6HEYqVPyqDcWk3AkMHgvSxQmZiTJVqneFECt51aqgFvxDbEaAsk4EALw_wcB",
#     caption="Williams Sonoma candle",
#     user_id=4
# )

# violet6 = Post(
#     title="Eucalyptus Sheet set",
#     photo_url="https://cdn.shopify.com/s/files/1/2461/6249/products/Pupsinbed_2000x.jpg?v=1610145981",
#     purchase_url="https://sheetsgiggles.com/products/eucalyptus-lyocell-sheet-sets-purple?variant=31966205902942",
#     caption="In purple, of course!",
#     user_id=4
# )

# violet7 = Post(
#     title="Microfiber Fitted Sheet",
#     photo_url="https://media.kohlsimg.com/is/image/kohls/2471446_Eggplant?wid=1200&hei=1200&op_sharpen=1",
#     purchase_url="https://www.kohls.com/product/prd-2471446/fitted-microfiber-sheet.jsp?skuid=65384421&CID=seo_offers&utm_campaign=SAG&utm_medium=organic&utm_source=google&utm_product=65384421",
#     caption="Brushed finish sheet set.",
#     user_id=4
# )

# violet8 = Post(
#     title="Vera Wang",
#     photo_url="https://i5.walmartimages.com/asr/84b4d40f-d28c-452b-9b5e-711fe33ccbd7.375f40779266b35e83dc4b50f88f784f.jpeg?odnWidth=undefined&odnHeight=undefined&odnBg=ffffff",
#     purchase_url="https://www.walmart.com/ip/Vera-Wang-Princess-Eau-de-Toilette-Spray-for-Women-3-4-Fl-Oz/358507425?wmlspartner=wlpa&selectedSellerId=101052711",
#     caption="For the princess in you.",
#     user_id=4
# )

# teddy1 = Post(
#     title="Cuddly friends",
#     photo_url="https://i5.walmartimages.com/asr/b11bafda-ea1a-4c55-ad9c-92f798b25bd8.6bf26330f7e545e15fa5e9db87566de8.jpeg?odnWidth=1000&odnHeight=1000&odnBg=ffffff",
#     purchase_url="https://www.walmart.com/ip/Aurora-Cuddly-Friends-8-Bear/631671562?wmlspartner=wlpa&selectedSellerId=101004606",
#     caption="8 inch teddy bear.",
#     user_id=5
# )

# teddy2 = Post(
#     title="Forest Plush Bear",
#     photo_url="https://cdn.shopify.com/s/files/1/0416/0149/products/woodland-forest_plush_a_1024x1024.jpg?v=1595589729",
#     purchase_url="https://lambsivy.com/products/woodland-forest-plush-bear-oscar",
#     caption="Meet Oscar. He is a friendly charcoal gray furry bear.",
#     user_id=5
# )

# teddy3 = Post(
#     title="Giant Soft Plush Teddy Bear",
#     photo_url="https://target.scene7.com/is/image/Target/GUEST_27556c59-356f-44c0-9142-0bf4465e116c?fmt=webp&wid=1400&qlt=80",
#     purchase_url="https://www.target.com/p/best-choice-products-38in-giant-soft-plush-teddy-bear-stuffed-animal-toy-w-bow-tie-footprints-brown/-/A-82323459?ref=tgt_adv_XS000000&AFID=google_pla_df_free_online&CPNG=Toys&adgroup=86-2",
#     caption="Cute while wearing a red bowtie.",
#     user_id=5
# )

# sarah1 = Post(
#     title="Beach towel",
#     photo_url="https://s7.landsend.com/is/image/LandsEnd/501758_A518_LF_95A?$1960x2940$",
#     purchase_url="https://www.landsend.com/products/rugby-stripe-beach-towel/id_325863?attributes=5575&source=GS&currency=USD&geo=US&skumv=5024281&promotion-code=KITE&promotion-pin=0&cm_mmc=139971612&SC=pla_brand&CMPGN=11304131253&ADGRP=113761308191&KYW=&MT=&DV=c&PID=5024281&TRGT=pla-1114290338360&CH=Google%20AdWords&_cclid=Google_Cj0KCQjw5auGBhDEARIsAFyNm9Eab2jfVji4Biy6REzfc2qWdPjWOcfxRCJDGMpKSozO4rxn1YCcMAMaAr9tEALw_wcB&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9Eab2jfVji4Biy6REzfc2qWdPjWOcfxRCJDGMpKSozO4rxn1YCcMAMaAr9tEALw_wcB",
#     caption="Perfect for the beach days",
#     user_id=6
# )

# sarah2 = Post(
#     title="Palm Leaf Beach towel",
#     photo_url="https://assets.ptimgs.com/ptimgs/rk/images/dp/wcm/202115/0273/img59o.jpg",
#     purchase_url="https://www.pbteen.com/products/the-emily-and-meritt-palm-leaf-beach-towel/?catalogId=21&sku=5438309&cm_ven=PLA&cm_cat=Google&cm_pla=Bath%20%26%20Beach%20%3E%20Beach%20Towels%20%26%20Accessories&region_id=708530&cm_ite=5438309_11182394393&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9GJHiTB56-beW7QcGQP-CPcvJ8XP8vxdRLjOXhPnakmHuHAFiCTSwMaAmAJEALw_wcB",
#     caption="Palm leaves and on pink background.",
#     user_id=6
# )

# sarah3 = Post(
#     title="Ming Fern",
#     photo_url="https://cdn.shopify.com/s/files/1/1334/4597/products/Pink-Preserved-Ming-Fern_b84e6250-4fc2-4f2f-954d-0b66c8959bd4_979x1370.jpg?v=1619624505",
#     purchase_url="https://www.afloral.com/products/pink-preserved-ming-fern-leaf-bundle-16-22tall?gclid=Cj0KCQjw5auGBhDEARIsAFyNm9FNDtntIeKdM4_T_s1Wwtle9_KV861rII5bVFWt1ff1Ke1ev0_d10waAmMqEALw_wcB",
#     caption="Add a pop of color to your dried flower arrangements.",
#     user_id=6
# )

# sarah4 = Post(
#     title="Sunset Light painting",
#     photo_url="https://www.erinhansonprints.com/Content/InventoryImages/Erin-Hanson-Sunset-Light.jpg",
#     purchase_url="https://www.erinhansonprints.com/p/Sunset_Light?gshop=true",
#     caption="Fine Art Prints by Erin Hanson.",
#     user_id=6
# )

# mark1 = Post(
#     title="Whole bean coffee",
#     photo_url="https://images.food52.com/MD9mtYvym_STLz9E_Wxdfsr3e5c=/2000x0/e48c4bb0-7fca-4aeb-a180-aaf1113034d9--2019-0225_coffee-manufactory_whole-bean-single-coffee-blends_12-oz-2-pack_espresso-01_silo_ty-mecham_001.jpg",
#     purchase_url="https://food52.com/shop/products/5770-coffee-manufactory-whole-bean-coffee-blends-2-pack?sku=17068",
#     caption="From Coffee Manufactory, the very best one out there.",
#     user_id=7
# )

# mark2 = Post(
#     title="Medium Roast",
#     photo_url="https://cdn.shopify.com/s/files/1/1475/5488/products/MediumRoast-Front_1024x1024@2x.jpg?v=1559143447",
#     purchase_url="https://www.bonescoffee.com/products/bones-coffee-company-medium-roast-coffee?variant=25983152705&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic",
#     caption="Provides a rich and smooth taste.",
#     user_id=7
# )

# mark3 = Post(
#     title="Coffee from Jamaica",
#     photo_url="https://cdn.shopify.com/s/files/1/1475/5488/products/MediumRoast-Front_1024x1024@2x.jpg?v=1559143447",
#     purchase_url="https://www.coffeeam.com/products/jamaica-blue-mountain-blend-coffee?variant=31128683315302&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9Ga56WlN_1XGdud-45lCfZGLBwtep4GG5dwveHC-zvudmxnaMyVA6YaAtZiEALw_wcB",
#     caption="Jamaica Blue Mountain Blend Coffee",
#     user_id=7
# )

# vanessa1 = Post(
#     title="Hello Sunflower",
#     photo_url="https://secure.img1-fg.wfcdn.com/im/84593557/resize-h800%5Ecompr-r85/3854/38549984/Hello+Sunflower+by+Catherine+Fitzgerald+-+Wrapped+Canvas+Print.jpg",
#     purchase_url="https://www.wayfair.com/Artist-Lane--Hello-Sunflower-by-Catherine-Fitzgerald-Wrapped-Canvas-Print-75CF-P26-L1318-K~RTLA2659.html?refid=GX431921220665-RTLA2659&device=c&ptid=898501776691&network=g&targetid=pla-898501776691&channel=GooglePLA&ireid=38549984&fdid=1817&PiID%5B%5D=21018434&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9GIE-XroajRJt1eR2P9UOOzMdgmmIyAHhL1u6knRMgYW5esPCcf5ZsaAvDfEALw_wcB",
#     caption="Artwork by Catherine Fitzgerald",
#     user_id=8
# )

# vanessa2 = Post(
#     title="Box of Sunshine",
#     photo_url="https://www.openblooms.com/wp-content/uploads/2018/09/OB18-SS06.jpg",
#     purchase_url="https://www.openblooms.com/product/box-of-sunshine/?gclid=Cj0KCQjw5auGBhDEARIsAFyNm9GuIA9TxRN33EUJYLudx1JL87jKqJ0ED84TVl1Wmay8fC67_Pa1ch4aAniNEALw_wcB",
#     caption="Like lightning in a bottle, but sunshine in a box!",
#     user_id=8
# )

# vanessa3 = Post(
#     title="Perfect Sunflowers",
#     photo_url="https://cdn2.1800flowers.com/wcsstore/Flowers/images/catalog/161952stjv3x.jpg?width=545&height=597&quality=80&auto=webp&optimize={medium}",
#     purchase_url="https://www.1800flowers.com/southern-living-sunflowers-161952?adid=161952STJV3&adtype=pla",
#     caption="Arrangement from Southern Living",
#     user_id=8
# )

# vanessa4 = Post(
#     title="Obsessed with orchids",
#     photo_url="https://www.plants.com/images/1567116573346_20190829-1567116576103.webp",
#     purchase_url="https://www.plants.com/p/small-phalenopsis-orchid-pink-157694-2?pla=9386",
#     caption="Small Phalaenopsis orchid in pink.",
#     user_id=8
# )

# vanessa5 = Post(
#     title="Phalaenopsis Orchid",
#     photo_url="https://cdn2.1800flowers.com/wcsstore/Flowers/images/catalog/101828lwcx.jpg?width=545&height=597&quality=80&auto=webp&optimize={medium}",
#     purchase_url="https://www.1800flowers.com/beautiful-blue-phalaenopsis-orchid-157423?adid=157423LWC&adtype=pla&r=googleplarkg&adcampaign=GSC-NE-Plants+SS&adcampaignid=6737243696&adgroupid=82169669231&addisttype=u&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9FBVxiWplBZoSlG9rvxW4cV_X_99dUJPxskEcLQli7Ea40zJrgRQbkaAtj2EALw_wcB",
#     caption="In a beautiful blue color.",
#     user_id=8
# )

# vanessa6 = Post(
#     title="Goldfish Bowls",
#     photo_url="https://chairish-prod.freetls.fastly.net/image/product/sized/f79f69ef-4ca6-4d09-8c04-cc4d838f2364/goldfish-bowls-photograph-by-john-manno-3787?aspect=fit&width=1600&height=1600",
#     purchase_url="https://www.chairish.com/product/2805265/goldfish-bowls-photograph-by-john-manno?gclid=Cj0KCQjw5auGBhDEARIsAFyNm9FlR50ue9QVvfxSEIyeR8XrYmMhZvn_0lR4ocEHYGOyBgmDLud2QI0aAvr6EALw_wcB",
#     caption="Photograph by John Manno.",
#     user_id=8
# )


# rachel1 = Post(
#     title="Celsa",
#     photo_url="https://cdn-images.article.com/products/SKU13259/2890x1500/image54625.jpg?fit=max&w=2600&q=60&fm=webp",
#     purchase_url="https://www.article.com/pla/13259/celsa-blossom-pink-sofa?artcl_campignID=902447655&artcl_network=g&artcl_adgroupid=45321893032&artcl_keyword&artcl_source=google&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9HbZC1SgHVrqOmOwvXej7toLaxB_AWt__F2l5Y5GoeaDBYwAFDBafoaAjk-EALw_wcB",
#     caption="In Blossom Pink and Oak color.",
#     user_id=9
# )

# rachel2 = Post(
#     title="Sven",
#     photo_url="https://cdn-images.article.com/products/SKU350F/2890x1500/image39247.jpg?fit=max&w=4684&q=50",
#     purchase_url="https://www.article.com/pla/11810/sven-cascadia-blue-right-sectional-sofa",
#     caption="This is Cascadia Blue",
#     user_id=9
# )

# rachel3 = Post(
#     title="Novogratz",
#     photo_url="https://ashleyfurniture.scene7.com/is/image/AshleyFurniture/U600001079_1?$AFHS-PDP-Zoomed$",
#     purchase_url="https://www.ashleyfurniture.com/p/novogratz__upholstered_velvet_cassidy_convertible_couch/U600001079.html?mrkgcl=1069&product_id=U600001079&google_pla=true&&mrkgadid=1&mrkgen=&mrkgbflag=&mrkgcat=&&acctid=21700000001497894&dskeywordid=92700063943962509&lid=92700063943962509&ds_s_kwgid=58700007031165557&ds_s_inventory_feed_id=97700000003427474&dsproductgroupid=1280907904009&product_id=U600001079&merchid=102213865&prodctry=US&prodlang=en&channel=online&storeid=%7bproduct_store_id%7d&device=c&network=u&matchtype=&locationid=9051962&creative=517422017979&targetid=pla-1280907904009&campaignid=12867062344&adgroupid=121619829516&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9FiMnJM18hhD4uXdtd9KUsKOGJCG_a_Sb2duGh5gVaWIpKDQqIdmtIaAqjqEALw_wcB&gclsrc=aw.ds",
#     caption="Vintage in design, is upholstered.",
#     user_id=9
# )

# rachel4 = Post(
#     title="Timber",
#     photo_url="https://cdn-images.article.com/products/SKU12813/2890x1500/image46886.jpg?fit=max&w=2600&q=60&fm=webp",
#     purchase_url="https://www.article.com/pla/12813/timber-rain-cloud-gray-right-sectional",
#     caption="Perfect for a Sunday evening.",
#     user_id=9
# )

# rachel5 = Post(
#     title="Andes",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202121/0046/img5z.jpg",
#     purchase_url="https://www.westelm.com/products/build-your-own-andes-sectional-petite-depth-h5875/?catalogId=71&sku=5585611&cm_ven=PLA&cm_cat=Google&cm_pla=Furniture%20%3E%20Sectionals&region_id=708530&cm_ite=5585611&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9HjDUF-LpSj5uZl6lKi3EPXQlDJJdJqmVKVWeUyucCmQIoYs9PrGWIaAnfkEALw_wcB",
#     caption="Distressed Velvet, Mineral Gray",
#     user_id=9
# )

# rachel6 = Post(
#     title="Syliva",
#     photo_url="https://secure.img1-fg.wfcdn.com/im/77542735/resize-h2458-w3200%5Ecompr-r85/9536/95366618/Syliva+80%27%27+Velvet+Recessed+Arm+Sleeper.jpg",
#     purchase_url="https://www.wayfair.com/furniture/pdp/orren-ellis-syliva-80-velvet-recessed-arm-sleeper-w002291296.html",
#     caption="80inch Velvet Recessed Arm Sleeper",
#     user_id=9
# )

# gina1 = Post(
#     title="Tiger in the Jungle",
#     photo_url="https://desenio.com/bilder/artiklar/zoom/3147_2.jpg?imgwidth=435&qt=",
#     purchase_url="https://desenio.com/us/tiger-in-jungle-30x40",
#     caption="See who's creepin in the jungle.",
#     user_id=10
# )

# gina2 = Post(
#     title="Tiger Landscape",
#     photo_url="https://i.etsystatic.com/15309855/r/il/a13fa9/3116849875/il_1588xN.3116849875_pfao.jpg",
#     purchase_url="https://www.etsy.com/listing/1015708575/tiger-landscape?gpla=1&gao=1&",
#     caption="Design of a tiger in the jungle surrounded by flowers and animals.",
#     user_id=10
# )

# gina3 = Post(
#     title="Big black cat",
#     photo_url="https://desenio.com/bilder/artiklar/zoom/2273_2.jpg?imgwidth=435&qt=",
#     purchase_url="https://desenio.com/us/black-panther-50x70",
#     caption="Black panther poster",
#     user_id=10
# )

# gina4 = Post(
#     title="Meet Loki",
#     photo_url="https://s7d5.scene7.com/is/image/Anthropologie/48605034_020_b?$a15-pdp-detail-shot$&fit=constrain&fmt=webp&qlt=80&wid=1080",
#     purchase_url="https://www.anthropologie.com/shop/loki-the-lion-stuffed-animal?color=020&size=One%20Size&inventoryCountry=US&countryCode=US&type=STANDARD&quantity=1",
#     caption="This is Loki the Lion Stuffed Animal.",
#     user_id=10
# )

# gina5 = Post(
#     title="Tiger Plushie",
#     photo_url="https://canary.contestimg.wish.com/api/webimage/5a698f8cd20e93700a9b2767-large.jpg?cache_buster=85d0d13fa445b29cd94ff96be2f8dff8",
#     purchase_url="https://www.wish.com/product/5a698f8cd20e93700a9b2767?from_ad=goog_shopping&_display_country_code=US&_force_currency_code=USD&pid=googleadwords_int&c=%7BcampaignId%7D&ad_cid=5a698f8cd20e93700a9b2767&ad_cc=US&ad_lang=EN&ad_curr=USD&ad_price=19.00&campaign_id=7203534630&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_pBmXRzsGkYOhvinnt3uUE9my57hJjfmUR_Bdv77atWY9dwcmHhThBoC8o4QAvD_BwE&hide_login_modal=true&share=web",
#     caption="Soft and cuddly kids toys for those who love tigers.",
#     user_id=10
# )

# bob1 = Post(
#     title="Magical Day cookies",
#     photo_url="https://cdn2.cheryls.com/wcsstore/CherylAndCompany/images/catalog/cco_VDY20_215631x.jpg?width=545&height=597&quality=80&auto=webp&optimize={medium}",
#     purchase_url="https://www.cheryls.com/have-a-magical-day-cookie-pail-cco-vdy20-215631?selectSku=215631&r=mercentfeed&camid=471_6542825959_215631&g_acctid=3302942173&g_campaignid=6542825959&g_adgroupid=81667072954&g_adid=385700845897&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_nhK_jJS_G06KDdeyLPVfYau6G8sw_Pzxzie219f3y7MwtCFACUsxxoCeaIQAvD_BwE",
#     caption="To remind you to have a magical day!",
#     user_id=11
# )

# bob2 = Post(
#     title="Classic Cookie basket",
#     photo_url="https://cdn1.harryanddavid.com/wcsstore/HarryAndDavid/images/catalog/18_26633_30XP_01ex.jpg?width=545&height=597&quality=80&auto=webp&optimize={medium}",
#     purchase_url="https://www.harryanddavid.com/h/bakery/cookies-brownies/26633?utm_medium=organic&utm_source=google&utm_campaign=organicshopping",
#     caption="Sweet tooth cookie basket gift.",
#     user_id=11
# )

# bob3 = Post(
#     title="Gourmet Cookie Basket",
#     photo_url="https://assets.wsimgs.com/wsimgs/ab/images/dp/wcm/202112/0052/img48o.jpg",
#     purchase_url="https://www.williams-sonoma.com/products/assorted-gourmet-cookie-box/?catalogId=79&sku=8625243&cm_ven=FreePLA&cm_cat=Google&cm_pla=Food%20%3E%20Cookies&region_id=708530",
#     caption="With (almost) all the colors of the cookie rainbow.",
#     user_id=11
# )

# bob4 = Post(
#     title="Buttercream Cookies",
#     photo_url="https://cdn1.cheryls.com/wcsstore/CherylAndCompany/images/catalog/cco_FAL21_226621x.jpg?width=545&height=597&quality=80&auto=webp&optimize={medium}",
#     purchase_url="https://www.cheryls.com/buttercream-frosted-salty-caramel-cookie-sampler-fal21-226621?selectSku=226621&utm_medium=organic&utm_source=google&utm_campaign=organicshopping",
#     caption="Cookie sampler.",
#     user_id=11
# )

# molly1 = Post(
#     title="Bamboo Palm",
#     photo_url="https://bloomscape.com/wp-content/uploads/2020/08/bloomscape_bamboo-palm_slate.jpg?ver=279483",
#     purchase_url="https://bloomscape.com/product/bamboo-palm/?attribute_pa_pot=slate&utm_source=Google%20Shopping&utm_campaign=Google%20Shopping%20Feed&utm_medium=cpc&utm_term=176756&&utm_source=google&utm_medium=cpc&utm_campaign=&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_qsfcMF3-2gZkd3FpaqUgOxr9NfODuns8F--i8b4lWgjrA7kzKf_nhoC-d0QAvD_BwE",
#     caption="Such a cool looking fern.",
#     user_id=12
# )

# molly2 = Post(
#     title="Trailing Succulent",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202117/0098/img6o.jpg",
#     purchase_url="https://www.westelm.com/products/faux-trailing-succulent-pure-white-ceramic-planter-set-d7154/?catalogId=71&sku=5009695&cm_ven=PLA&cm_cat=Google&cm_pla=Garden%20%3E%20Planter%20%2B%20Plant%20Sets&cm_ite=5009695&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_lFSzxUeLFmJoDSAMoKjjADupmAsIe-RjDh43V_WS3-ahYiDK3SVsxoCq4wQAvD_BwE#viewLargerHeroOverlay",
#     caption="For those who can't keep up with watering their plants.",
#     user_id=12
# )

# molly3 = Post(
#     title="Dracaena Rikki Cane",
#     photo_url="https://bloomscape.com/wp-content/uploads/2020/11/bloomscape_dracaena-rikki-cane_stone-scaled.jpg?ver=333303",
#     purchase_url="https://bloomscape.com/product/dracaena-rikki-cane/?attribute_pa_pot=stone&utm_source=Google%20Shopping&utm_campaign=Google%20Shopping%20Feed&utm_medium=cpc&utm_term=353800&&utm_source=google&utm_medium=cpc&utm_campaign=&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_i7NG0WobLrJXbf7rCv0g-k88_nen8zD-VWh_O-I5-xPEL7O6vTmwxoC4JAQAvD_BwE",
#     caption="Lookin pretty and proper and green.",
#     user_id=12
# )

# molly4 = Post(
#     title="Cast Iron Plant",
#     photo_url="https://cdn.shopify.com/s/files/1/0062/8532/8445/products/Cast_Iron_Plant_6_BB_1024x1024.jpg?v=1611594152",
#     purchase_url="https://www.brighterblooms.com/products/cast-iron-plant?variant=37941232926894&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_gC43yTPysmFqTFvqsKkrz758bGLzLVNdDwWjDFdkPayjkYGl2NpxhoC10IQAvD_BwE",
#     caption="Needing more greenery in our work from home office.",
#     user_id=12
# )

# molly4 = Post(
#     title="Monstera Leaf",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202115/0522/img4z.jpg",
#     purchase_url="https://www.westelm.com/products/monstera-leaf-d3773/?catalogId=71&sku=241633&cm_ven=PLA&cm_cat=Google&cm_pla=Garden%20%3E%20Faux%20Plants%20%2B%20Flowers&region_id=708530&cm_ite=241633&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_rWgUksnX4ohiMcj_yObZgz26qlLRx7nhbEMWaK2gs0oIB4TWuNY6BoCj_4QAvD_BwE",
#     caption="Who else has a green thumb on here?",
#     user_id=12
# )

# molly5 = Post(
#     title="Leafy Green Plant",
#     photo_url="https://akamai-scene7.grandinroad.com/is/image/frontgate/166148_main?$wgih$",
#     purchase_url="https://www.grandinroad.com/leafy-green-plant/1337159?listIndex=0&offers_sku=166148&intlShippingCtx=US%7CUSD&SourceCode=ZZ753369&utm_source=google&utm_medium=organic&utm_campaign=unpaid&CAWELAID=120245400000304024",
#     caption="Decorative, artificial leafy lush plant.",
#     user_id=12
# )

# molly6 = Post(
#     title="Candid Green Plant",
#     photo_url="https://i.etsystatic.com/25794530/r/il/ba6e1d/2665944769/il_1588xN.2665944769_c5c4.jpg",
#     purchase_url="https://www.etsy.com/listing/880037212/green-plant?gpla=1&gao=1&",
#     caption="Serene and pretty.",
#     user_id=12
# )

# patty1 = Post(
#     title="The Farmstand",
#     photo_url="https://images.ctfassets.net/tjhwhh07rwer/2sOYcDUtPM9wwOi3zzNl9S/6109ef4b8fda2015119ad9a44a2e918a/Farmstand-24.jpg?w=1920&h=1920&q=70&fm=webp",
#     purchase_url="https://www.lettucegrow.com/the-farmstand/24/?utm_source=google&utm_medium=cpc&utm_campaign=smart%20shopping&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_uVgqez4CCQkVSGOSzJNFhBxP1i4jrp4Vde8wvPRk333o3XWD4K1eBoCbxEQAvD_BwE",
#     caption="Self-watering and self-fertilizing.",
#     user_id=13
# )

# patty1 = Post(
#     title="Bird of Paradise",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202112/0158/img41o.jpg",
#     purchase_url="https://www.westelm.com/products/faux-potted-bird-of-paradise-plant-d11494/?catalogId=71&sku=7817814&cm_ven=PLA&cm_cat=Google&cm_pla=Garden%20%3E%20Faux%20Plants%20%2B%20Flowers&region_id=708530&cm_ite=7817814&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_j-LeeYYMv2O9k4iwOm1k0mMh09Oi0o99BNXxcd9F_npgaespF0IdBoCo30QAvD_BwE",
#     caption="Potted and 6ft. tall.",
#     user_id=13
# )

# patty2 = Post(
#     title="Zamioculcas Zamiifolia",
#     photo_url="https://cdn1.1800flowers.com/wcsstore/Flowers/images/catalog/157626mtempx.jpg?width=545&height=597&quality=80&auto=webp&optimize={medium}",
#     purchase_url="https://www.1800flowers.com/zz-plant-zamioculcas-zamiifolia-157626?adid=157626M&adtype=pla&r=googleplarkg&adcampaign=GSC-NE-FDAY+Gifts+SS&adcampaignid=13443042704&adgroupid=126926841081&addisttype=u&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_utlng5B3bq7jGGiy8k--cybYi_leSyVwxfV2_p35y5Kep-4_2yZrxoCjt0QAvD_BwE",
#     caption="The interesting Zz Plant.",
#     user_id=13
# )

# patty3 = Post(
#     title="Dried Pepper Grass",
#     photo_url="https://cdn.shopify.com/s/files/1/0051/8373/3878/products/060320_Lepidium_301_50_1949x.jpg?v=1623789524",
#     purchase_url="https://bloomist.com/products/dried-lepidium-pepper-grass?variant=34589077307555&utm_medium=adwords&utm_campaign=&utm_source=Google&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_oi2BNecQJSofl0QxIhjKXQvDf3jby1KmP3FUvwT2JIo33OvydSVqxoCcwwQAvD_BwE",
#     caption="at Bloomist",
#     user_id=13
# )

# patty4 = Post(
#     title="Majesty Palm",
#     photo_url="https://www.plants.com/images/1566416548156_20190821-1566416549015.webp",
#     purchase_url="https://www.plants.com/p/majesty-palm-floor-plant-157652-2?pla=9339&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_jqFgTQqKfUsx44HYJ_Uh7kDojLRx6xOYv2fag-6iNoFwjgXqS9ushoCEToQAvD_BwE",
#     caption="Floor plant",
#     user_id=13
# )

# patty5 = Post(
#     title="Potted Snake Plant",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202115/0673/img39o.jpg",
#     purchase_url="https://www.westelm.com/products/faux-botanicals-potted-snake-plant-d5383/?catalogId=71&sku=7931581&cm_ven=PLA&cm_cat=Google&cm_pla=Garden%20%3E%20Faux%20Plants%20%2B%20Flowers&region_id=708530&cm_ite=7931581&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_lM9UPHMAMg_2yxrr9F6cQbHod0yJ2pHtueVgLEiUQBP0nGmEmLwHBoCu4oQAvD_BwE",
#     caption="The lovely botanicals.",
#     user_id=13
# )

# patty6 = Post(
#     title="The Emerald",
#     photo_url="https://www.openblooms.com/wp-content/uploads/2018/09/OB18-SS17.jpg",
#     purchase_url="https://www.openblooms.com/product/the-emerald/?gclid=CjwKCAjwiLGGBhAqEiwAgq3q_rCRuqWvUwWkDogcJfyQCoZM4SD2tajUtcQVwfnl9cvY1s4WEqn39hoCtpQQAvD_BwE",
#     caption="There's no place like home.",
#     user_id=13
# )

# patty7 = Post(
#     title="Fig Leaf",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202122/0108/img1o.jpg",
#     purchase_url="https://www.westelm.com/products/faux-fiddle-plants-fig-leaf-d8917/?catalogId=71&sku=3042664&cm_ven=PLA&cm_cat=Google&cm_pla=Garden%20%3E%20Faux%20Plants%20%2B%20Flowers&region_id=708530&cm_ite=3042664&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_tjIkNp-QxAzB4n2MtUuwCs9qqgHcsWFlr0_iMjve99nh2cFTYfUwBoCkvYQAvD_BwE",
#     caption="This is 2ft high.",
#     user_id=13
# )

# patty8 = Post(
#     title="Gingko Branch",
#     photo_url="https://assets.weimgs.com/weimgs/ab/images/wcm/products/202103/0051/img85o.jpg",
#     purchase_url="https://www.westelm.com/products/faux-gingko-branches-d8680/?catalogId=71&sku=7885876&cm_ven=PLA&cm_cat=Google&cm_pla=Garden%20%3E%20Faux%20Plants%20%2B%20Flowers&region_id=708530&cm_ite=7885876&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_kQMXVBOnzslqa0SiyHWOZAvCp_ULD6Yl7eRYt_AsN6AdT__JcqX2hoCaHsQAvD_BwE",
#     caption="The upkeep is eternal.",
#     user_id=13
# )

# patty9 = Post(
#     title="Sympathy Potted Corn Plant",
#     photo_url="https://www.avasflowers.net/img/prod_img/avasflowers-sympathy-potted-corn-plant.jpg",
#     purchase_url="https://www.avasflowers.net/product/sympathy-potted-corn-plant/21582?gclid=CjwKCAjwiLGGBhAqEiwAgq3q_ivPPowm_faiiOViX8wkZliYWGnQvJ0fyh7p7Y7SC_CgJAqJuwf_iRoChHYQAvD_BwE",
#     caption="Is to serve as a tribute to a loved one lost.",
#     user_id=13
# )

# patty10 = Post(
#     title="Tula Planter",
#     photo_url="https://assets.pbimgs.com/pbimgs/rk/images/dp/wcm/202109/3472/img5o.jpg",
#     purchase_url="https://www.potterybarn.com/products/tula-planter-collection-fmp/?catalogId=84&sku=3212590&cm_ven=PLA&cm_cat=Google&cm_pla=Outdoor%20%26%20Garden%20%3E%20Planters&region_id=708530&cm_ite=3212590&gclid=CjwKCAjwiLGGBhAqEiwAgq3q_gAbBmFHjIyReKiYs8okKGD-7Twyuk2OZGcMxobeWNC85JjeOe80jRoCW1wQAvD_BwE",
#     caption="Terra Cotta",
#     user_id=13
# )



# db.session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13])

# db.session.commit()

# db.session.add_all([rose7, amy2, vanessa6, teddy1, bob3, patty6, vanessa1, amy1, gina5, mark1, 
# sarah2, patty4, rachel2, bob4, amy5, molly6, patty5, sarah1, gina4, violet6, rose5, sarah3, 
# vanessa5, rachel5, amy3, marvin4, patty3, rose3, marvin2, violet8, gina1, molly5, patty10,
# rachel1, violet2, patty9, vanessa2, mark2, marvin3, rose1, molly4, violet4, amy4,
# rose2, gina3, vanessa3, patty8, rose4, rose6, violet1, molly3, bob2, sarah4, rachel3,
# vanessa4, patty2, violet5, marvin1, rachel4, teddy2, mark3, patty7, violet3, teddy3, violet7, 
# gina2, molly2, patty1, bob1, rachel6, molly1])

# db.session.commit()

