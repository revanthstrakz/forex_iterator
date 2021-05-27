
#
#  Copyrights reserved by Revanth
#

cd output
for j in *
do 
    cd $j
    for i in *
    do 
        unzip $i
    done
    cd ..
done
