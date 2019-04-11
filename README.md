# Field-Glass-Bot
A short python script that automatically fills in fieldglass timesheets.
# Usage
After cloning the project, enter your username and password in credentials.py
Alternatively and what is actually better practice is to export your username and password as variables  
in your bash profile, then the script can access them using os.environ, you will need to uncomment two lines in the to fix this
After, simply run "python auto_field_glass.py" and let the script do the rest.
The Script won't actually submit the timesheet for you, this is done intentionally
so that you can make sure everything looks good before submitting yourself.

# Usage with Cron Jobs
If you don't know what Cron Jobs are here is a great video: https://www.youtube.com/watch?v=QEdHAwHfGPc  
You can set up your system's crontab such that this script is executed automatically on a weekly basis,
for example every Friday at 6pm. This way you don't have to run the script explicilty yourself!
An example crontab file is included in the root directory of this repo for reference.
# Requirements
Only selenium is required for this project, found in requirements.txt, run pip install -r requirements.txt or just pip install selenium.
additionally you will also need to install chrome driver, instructions to so can be found here:
mac: https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/
windows: https://www.kenst.com/2019/02/installing-chromedriver-on-windows/
# Demo
![](demo.gif)
