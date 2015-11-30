# Friends Challenge

Challenge proposed as test for an interview.

This Django app creates a RESTful API for the given situation:

As a popular developer you know a lot of people in your country. You are a person that travel a lot,
so you decided to create a software that tells you who are your friends that are nearest to you, based on 
the friend that you curretly are. Every one of your friend live in a specific position in a cartesian world,
that is their coordinates are cartesian so their location are points (x, y). Suppose that you can, somehow, identify
the location of your friends and that two friends are never in the same place.

Requirements:
 - REST API of your friends;
 - A route to show you the 3 friends that are closer to you;
 - A makefile with the tasks:
     - install: to install project requirements
     - run: to run the app
     - stop: to stop the app
 - Command line client to interact with the API
 - A repo at github (this one :) )
 - A README file (also this one :) )
 
 ## API
 
Every endpoint at this API return and expect a JSON

---
 
 - /me
   - Return my current position and id
 - /me/nearest
   - Return the 3 friends that are closer to me
 - /me/nearest/<number>
   - Return the <number> friends that are closer to me
 - /friends
   - Get all your friends or create a new friend
 - /friends/<number>
   - Get, update or delete the friend with id <number>
 - /route/to/<number> | /route/from/me/to/<number>
   - Return the route from you to your friend with id <number>
 - /route/from/<number1>/to/<number2>
   - Return the route from someone with id <number1> to someone with id <number2>
 - /reset
   - Reset the current position of everybody, including me, also delete any added friend
 
 ---
 Note that since this world is cartesian, the route from any place to any other place 
 is the straight path connecting the two set of points representing those places: (x1, y1) and (x2, y2).
 
 ---


## Route

  - A route is given through the API


## Makefile
 
   - TBD


## Client

   - TBD (but the API is browsable, try it)

