import pywhatkit as kit
phone_number = "+254748473493"
message ="Hello Counsel Andrew, this message is sent to you from Python code, A Python code project testing process"
kit.sendwhatmsg_instantly(phone_number, message)
print("Message sent successfully!")