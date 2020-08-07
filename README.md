# User and Activity Period details
This is the Django application with User and Activity Period details saved in the Database and can serve that data using API in JSON format.
We can populate data in the database using a custom management command.<br />

The data saved in database is served using JSON format, For demo the code is deployed in pythonanywhere.
Please click [here](https://dorai9845.pythonanywhere.com/) to view.

## Usage

Command to populate data in database

```bash
python manage.py add_data [user name] [start time] [end time]
```
## Help

For Example : 
```bash
python manage.py add_data karthik 0 20
```
Where : <br />
[user name] - karthik<br />
[start time] - 0 <br />
[end time] - 20 <br />

The number you enter for start time and end time argument is considered in minutes.<br />
For Ex : if you enter 10 (therefore 10 minutes) it is considered as current time + 10 minutes<br />
If you enter 0 it is considered as current date and time.
