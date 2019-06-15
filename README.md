# Field-Glass-Bot
A short python script that automatically fills in fieldglass timesheets.
# Usage
After cloning the project, take a look at the example.env file, here all you need to do is change the values 
to your credentials.
After, simply run "python auto_field_glass.py" and let the script do the rest.
The Script won't actually submit the timesheet for you, this is done intentionally
so that you can make sure everything looks good before submitting yourself.
# Requirements
Only selenium and python-dotenv are required for this project, found in requirements.txt, run pip install -r requirements.txt.
additionally you will also need to install chrome driver, instructions to do so can be found here:
mac: https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/
windows: https://www.kenst.com/2019/02/installing-chromedriver-on-windows/
# Demo
![](demo.gif)
