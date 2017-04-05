'''
comments here
'''

import os
import argparse

import random
pid=str(os.getpid()+random.randint(0,999999999))

def parse_cli_options():
  parser = argparse.ArgumentParser(description='Read reditools data tables', formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument( '-i', dest='result', help='')
  parser.add_argument( '-r', dest='rna_in', help='')
  parser.add_argument( '-d', dest='dna_in', help='')
  parser.add_argument( '-m', dest='html', help='')
  parser.add_argument( '-o', dest='outdir', help='')
  parser.add_argument( '-s', dest='sample_id', help='')
  parser.add_argument( '-g', dest='group_id', help='')
  parser.add_argument( '-t', '--init_html', dest='init_html', action='store_true', help='')
  parser.add_argument( '-c', '--close_html', dest='close_html', action='store_true', help='')
 
  return parser.parse_args()

def init_html_file(fout):
  '''
  Create html file
  '''
  f = file(fout,'w')
  html = []

  # Start html code
  html.append('<html><body><table border=1>')
  html.append('<tr><td>')
  html.append('RNA BAM file</td><td>DNA BAM file</td><td>ID sample</td><td>ID group</td><td>ID output')
  html.append('</td></tr>')

  f.write('\n'.join(html))
  f.write('\n')
  f.close()
  return f

def close_html_file(fout):
  '''
  Create html file
  '''
  f = file(fout,'a')
  html = []

  # Close html code
  html.append('<p>')
  html.append('</table></body></html>')

  f.write('\n'.join(html))
  f.write('\n')
  f.close()
  return f

def create_out_dir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)

def create_output_symlink(source, linkname):
  os.symlink(source, linkname)

def update_html(rna_in, dna_in, sid, gid, fout):
  '''
  Update output html file
  '''
  html = []
  html.append('<tr><td>')
  html.append('%s</td><td>%s</td><td>%s</td><td>%s</td><td><a href="%s">%s</a>' % (rna_in, dna_in, sid, gid, fout+'.txt', fout) )
  html.append('</td></tr>')
  return html

#def create_tab_list_file():

def set_sample_id(sid, n):
  if not sid:
    return n
  else:
    return sid

def set_group_id(gid, n):
  if not gid:
    return n
  else:
    return gid

def main():
  options = parse_cli_options()

  if(options.init_html):
    init_html_file(options.html)
    return

  if(options.close_html):
    close_html_file(options.html)
    return

  create_out_dir(options.outdir)

  filename = 'outTable_' + pid
  filepath = str(options.outdir) + '/' + filename + '.txt'

  create_output_symlink(options.result, filepath)

  sample_id = set_sample_id(options.sample_id, pid)
  group_id = set_group_id(options.group_id, 'example')

  fhtml = update_html(options.rna_in, options.dna_in, sample_id, group_id, filename)
  fin = file(options.html,'a')
  fin.write('\n'.join(fhtml))
  fin.write('\n')
  fin.close()

if __name__=="__main__":
  main()
