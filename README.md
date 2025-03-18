# tab-for-a-cause-selenium

donate to charity automatically for free using only a bit of processing power

this is done by automatically opening and refreshing a [tab for a cause](https://tab.gladly.io/) page in a browser

## requirements

- tab for a cause account, specifically one that uses the "email address" sign up option, no other types of account will work with this, (it's strongly recommended you DO NOT use your main account if you have one, instead make an alt account on tab for a cause to use for this script if this is the case)

- python 3

- selenium

- firefox

## how to use (windows installation)

in the same directory as this document, make a `credentials.txt` file and put the account's credentials in it like the following

```txt
youremail
yourpassword
```

run (double click) the `shortcutwin.bat` batch script to create the shortcut

run the `tab-for-a-cause-selenium` shortcut, this will open a console window that displays the program's output (this is normal), it will also open a firefox window to load the webpage in, it will attempt to login using the credentials in `credentials.txt`,

you may minimize both of these windows and let the program run in the background

to stop the program, close both the console and browser window it opened