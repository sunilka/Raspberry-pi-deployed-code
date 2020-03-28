#!/usr/bash
rm /home/pi/Desktop/final_year_project/current_location/location.txt

printf "current city is : " >> /home/pi/Desktop/final_year_project/current_location/location.txt
curl ipinfo.io/city >> /home/pi/Desktop/final_year_project/current_location/location.txt
printf "\n"

printf "current region is : " >> /home/pi/Desktop/final_year_project/current_location/location.txt
curl ipinfo.io/region >> /home/pi/Desktop/final_year_project/current_location/location.txt
printf "\n"

printf "Current country is : " >> /home/pi/Desktop/final_year_project/current_location/location.txt
curl ipinfo.io/country >> /home/pi/Desktop/final_year_project/current_location/location.txt
printf "\n"

echo "Program complete ,done" >> /home/pi/Desktop/final_year_project/current_location/location.txt