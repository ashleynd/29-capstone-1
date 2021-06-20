-- from the terminal run:
-- psql < favorites.sql

DROP DATABASE IF EXISTS picslink;

CREATE DATABASE picslink;

CREATE TABLE users
(
  id INT PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE posts
(
  id INT PRIMARY KEY,
  title TEXT NOT NULL,
  photo_url TEXT NOT NULL,
  purchase_url TEXT,
  user_id INT FOREIGN KEY REFERENCES users(user_id)
);

CREATE TABLE favorites
(
  id INT PRIMARY KEY,
  user_id INT FOREIGN KEY REFERENCES users(user_id),
  post_id INT FOREIGN KEY REFERENCES posts(post_id)
);


INSERT INTO users
    (first_name, last_name, username, password)
VALUES
('Rose', 'Smith', 'RosyMaid', '$2b$12$HfEoLHkLzjIw3fW8TguBI.e.yvx1ZTw1hYw/zZFYjdvKUTlMzeOwC'),
('Amy', 'Hemsworth', 'AmazingAmy25', '$2b$12$YnzqYD9N3B1VPrsGvsc3Wut1s1kATallKMK9vfN.ZbK90biNv/Mim'),
('Vanessa', 'Cooper', 'HappyGoLucky23', '$2b$12$9X3V2cEI.CD045i9RnvyHer5c5E18yvQ/Rg4GZUkLBQ3AzmWhbR2y');

INSERT INTO posts
    (title, photo_url, purchase_url, caption, user_id)
VALUES
('Tiny cobalt blue sea', 
'https://i.etsystatic.com/10451613/r/il/e81a7a/1072027519/il_1588xN.1072027519_hcfh.jpg', 
'https://www.etsy.com/listing/458754514/9-15mm-04-06-tiny-cobalt-blue-sea-glass?ref=pla_sameshop_listing_top-1&frs=1', 
'cobalt seaglass blue small sea glass mosaic glass jewelry glass', 1),
('Butterfly wall', 
'https://img.ltwebstatic.com/images3_pi/2020/03/19/1584607766e1634741d4fc0f69ad9bcadb6d8d8b35_thumbnail_900x.webp', 
'https://us.shein.com/12pcs-Hollow-Butterfly-Wall-Decor-p-1060702-cat-2520.html?url_from=adplashwallart16200319968B_ssc&gclid=CjwKCAjwn6GGBhADEiwAruUcKhl3EIALpw58hJ_ZOjDNACer1mJZOoxOsWcOfWrL7xNmGKI70RwdkxoCX-sQAvD_BwE', 
'Rose gold butterflies', 2),
('Hello Sunflower', 
'https://secure.img1-fg.wfcdn.com/im/84593557/resize-h800%5Ecompr-r85/3854/38549984/Hello+Sunflower+by+Catherine+Fitzgerald+-+Wrapped+Canvas+Print.jpg', 
'https://www.wayfair.com/Artist-Lane--Hello-Sunflower-by-Catherine-Fitzgerald-Wrapped-Canvas-Print-75CF-P26-L1318-K~RTLA2659.html?refid=GX431921220665-RTLA2659&device=c&ptid=898501776691&network=g&targetid=pla-898501776691&channel=GooglePLA&ireid=38549984&fdid=1817&PiID%5B%5D=21018434&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9GIE-XroajRJt1eR2P9UOOzMdgmmIyAHhL1u6knRMgYW5esPCcf5ZsaAvDfEALw_wcB', 
'Artwork by Catherine Fitzgerald', 3),
('Bliss garden succulent', 
'https://cdn.shopify.com/s/files/1/0715/7597/products/20200324-Bliss_720px_1024x1024.jpg?v=1613315139', 
'https://www.lulasgarden.com/products/bliss-garden?variant=375915184144&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_campaign=gs-2021-04-12&utm_source=google&utm_medium=smart_campaign&gclid=CjwKCAjwn6GGBhADEiwAruUcKmv3whVesWhvjBbz9zwDulB1lR8SAFRGlhmGm9ePPthkGJnqBFIO3BoCWQYQAvD_BwE', 
'Perfect gift. The unique colors of the succulents will make their face light up.', 2);


INSERT INTO favorites (user_id, post_id)
VALUES(3, 1), (1, 2), (8, 3), (5, 4), (11, 5), (13, 6);

-- INSERT INTO favorites (user_id, post_id)
-- VALUES(1, 1), (2, 1), (3, 1), (2, 2);