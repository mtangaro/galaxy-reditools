#RESULTS=$1
#BASEPATH= $2
#
#echo "<html><body><table border=1>"
#echo '<a href=${RESULTS}>ciao</>'
#echo "$RESULTS" | sed -r "s|$BASEPATH(.*)|<a href=\"\\1\">\\1</a>|" | sed '
#i<tr><td>
#s|\t|</td><td>|g
#a<\/td><\/tr>
#'
#echo "<p>"
#echo "</table></body></html>"



'''
comments here
'''

import os
import argparse


def parse_cli_options():
  parser = argparse.ArgumentParser(description='Read reditools data tables', formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument( '-i', dest='result', help='')
  parser.add_argument( '-p', dest='path', help='')
  parser.add_argument( '-o', dest='output directory', help='')
  parser.add_argument( '-s', dest='sample id', help='')
  parser.add_argument( '-g', dest='group id', help='')
  
  return parser.parse_args()



def create_html():
  '''
  Create html file
  '''
  html = []
  html.append('<html><body><table border=1>')
  return html


#def create_tab_list_file():

def main():
  print 'ciao';
  fhtml = create_html
  print fhtml
  fin = file('index.html','w')
  fin.write('\n'.join(fhtml))
  #fin.write('\n')
  fin.close()

if __name__=="__main__":
  main()
