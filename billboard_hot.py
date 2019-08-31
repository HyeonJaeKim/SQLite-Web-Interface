#!/usr/bin/python3
import cgi
import sqlite3
import cgitb

cgitb.enable()

print ('Content-Type: text/html\r\n\r\n')
print ( '<html>\n<head>')
print ( '<title>sqlite selection</title>')
print ( '''<link href='asg5_shk594_style.css' rel='stylesheet' type='text/css' />''')
print(' </head>')
print ( '<body>')

form = cgi.FieldStorage()

if 'display' in form:  # checking for a non-empty field
    display = form['display'].value
    print ( 'Displaying selected records.</h4>')
else:
    display = ''
    print ( 'Displaying all records.</h4>')
print ( '<hr />')

sort = form['sort'].value
order = form['order'].value
year = form['year'].value
limit = form['limit'].value

conn = sqlite3.connect('billboard_hot.db')
c = conn.cursor()

if display != 'Select':
    query = 'SELECT Song, Performer, Peak_Position, Week_Position, Weeks_On_Chart, WeekID FROM billboard_hot ORDER BY Song, Performer'
elif display == 'Select':
    query = 'SELECT Song, Performer, Peak_Position, Week_Position, Weeks_On_Chart, WeekID FROM billboard_hot WHERE WeekID LIKE "%' + year + '%" ORDER BY ' + order + ' ' + sort + ' LIMIT ' + limit

print('<p><em>Query:  </em>' + query + '</p>')
c.execute(query)

print ('<table >')

# first print a headings row
print ('<tr>')
print ('<td>Song</td>')
print ('<td>Performer</td>')
print ('<td>Peak_Position</td>')
print ('<td>Week_Position</td>')
print ('<td>Weeks_On_Chart</td>')
print ('<td>WeekID</td>')
print ('</tr>')

# now print the data
for Song, Performer, Peak_Position, Week_Position, Weeks_On_Chart, WeekID in c:
    print ('<tr>')
    print ('<td>' + Song + '</td>')
    print ('<td>' + Performer + '</td>')
    print ('<td>' + str(Peak_Position) + '</td>')
    print ('<td>' + str(Week_Position) + '</td>')
    print ('<td>' + str(Weeks_On_Chart) + '</td>')
    print ('<td>'+ WeekID +'</td>')
    print ('</tr>')

print ('</table>')

# close the cursor
c.close()

print('</body>')
print('</html>')
