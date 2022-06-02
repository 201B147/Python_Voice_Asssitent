from plyer import notification

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10
    )

if __name__ == '__main__':
    notifyMe("Mrinal","Lets stop the spread of this virus together")
