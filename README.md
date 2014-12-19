Mailer
========
You can use mailer to send customized versions of an email to a list of recipients. 
You simply need to have a body.txt template file, a data.csv containing the customizations (you can make it in Excel and then generate a csv),and then enter your gmail login data into the script itself. 

Check out the input format as specified in the example, and try it out!


Example body.txt
------------------------------------------------------------------------------
Dear /#1#/,

Thanks you for coming to my shindig last night. It was so great to have you here.
Also, thank you so much for the /#2#/. I really enjoyed /#3#/.

Have a good day!

Best,
Adi


Example corresponding data.csv
------------------------------------------------------------------------------
tom@gmail.com, 		Thomas,		brownies,			eating them
dick@yahoo.com,		Richard,	vinyl records,		listening to them
harry@hotmail.com,	Harry,		shirt,				folding it		
