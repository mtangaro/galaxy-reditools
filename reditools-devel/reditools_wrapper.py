#!/usr/bin/env python

#######################################
#
# REDItools wrapper - v0.00
# ma.tangaro@gmail.com
#
#######################################


"""
Runs REDItoolDnaRna

USAGE: python REDItoolDnaRNA.py [options]
Options:
-i              RNA-Seq BAM file
-j              DNA-Seq BAM file(s separated by comma) or folder
-I              Sort input RNA-Seq BAM file
-J              Sort input DNA-Seq BAM file
-f              Reference in fasta file
-C              Base interval to explore [100000]
-k              List of chromosomes to skip separated by comma or file
-t              Number of threads [1]
-Y              Work Only On Region: chrxx:start-end (positions are distributed by the number of threads)
-o              Output folder [rediFolder_%s]
-F              Internal folder name [null]
-M              Save a list of columns with quality scores
-c              Min. read coverage (dna,rna) [10,10]
-Q              Fastq offset value (dna,rna) [33,33]
-q              Min. quality score (dna,rna) [25,25]
-m              Min. mapping quality score (dna,rna) [25,25]
-O              Min. homoplymeric length (dna,rna) [5,5]
-s              Infer strand (for strand oriented reads) [1]
-g              Strand inference type 1:maxValue 2:useConfidence [1]
-x              Strand confidence [0.70]
-S              Strand correction
-G              Infer strand by GFF annotation (must be GFF and sorted, otherwise use -X)
-K              GFF File with positions to exclude (must be GFF and sorted, otherwise use -X)
-T              Work only on given GFF positions (must be GFF and sorted, otherwise use -X)
-X              Sort annotation files
-e              Exclude multi hits in RNA-Seq
-E              Exclude multi hits in DNA-Seq
-d              Exclude duplicates in RNA-Seq
-D              Exclude duplicates in DNA-Seq
-p              Use paired concardant reads only in RNA-Seq
-P              Use paired concardant reads only in DNA-Seq
-u              Consider mapping quality in RNA-Seq
-U              Consider mapping quality in DNA-Seq
-a              Trim x bases up and y bases down per read [0-0] in RNA-Seq
-A              Trim x bases up and y bases down per read [0-0] in DNA-Seq
-b              Blat folder for correction in RNA-Seq
-B              Blat folder for correction in DNA-Seq
-l              Remove substitutions in homopolymeric regions in RNA-Seq
-L              Remove substitutions in homopolymeric regions in DNA-Seq
-v              Min. num. of reads supporting the variation [3] for RNA-Seq
-n              Min. editing frequency [0.1] for RNA-Seq
-N              Min. variation frequency [0.1] for DNA-Seq
-z              Exclude positions with multiple changes in RNA-Seq
-Z              Exclude positions with multiple changes in DNA-Seq
-W              Select RNA-Seq positions with defined changes (separated by comma ex: AG,TC) [default all]
-R              Exclude invariant RNA-Seq positions
-V              Exclude sites not supported by DNA-Seq
-w              File containing splice sites annotations
-r              Num. of bases near splice sites to explore [4]
--gzip  Gzip output files
-h              Print this help
--help
--reads Get reads containing nuc. changes
--fastq Fastq to get reads [requires --reads], separated by comma [if paired]
--addP  Add positions for reads
"""

# import modules
import optparse, os, shutil, subprocess, sys, tempfile
#try: import pysam
#except: sys.exit('Pysam module not found.')

version='0.1'


##____________________________________
# check if string is integer

def check_int(s):
   if s.isdigit(): 
     return True
   else:
     return False

##____________________________________

def __main__():
   # parse REDItoolDnaRna command line options
   parser = optparse.OptionParser()
   parser.add_option( '-i', dest='input_rna_seq', help='RNA-Seq BAM file' )
   parser.add_option( '-j', dest='input_dna_seq', help='DNA-Seq BAM file' )
   parser.add_option( '-I', action='store_true', dest='sort_rna_seq', help='Sort input RNA-Seq BAM file' )
   parser.add_option( '-J', action='store_true', dest='sort_dna_seq', help='Sort input DNA-Seq BAM file' )
   parser.add_option( '-f', dest='reference', help='Reference in fasta file' )
   parser.add_option( '-o', dest='outfolder', help='Output folder [rediFolder_%s]' )
   parser.add_option( '-t', dest='threads', help='Number of threads [1]' )
   # wrapper options
   parser.add_option( '-1', dest='output1', help='Wrapper output file' )
   (options, args) = parser.parse_args()

   command = 'REDItoolDnaRna.py -i %s -f %s -t %s' % ( options.input_rna_seq, options.reference, options.threads )

   if options.input_dna_seq is not None:
     command += ' -j %s' % ( options.input_dna_seq )

   if options.sort_rna_seq == True:
     command += ' -I'

   if options.sort_dna_seq == True:
     command += ' -J'

   proc = subprocess.Popen( args=command, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE )

   communicateRes = proc.communicate() 
   stdOutValue, stdErrValue = communicateRes

   # split command, here is by space
   my_output_list = stdErrValue.split( )
   
   output_random_index = my_output_list[8]
 
   # Check if random number is integer
   if check_int(output_random_index)==False:
      sys.exit(2)

   # Check job folder consistency
   fname = 'rediFolder_%s/DnaRna_%s/outTable_%s' % ( output_random_index, output_random_index, output_random_index )
   if os.path.isfile(fname) == False:
     sys.exit(3)

   mvoutput = 'cat rediFolder_%s/DnaRna_%s/outTable_%s > %s' % ( output_random_index, output_random_index, output_random_index, options.output1 )
   os.system( mvoutput ) 
   
   print 'Job command: %s' % ( command )
   print 'Number of threads: %s' % ( options.threads )
   print 'Job pid: %s' % ( output_random_index )
   print stdErrValue

##____________________________________
 
if __name__ == "__main__":
    __main__()
