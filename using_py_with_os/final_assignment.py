#!/usr/bin/env python3

import re
import subprocess
import csv
import operator

per_user = {}
per_user2 = {}
error = {}
with open("syslog.log") as fd:
    for line in fd:
        if "ERROR" in line:
            temp = line.split("ERROR")[-1].split('(')[0].strip()
            if temp not in error:
                error[temp] = 1
            else:
                error[temp] += 1

with open("syslog.log") as fd:
    for line in fd:
        if "INFO" in line:
            temp = line.split('(')[-1].split(')')[0]
            if temp not in per_user:
                per_user[temp] = 1
            else:
                per_user[temp] += 1
        if "ERROR" in line:
            temp = line.split('(')[-1].split(')')[0]
            if temp not in per_user2:
                per_user2[temp] = 1
            else:
                per_user2[temp] += 1

with open("error_message.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Error", "Count"])
    for key, value in sorted(error.items(), key=operator.itemgetter(1), reverse=True):
        writer.writerow([key, value])

with open("user_statistics.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for key in sorted(per_user):
        writer.writerow([key, per_user[key], per_user2[key]])
