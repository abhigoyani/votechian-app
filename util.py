from Crypto.PublicKey import RSA
import binascii
import random
import requests
import os

def verfiyKey(key: str):
    try:
        if len(key) < 750:
            return False
        RSA.importKey(binascii.unhexlify(key))
        # .publickey().exportKey('PEM')
        return True
    except:
        return False


# function for otp generation
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(random.randint(1,9))
    return otp


def SendOtp(mail):
    otp=otpgen()
    requests.post(
        "https://api.eu.mailgun.net/v3/votechain.biz/messages",
        auth=("api", os.environ.get('mailGunAPI')),
        data={"from": "VoteChain verification <otp@votechain.biz>",
              "to": [mail],
              "subject": "Account verification | VoteChain",
              "template": "votechain",
              "v:otp":otp})
    return otp


print(os.environ.get('mailGunAPI'))