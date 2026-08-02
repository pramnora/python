# USE PYTHON 3 CODE TO CREATE YOUR OWN 'CHATBOT'...

**CREATED**: *Sun 2nd Aug 2026 12:17 PM GMT*  
**UPDATED**: *Sun 2nd Aug 2026 12:17 PM GMT*  

----

**PROGRAM**: Google Gemini chatbot  
**OS/OPERATING SYSTEM**: Linux Mint 22.3  
**LANGUAGE**: Python3, Version: 3.12.3  
**COMPUTER**: Home based Fujitsu mini-PC  

-----

## HOW THIS CODE CAME ABOUT

I was watching a YouTube 'short' video: (YouTube Channel: @CodeW1thAlex):  
- https://www.youtube.com/shorts/hW1-H1RgRsA  
...which explained you can build a Google Gemini Chatbot -using Python code- in 60 seconds.  

I never hand coded a chatbot program before...; so, I was really curious to try.  

I suffer from ADD/Attention Deficit Disorder(Short attention span)...;  
but, I can touch type fairly fast: 60 w.p.m;  
therefore, I thought this code should be very 'quick and easy' for me to type in/and, then, run.    

-----

## 3 different variations

The video showed around 3 different variations of the code:-

- Version 1: hard coded -non interactive- prompt: (7 lines)  
- Version 2: enter your own -interactive- prompt by typing it in from the keyboard: (8 lines)  
- Version 3: the final version/without my extra code comments/and, extra vertical line spaces: (9 lines)
- 
-----

Version 1

-----

> from google import genai
 
> client=genai.Client(api_key="MY_SECRET_API-KEY")

> response=client.models.generate_content(
>    model="gemini-3.5-flash",
>    contents="Explain Python to me!"
> )

> print(response.text)

-----

Version 2

-----

> from google import genai
 
> client=genai.Client(api_key="MY_SECRET_API-KEY")

> message=input("You: ")

> response=client.models.generate_content(
>    model="gemini-3.5-flash",
>    contents=message
> )

> print(response.text)

-----

Version 3

-----

> from google import genai
 
> client=genai.Client(api_key="MY_SECRET_API-KEY")

> chat=client.chats.create(model="gemini-3.5-flash")

> while True:
>    message=input("You: ")
>    if message.lower() in ("exit","quit"):
>      break
>    response=chat.send_message(message=message)
>    print(f"Bot: {response.text}\n")

----

## Setting up the coding environment to run:

The video explains it all in 60 seconds.  
But, in reality, it takes a lot more time...  
to be able to set up/and, run the code, effectively,   
using your own programming environment.  

-(**NOTE**: If setting up is something you find difficult to do...;    
  then, do what I do which is just use:   
  https://gemini.google.com  
  ...to help you sort things out whenever you find you are stuck.  
  I just *copy and paste* in any error messages;  
  and, then, let web browser based Gemini *chatbot* figure out telling me how to fix it.)-  

First, get a Google API key...  
- https://aistudio.google.com/api-keys  

-(**NOTE**: You may if you wish choose to 'delete' the Google API key, afterwards...; so as to avoid running up charges.)-  
    
Set up a virtual environment:  
> sudo apt install python3-venv python3.12-venv -y   
> python3 -m venv my-env  
> source my-env/bin/activate                             

-(**NOTE**: Linux Mint wouldn't let me install: google-genai, unless it was under a virtual environment.)-  

Next, install Pip:  
> sudo apt install python3-pip    
Install Google Gemini:    
> pip install google-genai  

Now, you should be able to run the code, effectively; and, without running into any problems.  
