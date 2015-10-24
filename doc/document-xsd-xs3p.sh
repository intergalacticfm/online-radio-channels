# This script will generate documentation on XSD files in HTML files.

# Note: the result must be viewed locally by a web browser and not in GitHub!

# In order to run this script, create a directory named xs3d in the parent
# directory here. That is, the root directory of this git repository. Download
# from http://sourceforge.net/projects/xs3p/?source=typ_redirect the file
# xs3p-1.1.5.zip and unpack it in the xs3d directory. Note that git will not
# monitor that directory as it is in the .gitignore file.

# If needed, do also $ apt-get install xsltproc

for i in ../*xsd
do
    echo $i
    if [ $i -nt `basename $i .xsd`-xs3p.html ]
    then
        echo Generating HTML...
        xsltproc -o `basename $i .xsd`-xs3p.html ../xs3p/xs3p.xsl $i
    else
        echo HTML is up to date
    fi
done
