import requests
import os
from bs4 import BeautifulSoup

print "<<<GitHub Bug Tracking Script - Copyright Sumith 2015>>> \n"
print "Make sure you enter the details in correct case-sensitivity \n"

org = raw_input("Enter the user/org holding the repo: ")
repo = raw_input("Enter the repo name: ")
label = raw_input("Label name of bugs you want to track: ")

siteURL = "https://github.com/"
extenURL = org + '/' + repo + '/labels/' + label
pageURL = siteURL + extenURL

HTTPSession = requests.session()
page = HTTPSession.get(pageURL)
soupmain = BeautifulSoup(page.content)

issues = soupmain.find_all("span", class_ = "issue-meta-section opened-by" )
issue_new = issues[0].text.split()

number = issue_new[0]
date = issue_new[2]+" "+issue_new[3]+" "+issue_new[4]
reporter = "@" + issue_new[6]

print "Most recent issue with your specification:"
print number
print "Reported on " + date
print "Reported by " + reporter

print "All issues in this section: \n"
for issue in issues:
	issu = issue.text.split()
	no = issu[0]
	print no
print ""

data = open("bugtracker.txt", "rb+")

found = False

lines = data.readlines()
data.seek(0)
data.truncate()

for line in lines:
	if extenURL in line:
		found = True
		issue_details = line.split()
		if number == issue_details[-1]:
			print "You have already been notified about this previously \n"
		else:
			print "New bugs have been reported, do check \n"
			print line
			line = line.replace(issue_details[-1], number)
			print line
	data.write(line)

if not found:
	print "Thanks for tracking new bugs, execute later to find out if new bugs have been reported"
	data.write(extenURL+ " : "+number + "\n")
	data.close()

print "Thanks for using this, keep using :)"

#Copyright Sumith
