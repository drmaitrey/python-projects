import datetime
from plyer import notification


def tell1():
    hour = (datetime.datetime.now().hour)
    if hour == 13:
        notification.notify(
            title = "Trial Title 1",
            message = "It is just a trial~~~~!!!!!!!!"
        )

def tell2():
    hour = (datetime.datetime.now().hour)
    if hour == 13:
        notification.notify(
            title = "Trial Title 2",
            message = "It is second trial message ~~~~~~~~~~~~!!!!!!!!!"

        )

def tell3():
    hour = (datetime.datetime.now().hour)
    if hour == 13:
        notification.notify(
            title = "Trial Title 3",
            message = "It is third trial message ~~~~~~~~~~~~~~!!!!!!!!!!"
        )


if __name__ == '__main__':
    tell1()
if __name__ == '__main__':
    tell2()
if __name__ == '__main__':
    tell3()