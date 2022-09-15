import random
import os
def emails():
	email_mak = "qwertyuiopasdfghjklzxcvbnm"
	num_email = "1234567890"
	nmail = email_mak + num_email
	while True :
		#gmail
		choice_emile ="".join(random.choice(nmail)for i in range(6,20))
		gmail = choice_emile+"@gmail.com\n"
		with open("gmail.txt","a+") as gm : 
			gm.write(gmail)
			gm.close()
			
			#yahoo
		yahoo = choice_emile+"@yahoo.com\n"
		with open("yahoo.com.txt","a+") as y:
			y.write(yahoo)
			y.close()
			#hotmail
		hotmail = choice_emile+"@hotmail.com\n"
		with open("hotmail.com.txt","a+") as hotm :
			hotm.write(hotmail)
			hotm.close()
			#autlook.com
		outlook = choice_emile+"@autlook.com\n"
		with open("autlook.com.txt","a+") as outl :
			outl.write(outlook)
			outl.close()
			# autlook.sa
		autlooksa = choice_emile+"@autlook.sa\n"
		with open("autlook.sa.txt","a+") as sa :
			sa.write(autlooksa)
			sa.close()
			
emails()