# Project - Readme
This is the [Final Project] for [CSE 30332 Programming Paradigms]

## OO API
The bible_library.py contians basically all the functions Controllers need. It implements: load data, all get method (book, chapter, verse), search by keyword, and all functions of "my favorite" module (add, delete, get).

All Controller files and the server.py import bible_library.py. 

To run the test for bible_library.py, run the following command in the ooapi folder:
```bash
python3 test_api.py
``` 

## JSON Specification
The following is the JSON Specification for our server:

| Request Type | Resource endpoint 		  				| Body										 | Expected response 								|
|:------------:| -------------------------------------- |:------------------------------------------:| ------------------------------------------------ |
| GET          | /book/            		  				| No body 									 | string formatted json of the book                |
| GET          | /book/:term       		  				| No body 									 | string formatted json of the term-related verses |
| GET          | /chapter/:chapter_number 			    | No body 									 | string formatted json of the chapter				|
| GET          | /verse/:chapter_number_verse_number    | No body  									 | string formatted json of the verse				|
| GET          | /favorite/								| No body 									 | string formatted json of the "my favorite"		|
| POST         | /favorite/								| {'chapter number': 144, 'verse number': 4} | {“result”: “success”} if operation worked		|
| DELETE       | /favorite/								| {}      									 | {“result”: “success”} if operation worked		|
| DELETE       | /favorite/:chapter_number_verse_number | {}      									 | {“result”: “success”} if operation worked		|
| GET          | /recommendation/:number				| No body 									 | string formatted json of the recommendations		|

## Server
Our server currently uses:
* host: localhost
* port: 51060

## User Interaction

 
[Final Project]: https://docs.google.com/document/d/15YQbpM2lFVR3J5dg1RQ0uKpSqXaUg0zSrnoFMKk1HKc/edit
[CSE 30332 Programming Paradigms]: https://www3.nd.edu/~skumar5/teaching/2020-fall-pp.html
