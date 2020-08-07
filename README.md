# User and Activity Period details
This is the Django application with User and Activity Period details saved in the Database and can serve that data using API in JSON format.
We can populate data in the database using a custom management command.
## Usage
```bash
python manage.py add_data [user name] [start time] [end time]
```
## help

For Example : python manage.py add_data praveen 0 20
*Where praveen - user name
0 - time
