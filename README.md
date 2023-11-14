Author: Miles Anderson
Email: mander20@uoregon.edu
Description: This project provides a brevets control calculator. The algorithm takes the total distance of the brevets, the distance of the control, and the start time of the race. It uses these to compute the opening and closing times for the checkpoint at the given control. To start the program you should make sure you are in the brevets subdirectory so docker can read the Dockerfile. Then type in the docker build and run commands, specifying the port within the docker run command. Once on the webpage the user can choose the total distance of the brevets race and the start time of the race. The user can then enter the distance of the first control (either in miles or kilometers). After hitting enter the opening and closing times for that control will be displayed.

Control Calculation rules:
For calculating control times there are set maximum and minimum speeds which are divided by the control distance. Which maximum or minimum speed is used depends on the distance of the control from the beginning control. We use the maximum speeds for finding the opening times and the minimum speeds for finding the closing times. 

# UOCIS322 - Project 5 #
Brevet time calculator with MongoDB!

## Overview

You'll add a storage to your previous project using MongoDB and `docker-compose`.
As we discussed, `docker-compose` makes it easier to create, manage and connect multiple container to create a single service comprised of different sub-services.

Presently, there's only a placeholder directory for your Flask app, and a `docker-compose` configuration file. You will copy over `brevets/` from your completed project 4, add a MongoDB service to docker-compose and your Flask app. You will also add two buttons named `Submit` and `Display` to the webpage. `Submit` must store the information (brevet distance, start time, checkpoints and their opening and closing times) in the database (overwriting existing ones). `Display` will fetch the information from the database and fill in the form with them.

Recommended: Review [MongoDB README](MONGODB.md) and[Docker Compose README](COMPOSE.md).

## Tasks

1. Add two buttons `Submit` and `Display` in the ACP calculator page.

	- Upon clicking the `Submit` button, the control times should be inserted into a MongoDB database, and the form should be cleared (reset) **without** refreshing the page.

	- Upon clicking the `Display` button, the entries from the database should be filled into the existing page.

	- Handle error cases appropriately. For example, Submit should return an error if no control times are input. One can imagine many such cases: you'll come up with as many cases as possible.

2. An automated `nose` test suite with at least 2 test cases: at least one for for DB insertion and one for retrieval.

3. Update README.md with brevet control time calculation rules (you were supposed to do this for Project 4), and additional information regarding this project.
	- This project will be peer-reviewed, so be thorough.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* Front-end implementation (`Submit` and `Display`).
	
	* Back-end implementation (Connecting to MongoDB, insertion and selection).
	
	* AJAX interaction between the frontend and backend (AJAX for `Submit` and `Display`).
	
	* Updating `README` with a clear specification (including details from Project 4).
	
	* Handling errors correctly.
	
	* Writing at least 2 correct tests using nose (put them in `tests`, follow Project 3 if necessary), and all should pass.

* If DB operations do not work as expected (either submit fails to store information, or display fails to retrieve and show information correctly), 60 points will be docked.

* If database-related tests are not found in `brevets/tests/`, or are incomplete, or do not pass, 20 points will be docked.

* If docker does not build/run correctly, or the yaml file is not updated correctly, 5 will be assigned assuming README is updated.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
