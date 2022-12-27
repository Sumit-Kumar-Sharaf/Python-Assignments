""" Write a python script to create a Phone class with 2 methods to 
print the features (calling and sms) """

class Phone:
    def calling(self):
        print("This Phone Supports Voice Calling And Video Calling Features")
    def sms(self):
        print("This Phone Support SMS And MMS Features")

nokia6600=Phone()
nokia6600.calling()
nokia6600.sms()