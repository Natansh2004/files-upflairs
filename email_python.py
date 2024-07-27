import smtplib                                  #importing smtplib module

fp=open("C:/matrix/credentials.txt","r")        #opening a file using read mode
                               
s=smtplib.SMTP('smtp.gmail.com',587)            #creates SMTP session
s.starttls()                                    #start TLS for security

s.login("minanatansh@gmail.com","ghutthvbldteifcd")    #authentication
#s.login("sender_email_id", "sender_email_id_password / app_password")

# message to be sent (in our case we've read our data/msg from file)
data=fp.read()

# sending the mail
s.sendmail("minanatansh@gmail.com","ranjit.upflairs@gmail.com",data)
#s.sendmail("sender_email_id", "receiver_email_id", message)

s.quit()                                         #terminating the session

#Closing the file
fp.close()
