# this is a script to get the tags from the tamaulipas pages.

from bs4 import BeautifulSoup
import urllib

# global variables
url="http://www.tamaulipas.gob.mx/prensa/page/"
tag="a"
attrs={'rel':'category tag'}
result= list()
# gets a tag from an html 
def get_tags(url, tags, attributes):
    # get the url 
    html = urllib.urlopen(url).read()
# parse in soup
    soup = BeautifulSoup(html, 'html.parser')
    temp_tags=soup.find_all(tags, attrs=attributes)
    
    for tag in temp_tags:
        result.append(tag.text)
    
def remove_duplicates(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

get_tags("http://www.tamaulipas.gob.mx/prensa", tag, attrs)

# main 
for i in range(1, 23):
    finalUrl=url+str(i)
    get_tags(finalUrl, tag, attrs)

# the result is saved in the result variables
# then we need to remove the duplicates
finalResults=remove_duplicates(result)

# and print the final result to the screen
for category in finalResults:
    print category
    