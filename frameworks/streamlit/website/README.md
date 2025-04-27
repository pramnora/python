**CREATED**: *Sun 27 April 2025 19:09 PM GMT*  
**UPDATED**: *Sun 27 April 2025 19:09 PM GMT*  

-----

# Creating web sites using Streamlit...  
## Concerning web site structure/and, also, specific page order/numbering    

In order to create a web site using Streamlit...;  
one has to pay careful attention how to structure your site/  
and, also, how to call/number each page:      

There should be a file called:    

> main.py  

...and, there should be a directory folder called:  

> pages  

...inside of the pages folder that's where pages are stored.  
Each page is numbered at the start...  

> 1_anyPageName.py  
> 2_anyPageName.py  
> 3_anyPageName.py  

...and, the pages will be displayed with a menu that shows that specific order of page arrangment.  

-----

In order to run the site...you type in at your browsers terminal window command:  

> streamlit run main.py  

...you will get instruction of which browser URL to type in to view your web page...  

> http://localhost:5001  

...you go over to your web browser; and, type in that URL in order to view the website 'output'.  

If you wish to stop the site running...just type in...at the terminal window.

[CTRL]+[C]  

...which will stop the web server running.  

NOTE: 

- If your web browser already had opened windows before...; then, those windows will still remain open.  

- If your web browser was opened from Streamlit itself...; then, it will automatically close the web browser down...  
whenever you choose to stop the web sever running, anymore.  
  
