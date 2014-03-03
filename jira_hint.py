#!/usr/bin/python

from jira.client import JIRA

# By default, the client will connect to a JIRA instance started from the
# Atlassian Plugin SDK
# (see
# https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK
# for details).
# Override this with the options parameter.
options = {
        'server': 'https://jira.atlassian.com'
}
jira = JIRA(options)

#jira = JIRA(basic_auth=('', ''))

# Get all projects viewable by anonymous users.
projects = jira.projects()
print "projects =>", projects

# Sort available project keys, then return the third, fourth and fifth keys.
keys = sorted([project.key for project in projects])[2:5]
print "keys =>", keys

# Get an issue.
issue = jira.issue('JRA-1330')
print "issue =>", issue
