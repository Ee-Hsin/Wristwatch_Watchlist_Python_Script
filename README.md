Purpose:
This script scrapes prices from https://watchcharts.com/ for the models you select and will send an email to notify you when there is a listing in your budget.

STEPS to use:

Fill up the form at the beginning of the script with your User Info and the watches you are looking for and at given price points (prices are in SGD by default)
The gmail App password is not your gmail password, but is the app Password Google generates for you for a specific app.

The script has a frequencyOfChecks variable that you can set, the default is 1, meaning it will run every 24 hrs. 
I recommend running it on a cloud. If you are going to run it with a task scheduler, set the frequencyOfChecks to 0 as you
will not need it. 
