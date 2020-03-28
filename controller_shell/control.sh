#!/usr/bash
play /home/pi/Desktop/final_year_project/extravoices/welcome_speech.mp3
while $1
do
sleep 1
echo "Please enter your option"
play /home/pi/Desktop/final_year_project/extravoices/get_option.mp3
read option
case ${option} in
   11) echo "Horoscope option selected"
        play /home/pi/Desktop/final_year_project/extravoices/h_welcome.mp3 &&
	sh /home/pi/Desktop/final_year_project/horoscope/hsh.sh &&
	python3 /home/pi/Desktop/final_year_project/horoscope/hvoice.py && 
	play /home/pi/Desktop/final_year_project/horoscope/h_voice.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;;
   12) echo "play music"
        python3 /home/pi/Desktop/final_year_project/music/m.py &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;;

   13) echo "joke option selected"
        python3 /home/pi/Desktop/final_year_project/jokes/joke.py &&
	python3 /home/pi/Desktop/final_year_project/jokes/joke_gtts.py &&
	play /home/pi/Desktop/final_year_project/jokes/joke_voice.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;;
   0) echo "option 0 choosen : calculator"
	python3 /home/pi/Desktop/final_year_project/calculator/cal.py &&
	python3 /home/pi/Desktop/final_year_project/calculator/cal_gtts.py &&
	play /home/pi/Desktop/final_year_project/calculator/cal_voice.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;;
   1) echo "option 1 choosen : funtion date and time"
	play /home/pi/Desktop/final_year_project/extravoices/option1.mp3
	python3 /home/pi/Desktop/final_year_project/date_and_time/date_time.py &&
	python3 /home/pi/Desktop/final_year_project/date_and_time/date_time_gtts.py &&
	play /home/pi/Desktop/final_year_project/date_and_time/date_time_voice.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;; 
   2) echo "option 2 choosen : function current location"
	play /home/pi/Desktop/final_year_project/extravoices/option2.mp3
	sh /home/pi/Desktop/final_year_project/current_location/current_loc.sh &&
	python3 /home/pi/Desktop/final_year_project/current_location/location_gtts.py &&
	play /home/pi/Desktop/final_year_project/current_location/cur_loc.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;;

   7) echo "option 7 choosen : function current weather"
	play /home/pi/Desktop/final_year_project/extravoices/temperature.mp3
	python3 /home/pi/Desktop/final_year_project/weather/weather_code.py &&
	python3 /home/pi/Desktop/final_year_project/weather/weather_gtts.py &&
	play /home/pi/Desktop/final_year_project/weather/weather_voice.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;;

   3) echo "option 3 choosen : function email reading"
	play /home/pi/Desktop/final_year_project/extravoices/option3.mp3
	python3 /home/pi/Desktop/final_year_project/email/email_code.py &&
	python3 /home/pi/Desktop/final_year_project/email/email_gtts.py &&
	play /home/pi/Desktop/final_year_project/email/email_voice.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;;

   4) echo "option 4 choosen : newsheadlines"
	play /home/pi/Desktop/final_year_project/extravoices/option4.mp3
	python3 /home/pi/Desktop/final_year_project/news_headlines/news.py &&
	python3 /home/pi/Desktop/final_year_project/news_headlines/news_gtts.py &&
	play /home/pi/Desktop/final_year_project/news_headlines/news_voice.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
      ;;

   5) echo "option 5 choosen : ocr"
	play /home/pi/Desktop/final_year_project/extravoices/option5.mp3
	python /home/pi/Desktop/final_year_project/ocr/ocr_img_to_text.py &&
	python3 /home/pi/Desktop/final_year_project/ocr/ocr_gtts.py &&
	play /home/pi/Desktop/final_year_project/ocr/ocr_voice.mp3 &&
	play /home/pi/Desktop/final_year_project/extravoices/program_complete.mp3
	sleep 1.5
	;;

   6) play /home/pi/Desktop/final_year_project/extravoices/help_welcome.mp3
      play /home/pi/Desktop/final_year_project/extravoices/help_info.mp3
      play /home/pi/Desktop/final_year_project/extravoices/help_again.mp3
	sleep 1.5
	;;
   
   
   8) play /home/pi/Desktop/final_year_project/extravoices/color_welcome.mp3
      python /home/pi/Desktop/final_year_project/color/capture_image.py
      play /home/pi/Desktop/final_year_project/extravoices/color2.mp3
      python3 /home/pi/Desktop/final_year_project/color/color_detect.py
      python3 /home/pi/Desktop/final_year_project/color/color_gtts.py
      play /home/pi/Desktop/final_year_project/color/color_voice.mp3
	sleep 1.5
	;;

   9) echo "Program complete"
	play /home/pi/Desktop/final_year_project/extravoices/exit.mp3
	exit 1
	;;

   *)  echo "improper button please choosen again" 
	play /home/pi/Desktop/final_year_project/extravoices/improper_button.mp3
	sleep 1.5
      ;; 
esac 
done