#!/usr/bin/python
copyright="""
Copyright (c) 2012, Sigasi nv
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. All advertising materials mentioning features or use of this software
   must display the following acknowledgement:
   This product includes software developed by the <organization>.
4. Neither the name of the <organization> nor the
   names of its contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY <COPYRIGHT HOLDER> ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

info = """
Script for running the GHDL simulator on a Sigasi project 

This script is intended as a demonstration of how to write your own scipts that use the Sigasi exported CSV File. 
This script is not part of the supported Sigasi Pro product.  
We appreciate if you share your scripts for other EDA tools on our website: http://www.sigasi.com

In order to use this script:
First export a CSV file list from your Sigasi project: Export > Sigasi > CSV File
Then, run this script. You can adjust the parameters below to your needs

Known limitations:
GHDL requires you to compile all units in a library at the same time. 
If you use more than one library, this script might not work.
"""

# Parameters
csv_file="compilation_order.csv"
ghdldir="/opt/GHDL/bin/"
top="testbench"
toplibrary="work"


import os

f = open(csv_file)
lines = f.readlines()
f.close()
libraries={}
sortedLibraries=[]
for line in lines:
	[library,filename]=line.split(',')
	library = library.strip()
	filename = filename.strip()
	if (not(library in sortedLibraries)):
		sortedLibraries.append(library)
	if not( libraries.has_key(library) ):
		libraries[library] = []
	libraries[library].append( filename)
	
print libraries

ghdl=ghdldir+"ghdl"
for library in sortedLibraries:
	print library
	files = libraries[library]
	os.spawnv(os.P_WAIT,ghdl,[ghdl,"-a","--work="+library,] + files)

	
print "You can start your simulation with:"
print "ghdl -r --workdir=bin/"+toplibrary+" "+top
