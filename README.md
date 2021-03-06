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

## User Interaction Guide

**Search by Chapter Number:**
    By typing in a chapter number into the first input box, the user can view the content of a particular chapter in the book of Psalms.
    After entering a chapter number, the user can click the "Go To" button to view results in the textbox at the bottom of the page. Results can also be viewed using a scroll bar.

    Test Case:
        1. Enter "1" into the "Enter Chapter Number" input box.
        2. Click Go To button.



**Search by Verse Number:**
    By typing in a particular chapter number and verse number into their separate input boxes, the user may view the results of a particular verse   upon clicking the "Go To" button.
   
    Test Case:
        1. Enter "1" into the "Enter Chapter Number" input box.
        2. Enter "2" into the "Enter Verse Number" input box.
        3. Click Go To button.



If the user does not input a chapter number or a verse number and clicks the "Go To" button, then the results will be the entire book of Psalm. 
Also, if the user inputs invalid chapter numbers of verse numbers, then they will receive an alert message.


**Search by Keyword:**
    The user can type in a particular keyword and upon clicking the "Go To" button, will be able to view all the verses that have that keyword in it. We also have implemented a "fuzzy search" feature. This means that if a user attempts to search for a particular keyword that is not within the book of Psalms, similar results will still pop up.  For example, the word "aladdin" would likely not be in the book of Psalms, but you could search by it and find verses with words that have similar spellings.
    
    Test Case:
        1. Enter "rod" into the "Enter a Keyword to Search by:" input box.
        2. Click magifying glass button.
        3. Enter "aladdin" "Enter a Keyword to Search by:" input box.
        4. Click magnifying glass button.




**My Favorites:**
    Located in the top right hand corner, the My Favorites button takes the user to a page in which they can add there favorites verses to a textbox located at the bottom of the page. 

**Add to "My Favorites":**
    The user can type in a chapter number and verse number and add a verse to the bottom textbox by clicking the "Add to MyFavorites" button. The results of adding a favorite can be viewed at the bottom of the page. The user can also use a scroll bar to view the results.
    
    Test Case: 
        1. Click MyFavorites button from home page.
        2. Type Chapter Number "1" into "Enter Chapter Number" textbox.
        3. Type Verse Number "1" into "Enter Verse Number" textbox.
        4. Click add to "My Favorites" button.




**Delete from "My Favorites":**
    The user can delete a verse from their favorite verse section by typing in the chapter number and verse number and clicking "Delete from "My Favorites".
 
    Test Case: 
        1. Click MyFavorites button from home page.
        2. Type Chapter Number "1" into "Enter Chapter Number" textbox.
        3. Type Verse Number "1" into "Enter Verse Number" textbox.
        4. Click "Delete from My Favorites" button. Alternatively, the user may click an "X" button beside each verse to delete the verse.



**Clear all in "My Favorites":**
    If the user wants to delete all the verses in the "My Favorites" section, then they can click the Clear all in "My Favorites" button.

**Recommendation for You:**
    If the user has verses inside of the "My Favorites" section, then they can click the "Recommedation for You" button to view a list of recommended verses, which are similar to the verses located in their "My Favorites" section. If the user adds more verses to their favorites, then this recommendation list can be updated by clicking the "Recommendation for You" button again. Results should appear in the "You Might Also Like:" text box.

**Email:**
    The user can send either of us an email by clicking on our netids in the top right hand corner.

    Test Case: 
       1. Click on ccolon2 in top right hand corner.
       2. Type in email you want to send and send it.

## Complexity
We have implemented the follwing features:
* Show the whole book
* Search by chapter number
* Search by chapter number and verse number
* Search by keyword ([fuzzy-search] included)
* My Favorite Module (add, delete, clear verses)
* Recommendation system (using [SentenceTransformers])

All features are supported by the frontend

## Installation
### Using Anaconda
If you are using [Anaconda], just run the following command:
```bash
conda env create --file conda/environment.yml
```
### Manual Installation
```bash
pip install CherryPy
pip install numpy
pip install scikit-learn
pip install torch
pip install tqdm
pip install fuzzysearch
pip install sentence-transformers
```
## Usage
* To ensure best performance, download [similarity_matrix.pickle] and [cosine_scores.npy] and put them under ./data
* If you do not include similarity_matrix.pickle in the project, the code will require the calcualtion of the similarity matrix. The code requires cosine_scores.npy to calulate the similarity matrix **without using GPU**.
* If you do not include cosine_scores.npy when the calculation of the similarity matrix is needed, the calculation could take **up to a few minutes**.
* Run the following commands:
```bash
cd server
python3 server.py
```

[Final Project]: https://docs.google.com/document/d/15YQbpM2lFVR3J5dg1RQ0uKpSqXaUg0zSrnoFMKk1HKc/edit
[CSE 30332 Programming Paradigms]: https://www3.nd.edu/~skumar5/teaching/2020-fall-pp.html
[fuzzy-search]: https://fuzzysearch.readthedocs.io/en/latest/
[SentenceTransformers]: https://www.sbert.net/
[Anaconda]: https://www.anaconda.com/
[similarity_matrix.pickle]: https://drive.google.com/file/d/1n8VpTT3Sa5DrqK9B1VaD6SyoHYaO-M_Y/view?usp=sharing
[cosine_scores.npy]: https://drive.google.com/file/d/1EO9LnRubEy-aS8qkJg8StyhkCEd3i4kM/view?usp=sharing