


  


Setup Database  
  SetUp your database User,Password, Host  just basically change values in .env files to your own...Then delete everything inside the migrations folder which is inside the instagram folder

  then run python .env 

  Then run


python manage.py makemigrations instagram
   
   i used the name instagram because my database name is instagram
 
 python manage.py migrate 

 Run the application  
 
 python manage.py runserver 

