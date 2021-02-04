import sys

s = "2015-11-12-a-wonderful-serenity-has-taken-possession-of-my-entire-soul.md"
s = '2019-6-19-millionaire-fastlane.md'
s=sys.argv[1]

url = "https://www.sandordargo.com/blog/"

pos = 0
ypos = s.find('-')
url+=s[:ypos] + "/"

#print(url, ypos)
mpos = ypos + s[ypos+1:].find('-')
url+=s[ypos+1:mpos+1].zfill(2) + "/"

#print(url, ypos, mpos)
dpos = mpos + s[mpos+2:].find('-')
url+=s[mpos+2:dpos+2].zfill(2) + "/"

#print(url, ypos, mpos, dpos)
url+=s[dpos+3:s.find('.')]

print(url)

