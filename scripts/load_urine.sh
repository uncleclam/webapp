#!/bin/sh

 curl -L --get https://api.serpwow.com/search \
    -d api_key="6521809044384F6486918BFCB59AF83D" \
    -d q="urination" \
    -d engine="google" \
    -d google_domain="google.com" \
    -d page="1" \
    -d num="10" \
        -o urination.json 

#PARSE JSON AND EXPORT CSV
python python/piss.py

#LOAD CSV TO MYSQL
./mysql_load.sh

#DELETE TEMP FILES
#sudo rm urination.json
#sudo rm urine.csv

#file_name=piss
#current_time=$(date "+%Y-%m-%d_%H:%M:%S")
#new_fileName=$file_name-$current_time
#today_date=$(date "+%Y-%m-%d")


#cp $file_name $new_fileName.json 

#aws s3 cp $new_fileName.json s3://uncleclam-webapp/$today_date/ 

#sudo rm piss
