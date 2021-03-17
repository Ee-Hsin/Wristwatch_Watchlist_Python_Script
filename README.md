<b>Purpose</b>:

This script scrapes prices from https://watchcharts.com/ for your desired models and will send an email to notify you when there is a listing in your budget range.

<b>STEPS to use:</b>

Fill up the form at the beginning of the script with your User Info and the watches you are looking for at the given price points (prices are in Singapore Dollar by default).
![image](https://user-images.githubusercontent.com/75463789/111506274-6f705e00-8784-11eb-82b8-27553dfd1704.png)
The gmail App password is not your gmail password, but is the app Password Google generates for you for a specific app.
The script has a frequencyOfChecks variable that you can set, the default is 1, meaning it will run every 24 hrs. 
It is recommend to run this on the cloud. If you are going to run it with a task scheduler, set the frequencyOfChecks to 0 as you
will not need it, your task scheduler will handle when it runs.
