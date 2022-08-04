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
