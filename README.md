## CAPSTONE 1 PROJECT PROPOSAL

#### API Links
Link to API:
https://apidocs.imgur.com/?ref=apilist.fun

Link from free API list:
https://apilist.fun/api/imgur 

imgur site:
https://imgur.com/

My account on imgur site:
https://imgur.com/user/ashleynd/posts

Schema design:
https://app.quickdatabasediagrams.com/#/d/CKfso


### Objective: A visual “wish-list”
  
The goal is to be an image sharing and social media platform designed to enable saving with a path to purchasing items on the internet using images, GIFs, and vidoes in the form of “folders”. The items a user adds to each folder will collate on the page as a collage. Items that are available for purchase will be shown on the other side of the page that includes a path to where the item can be purchased. 

### Demographics: Mostly women, Millennials, and moms 

While open to everyone, the usage will probably err more on female tastes due to its visual characteristics and shopping capabilities. But it’s for anyone who likes to make lists of items they want, and compare and contrast products and brands all in one place. The target audience will mostly be using it as an app on mobile phones. 

### The Data: Pinterest-y

The API will have Pinterest-like data, populating the site with media that users can add media and“save” to a folder. It will be a public API to obtain relevant data such as images, gifs and short videos.

### My Approach: A Home page and Tabs

### Schema
This is RESTful API based on HTTP requests and JSON responses. All requests will need to be encrypted and sent via HTTPS. This will be a 3-page application. Will include a home page showing content from other users, and a Posts and Favorites tab for the user. GET requests will be made for seeing info about a comment/image. POST requests for creating comments, votes, and uploading images. A PUT request for user to change their account settings.

### Potential API issues
I had to use a different API than what I was originally planning on. It has many of the capabilites I was hoping for. It may be difficult to manipulate or include new capabilites I was planning on. 

### Sensitive information
I need to make sure only the user can delete/edit their own posts.

### Functionality
Similar to favoriting, users can save items to a folder, create new folders, and give them a title. Users are also able to comment and "vote", or like posts from other users. Posts will also have a path to help guide the user to where to purchase the item, if available for sale.

### User Flow
The user will see the homepage when they first login. It will show the latest posts from other users. This will be a search-focused application. So the search bar will be at the top, perhaps with helpful search suggestions in the placeholder. Each image will have a "vote" button appended to it. You can view all your saved folders back in your profile page.

HTML iframe tag:
https://www.w3schools.com/tags/tag_iframe.asp

### Stretch Goals
1. To have commenting capabilities on posts. 
2. Item that can be purchased is seen in the same window, so the user doesn’t need to open a new tab. It will appear next to the post. 
3. Time permitting, it would also be fun to make a dark mode toggle. So the user can choose between a light and dark mode.


