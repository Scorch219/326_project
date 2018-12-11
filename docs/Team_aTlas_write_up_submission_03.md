Project 3 Team Write-Up


Overview:
For our UMarket website, we were successfully able to create a user login/logout functionality, which can now be used to change a user’s seller rating, maintain their wishlist, and manage their items for sale. Further, we were able to implement user interaction in forms by allowing them to add a new item the user may wish to sell, and upload it onto the main listing for everyone to see. Each listing contains a picture of the item, Title, description, price, seller rating, and an “I’m Interested” Button which will be later implemented for sales.


Team Members:
Tajour Cohen-Henry
Brandon Curran
John Domenichelli
Aristotel Fani
Ashley Tapulado
Quyen Tran


Video Link: https://youtu.be/_fEhWJkAukw



Design Overview:
Our design includes a Sign-In option at the bottom of our home page. Pressing that option takes you to new page, with username and password fields to fill out. It correctly searches for names and passwords from database, and brings the user to their user page, displaying their name, rating, email address, and a listing of each item they are currently selling.

The user page also contains the “add+” button, which, when pressed, takes the user to a page where they can fill in the necessary data to upload their item to sell in the main listing. After submitting the item, the user is taken to the product listing page where they can see what they’ve just posted.


Problems/Successes:
Creating a subclass for the user profile, so we could add our own custom fields beside the defaults in Django.
Correct URL mappings,
Producing product page
Interpreting the tutorial videos and example code



Team Choice:

	Overall changes we plan to implement include adding CSS changes which clean up the overall appearance and color scheme of the website. Also, we have an “I’m Interested” button which needs to lead to allow the user to buy/sell a given item. For Seller rating, we need to modify our existing code so that the user cant rate him/herself, as well as producing averages for ratings, ensuring the user cant buy own product, etc. Further, we would like to create a filtering option to sort items in the listing by price and category. Lastly, we would like to create a means of deleting sold/pulled items from the listing.
