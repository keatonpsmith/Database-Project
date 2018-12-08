Names: Ikra Rashid, Keaton Smith, Antoine Assaf, Jahlil Walker 

Additional Features: 

Feature: Remove user from group
Name: Jahlil
Why it is a good feature: A user can remove another user from a group. This will allow users to be in control of their friend group space. 
Changes to database: No changes to the database schema. 
Queries: 
Source code destination: Located on line 172 in file main.py and the HTML code is in file old_user.html

Feature: View Own Posts
Name: Keaton
Why it is a good feature: This feature allows for users to view all of their own posts, whether or not public or private. This allows for the user to access their own data whenever they wish, as compared to how they were initially only able to see all public posts within the last 24 hours. 
Changes to database: No changes to the database schema.
Queries: 
query = 'SELECT * FROM contentitem NATURAL LEFT JOIN share WHERE email_post = %s OR item_id IN (SELECT item_id FROM share NATURAL JOIN belong WHERE email = %s) ORDER BY post_time DESC'
Source code destination: The query and the code associated with the query above can be found in the main.py file on line 196

Feature: Create Group 
Name: Jahlil 
Why it is a good feature: This allows for a user to make a group of their own so that they aren’t only being added to set groups. This will allow for the application to be more flexible and connect people together. 
Changes to database: No changes to the database schema
Queries: query = 'INSERT INTO friendgroup (owner_email,fg_name) VALUES(%s,%s)'
Source code destination: The query and the code associated with the query above can be found in the main.py file on line 186.  HTML code is in file new_group.html

Feature: Leave Group
Name: Ikra
Why it is a good feature: This feature allows for a user to have the ability to leave a group. This way, they are not required to stay in a group they no longer want to be in, and don’t have to rely on the owner to drop them. 
Changes to the database: No changes to the database schema 
Queries: DELETE FROM belong WHERE email = %s AND fg_name = %s
Source code destination: The query and the code associated with the query can be found on line 236 in file main.py and the HTML code for leaving the group can be found in leave_group.html.

Feature: Add comments 
Name: Antoine 
Why it is a good feature: Users can respond and be able to express their thoughts on the contents posted by themselves and other users. It is a good way to promote social interactions via the platform. 
Changes to the database: Added the table comments with keys (commentor, comment, item_id, commenttime) to handle the existence of commments.
Queries: INSERT INTO comments VALUES (%s, %s, %s, %s)
query = 'SELECT item_id FROM contentitem WHERE item_id IN (SELECT item_id FROM contentitem NATURAL LEFT JOIN share WHERE email_post = %s OR item_id IN (SELECT item_id FROM share NATURAL JOIN belong WHERE email = %s))'
Source code destination: The query and the code associated with the query above can be found in the main.py file on line 215.  HTML code is in file create_comments.html

Feature: View comments
Name: Antoine
Why it is a good feature: This feature allows for a view all comments on any posts they can regularly view. It displays the Commenter’s email, the post with which it is associated, the content of the comment, and the time of the comment.
Changes to the database: No additional features from the Add Comments feature.
Queries: SELECT * FROM comments NATURAL LEFT JOIN share WHERE commentor = %s OR item_id IN (SELECT item_id FROM share NATURAL JOIN belong WHERE email = %s) ORDER BY commenttime DESC
Source code destination: The query and the code associated with the query above can be found in the main.py file on line 206.  HTML code is in file comments.html
