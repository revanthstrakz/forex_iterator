
#
#  Copyrights reserved by Revanth
#

cd output
for j in *
do 
    cd $j
    mv *.csv ../data/
    cd ..
done
