import cv2 
import pytesseract
import os

try:
    f = open("//home//pi//Desktop//final_year_project//ocr//saved_img.jpg")
    f2 = open("//home//pi//Desktop//final_year_project//ocr//saved_img-final.jpg")
    f3 = open("//home//pi//Desktop//final_year_project//ocr//ocr_text.txt")
    # Do something with the file
    print("file exists")
    os.remove("//home//pi//Desktop//final_year_project//ocr//saved_img.jpg")
    os.remove("//home//pi//Desktop//final_year_project//ocr//saved_img-final.jpg")
    os.remove("//home//pi//Desktop//final_year_project//ocr//ocr_text.txt")
    #os.remove("ocr_voice.mp3")
    
except IOError:
    print("Files no found")
finally:
    print("complete")

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='//home//pi//Desktop//final_year_project//ocr//saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('//home//pi//Desktop//final_year_project//ocr//saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('//home//pi//Desktop//final_year_project//ocr//saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(999,999))
            print("Resized...")
            img_resized = cv2.imwrite(filename='//home//pi//Desktop//final_year_project//ocr//saved_img-final.jpg', img=img_)
            print("Image saved!")
            print("Hello we are printing here")
            text = pytesseract.image_to_string('//home//pi//Desktop//final_year_project//ocr//saved_img.jpg').encode('utf-8').strip()
            print(text)
            text_file = open("//home//pi//Desktop//final_year_project//ocr//ocr_text.txt","w")
            n = text_file.write(text)
            text_file.write("Program complete, complete")
            text_file.close()
            #execfile('he4.py')
        
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()	
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

