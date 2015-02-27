*This does not work anymore, due to google api v2 shutdown!
New api allows only oauth authentication, which is insanely painful for desktop
application, so I'm not going to rewrite it. It's just easier to copy it manually. Live sucks.*

UsosAPI uses oauth authorization. To allow usos2google to read you schedule,
you need to:

1. Enter site https://usosapps.uw.edu.pl/developers/ or similar for your
   UsosAPI instance.
1. Enter:
    Application Name = USOS2google
    Application's Webpage = https://github.com/mdebski/usos2google
   and your email.
1. Click 'Submit' and copy Consumer key and Consumer secret to
   corresponding variables in usos2google_conf.py file.
1. Run usos2google, enter site you will be asked to and copy PIN from it.
1. To avoid repeating 4. point every time you run usos2google, you may copy
   Access Token Key i Access Token Secret to usos2google_conf.py

Google authorization is performed simply with your password - you will be asked
for it every time.
