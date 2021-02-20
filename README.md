# assignment-2-API

## Description:

This is a API assignment written in **Django Rest Framework** for returning number of occurence of words like
"the", "this", "there" in uploaded .txt file

## Steps:
Step 1: 
> Create python3 virtualenv

Step 2: 
> Activate virtualenv according to your OS

Step 3: Install the require packages from requirements.txt file
> `$: pip intall -r requirements.txt`

Step 4: Making migration of database on your local machine
> `$: python manage.py makemigrations`

Step 5: 
> `$: python manage.py migrate`

Step 6: Run Django Server
> `$: python manage.py runserver`

Step 6: After running a server send a .text file to the server using CURL
> `$: curl -X POST -F upload=@"C:\Users\USER\Desktop\test.txt" http://localhost:8000/getnumbers/`

