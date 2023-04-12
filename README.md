# flaskwork

To access the page for creating the database: /create
To access the page for editing the database: /edit/1 => the number is the ID of each database element, for example: /edit/2 => edit name of the second project with ID 2
To access the page for deleting element from database: /delete/1 => the number is the ID of the element like in /edit

Deployment: The application is deployed using render.com following the same steps in the tutorial provided by Samuel. The only difference is that I adjusted the version of python that render.com was using to match my version 3.8.6 and not 3.7.10.

The database is now directly editable from a page and you can create and delete content, and if you click on the projects added in the database through those pages you can access a new page that takes the name of the project and creates an automatic slug in the URL that even if you edit the name of the project, the slug will change accordingly. 
