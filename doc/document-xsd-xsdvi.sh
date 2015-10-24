# This script will generate documentation on XSD files in SVG files.

# Note: the result must be viewed locally by a web browser and not in GitHub!

# In order to run this script, create a directory named xsdvi in the parent
# directory here. That is, the root directory of this git repository. Download
# from http://sourceforge.net/projects/xsdvi/?source=typ_redirect the file
# xsdvi.zip and unpack it in the xs3d directory. Note that git will not
# monitor that directory as it is in the .gitignore file.

# If needed, do also $ apt-get install openjdk-8-jre

for i in ../*xsd
do
    echo $i
    if [ $i -nt `basename $i .xsd`-xsdvi.svg ]
    then
        echo Generating SVG...
        java -jar ../xsdvi/dist/lib/xsdvi.jar $i
        mv -f `basename $i xsd`svg `basename $i .xsd`-xsdvi.svg
    else
        echo SVG is up to date
    fi
done
rm -f xsdvi.log
