Team Write Up P02

Overview:
	The purpose of our application is to provide UMass students with their own dedicated website to sell and trade items to each other, from iClickers to books to furniture. Upon making an account for free, the user will be able to post any items they wish to sell, make bids or purchases on other students’ items, and update a “wishlist” containing items they are looking to buy, in the cases where trading/bartering is the preferred means of transaction. Our project proposal has not yet required any changes since the Project 1 submission.

Team Members:

Tajour Cohen-Henry
Brandon Curran
John Domenichelli
Aristotel Fani
Ashley Tapulado
Quyen Tran


Video Link:

		https://youtu.be/5k8mLzrFkc0


Design Overview:

Data model design overview:

		We have two classes: the UserAccount class and a Product class. These are the main entities used in the database, to model the data that users will enter in our website. The UserAccount contains email, password, and name parameters to be used publicly and allow returning users to access their account. Rating is what will indicate that seller’s reputation, and provides a medium for other users to give feedback for each other. UserID is used interally to reference the user.
		As for the Product class, each product is given the parameters productID, userID, name, description, price, seller_rating, and category. Name, description, price, and category are used to provide information to the user about the product. Seller_rating contains the score of the seller’s reputation so interested buyers know if they should trust buying it.

             The important URL routes:

In each product item for sale, a link is provided through the get_absolute_url function, which sends the unique id of that product to the urlpatterns array in urls.py. It then maps to the corresponding path (views.ProductDetailView) and returns the requested data.

In reference to the other paths, the userdetail path returns any info about the user that was entered into the system, and the about path sends the user to the About page which contains information about TeamAtlas. The user path contains paths to their own personal information, as well as data on the products they are selling.

Implemented UI views:

	We implemented five pages. The Home and About page didn’t require much Django template use, compared to item listing, product, and user pages. We added Python Django property accessors to grab the data and populate the listing, user and product pages.

Problems/Successes:

In terms of our goals for our design, we were able to successfully:
Create the URL links that connect each webpage from P01
Implement the Django data model, and populate the database with mock data


In the coding aspect of the project, our biggest problem we encountered stemmed from not regularly migrating our model to Django after we made modifications to it. Since Django updates the database to adjust to our data model, making large updates instead of updating one thing at a time created a backup of errors that wouldn’t have been as troublesome otherwise. Aside from that, most members reported little-to-no major problems with their designated portion of work.

Outside of coding, the team has provided a positive, supportive attitude among the teammates, who all have different amounts of experience in web programming. Whenever a member struggled to understand a concept, anyone in the group with the relevant knowledge was always happy to lend a hand. Further, members were never particularly behind on their work at any given point, especially where their work was required for another member to continue.

To improve as a team moving forward, communication could be improved; if we were able to find a time in the week where we were all free, we would be able to collectively work on it together at the same time. Additionally, while it is difficult to properly divide the workload evenly among the team, finding a way to further ensure each member is doing a proper amount of work, in amounts that everyone is satisfied with, will continue to be a challenge to improve on.
