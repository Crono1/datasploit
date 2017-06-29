#!/usr/bin/env python

import base
import config as cfg
import sys
import requests
import json
from termcolor import colored

# Control whether the module is enabled or not
ENABLED = True


class style:
    BOLD = '\033[1m'
    END = '\033[0m'


def banner():
    print colored(style.BOLD + '\n---> Searching Clearbit\n' + style.END, 'blue')


def main(email):
    headers = {"Authorization": "Bearer %s" % cfg.clearbit_apikey}
    req = requests.get("https://person.clearbit.com/v1/people/email/%s" % (email), headers=headers)
    person_details = json.loads(req.content)
    if "error" in req.content and "queued" in req.content:
        print "This might take some more time, Please run this script again, after 5 minutes."
    else:
        return person_details


def output(data, email=""):
    for x in data.keys():
        print '%s details:' % x
        if type(data[x]) == dict:
            for y in data[x].keys():
                if data[x][y] is not None:
                    print "%s:  %s, " % (y, data[x][y])
        elif data[x] is not None:
            print "\n%s:  %s" % (x, data[x])

    print "\n-----------------------------\n"


if __name__ == "__main__":
    try:
        email = sys.argv[1]
        banner()
        result = main(email)
        output(result, email)
    except Exception as e:
        print e
        print "Please provide an email as argument"
