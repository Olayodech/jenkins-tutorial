# jenkins-tutorial

Use case diagram

Mepot -- Is an ecommerce application which has two main actors: Customer and admin.
See use case diagram: mepotschema.png

Both actors can perform different actions.

 A customer can browse the home page of the application for all products listed and add an item to cart. To add an item to cart, the customer must have a session, thus must be registered and logged in. A customer can delete the cart ot proceed to checkout. Carts and checkout requires customers to be registered and login


An admin can manage the application for products listed, add new products to be listed on the home page, a user can view all orders placed and manage orders if it can be fulfilled or not (Note this is to be replaced by automated system using event processing depending on stock level)

Database schema
Currently, the application only has Product and Customer database model. However the remaining part of the schema is to be implemented phase by phase.

See schema screenshot
usecase.png

Technology stack:

See attached image
techstack.png


Development:
    The project is split into sprint using jira. See jira.png.

Deployment:
    Deployment of the app is based of git webhook from jenkins which is trigger on pushing from the local dev environment. 
    See jenkins pipeline.png

Future improvement:
    Fix mysql db connection issue on docker
    Fix the product listing page css for user acceptance
    Implement Checkout page 
    Implement password recovery using sendgrid for email
    

CHALLENGES

- 1: As can be seen in the video, the local environment, the app works using a different directory structure which can be found in "MEPOT-ORIGINAL", it uses main.py as the entry point and flask run, however, I couldn't connect to port 5000
when running in docker (I discussed with my trainer), however, when I stripped down the application to use app.py as entry point and run with "python3 app.py", I was able to connect to port 5000 in docker. Challenges of that
is the login functionality required for a user to go to cart and required for the login and register options to be replaced by logout in the nav bar are broken. I did not have time to fix it
given the 1 week sprint. I deployed this to docker

2: I was unable to connect to mysql with pmysql as it kept saying database in use is not found, even though I could connect to port 3306 on mysql workbench and the database and table exists.
3: At the time of writing this, docker swarm is not configured, it might be configured if I have time but I doubt it.


