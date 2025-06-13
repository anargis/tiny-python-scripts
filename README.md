# Tiny Python Scripts

A collection of minimal Python scripts — each under ~100 lines — built to solve everyday tasks with simplicity and elegance.
___

1. [break-time](https://github.com/anargis/tiny-python-scripts/blob/main/break-time.py)
**Take breaks on time — automatically.**  
Schedule breaks by setting start and end times. This script opens a web browser notification or URL to remind you.  
**Modules used:** `time`, `subprocess`, `webbrowser`

2. [convert-video-to-images](https://github.com/anargis/tiny-python-scripts/blob/main/convert-video-to-images.py)
**Extract every frame from a video.**  
Convert a video file into a sequence of images, frame-by-frame.  
**Modules used:** `os`, `cv2 (OpenCV)`

3. [send-email-via-sendgrid](https://github.com/anargis/tiny-python-scripts/blob/main/send-email-via-sendgrid.py)
**Send emails effortlessly with SendGrid.**  
A simple way to send emails using the SendGrid API. Just provide your API key, Validated Sender and Recipient.  
**Module used:** `sendgrid`

4. [system-info](https://github.com/anargis/tiny-python-scripts/blob/main/system-info.py)
**Get a snapshot of your system hardware and OS.**  
Displays platform, memory usage, and disk space stats — handy for quick diagnostics.  
**Modules used:** `platform`, `psutil`

5. [tutanota-empty-spam-folder, tutanota_credentials](https://github.com/anargis/tiny-python-scripts/blob/main/tutanota-empty-spam-folder.py)
**Automatically clean your Tutanota spam folder.**  
Uses Playwright to log in and empty the spam folder from your Tutanota email account.  
Includes helper file: `tutanota_credentials.py`  
**Module used:** `playwright`

6. [vscode-change-color-theme](https://github.com/anargis/tiny-python-scripts/blob/main/vscode-change-color-theme.py)
**Toggle VS Code between light and dark themes.**  
Switch your VS Code color theme from light to dark (and vice versa) with a simple script.  
Want full system theme switching? Check out [gnome-theme-switcher](https://github.com/anargis/gnome-theme-switcher)  
**Modules used:** `time`, `pynput`

7. [scan-cms](https://github.com/anargis/tiny-python-scripts/blob/main/scan-cms.py)
**Detect popular CMS platforms on any website.**
Identify if a website is running one of the major CMS platforms—WordPress, Joomla, or Moodle  
**Modules used:** `requests`

## Notes

- These scripts are meant to be simple, clean, and easy to extend.
- Great for automation, quick tasks, or as learning resources.
- Feel free to fork, adapt, and contribute!
