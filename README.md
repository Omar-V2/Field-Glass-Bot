# Field-Glass-Bot
A short python script that automatically fills in fieldglass timesheets.
# Usage
After cloning the project, the recommended way to enter your username and password is to 
store them as environment variables in your bash_profile and then update the envar.py file 
with the names of these variables. Alternatively, but not recommended you can simply enter 
your username and password in the credentials.py file.
After, simply run "python auto_field_glass.py" and let the script do the rest.
The Script won't actually submit the timesheet for you, this is done intentionally
so that you can make sure everything looks good before submitting yourself.
# Requirements
Only selenium is required for this project, found in requirements.txt, run pip install -r requirements.txt or just pip install selenium.
additionally you will also need to install chrome driver, instructions to do so can be found here:
mac: https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/
windows: https://www.kenst.com/2019/02/installing-chromedriver-on-windows/
# Demo
![](demo.gif)
