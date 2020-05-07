def getFriends():
    return ['Kevin', 'Diana', 'Jesse', 'Lisa', 'Daniel']


def sendInvitations(list):
    for friend in list:
        string = (
            f"Dear {friend}, \n"
            f"I am having a farewell party on May 21st \n"
            f"at my place. My address is 135 Italy Street, \n"
            f"San Francisco, CA 94112. Please let me know if \n"
            f"you can make it. \n"
            f" \n"
            f"Dahyun \n"
            f"\n"
        )
        print(string)


def main():
    friends = getFriends()
    sendInvitations(friends)


main()
