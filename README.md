sigasi-csv-build
================

Compile VHDL projects from the CSV list of files, exported by Sigasi Pro.


Now that Sigasi (as off version 2.8) can export a list of the VHDL files in a project, you can write your own scripts for virtually any EDA tool; compilers, linters or synthesis tools. 

Download Sigasi at http://www.sigasi.com 
There is a free Starter Edition or you can request a one month evaluation license for the Sigasi Pro version.

This project contains a short python script that reads the file list that comes from Sigasi and compiles your project using GHDL. To use this script, you first need to export the CSV file list: right-click on your project and select Export > Sigasi > CSV File. Now put the python script in the project directory and run it. You can change the parameters in the python script if you like.

This script might not suit your exact needs, but it should be a good starting point. If you create your own script for a different EDA tool, it would be great if you can share this script with us. 

Feel free to fork, share and submit pull requests.