#!/usr/bash
rm /home/pi/Desktop/final_year_project/horoscope/h.txt
curl -X POST 'https://aztro.sameerkumar.website/?sign=aries&day=today' >> /home/pi/Desktop/final_year_project/horoscope/h.txt
echo "Program complete" >> /home/pi/Desktop/final_year_project/horoscope/h.txt