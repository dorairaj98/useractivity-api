# User and Activity Period details
This is the Django application with User and Activity Period details saved in the Database and can serve that data using API in JSON format.
We can populate data in the database using a custom management command.
## Usage
```bash
python manage.py add_data [user name] [start time] [end time]
```
## help

For Example : 
```bash
python manage.py add_data karthik 0 20
```
Where : [user name] - karthik<br />
[start time] - 0 (in minutes)<br />
[end time] - 20 (in minutes)<br />

The number you enter for start time and end time arguments is considered in minutes.<br />
For Ex: if you enter 10 (therefore 10 minutes) it is considered as current time + 10 minutes<br />
If you enter 0 it is considered as current date and time.
