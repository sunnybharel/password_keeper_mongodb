# password_keeper_mongodb
MongoDB based password keeper

### Pre-requisite:
Run a docker container running mongoDB on your host and run the python script on your host (not within Docker).
Command to run docker instance of mongoDB:

docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4


### Usage:

python password_keeper_mongodb.py 
```
'c' to create a record 
'v' to view all records 
'w' to filter by domain 
Any other key to quit: w
Enter partial or complete domain name to search for: insta
---
URL		instagram.com
User		Dave
Password	GreenBird34
Published	2019-11-19 14:57:53.049000
'c' to create a record 
'v' to view all records 
'w' to filter by domain 
Any other key to quit: v
---
URL		instagram.com
User		Dave
Password	GreenBird34
Published	2019-11-19 14:57:53.049000
---
URL		facebook.com
User		mama_shango
Password	Shampoo23
Published	2019-11-19 15:07:26.286000
---
URL		twitter.com
User		LouisaNameless
Password	PeanutCampa56
Published	2019-11-19 15:12:18.587000
'c' to create a record 
'v' to view all records 
'w' to filter by domain 
Any other key to quit: q

```
