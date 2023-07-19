<!DOCTYPE html>

<html lang="en">

 <!--Page created: 12:20 19/07/2023
     Last updated: 12:20 19/07/2023-->

 <head>

  <meta charset="utf-8">
  
  <title>My Py-repl</title>
               
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css">

  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>

  <style>
   header{text-align:center;}
  </style>
  
 </head>
 
 <body>
 
  <header>
   <h1>Python REPL/Read Eval Print Loop</h1>
   <p>
    -(<b>Instructions</b>: [SHIFT]+[ENTER] to evaluate a line of code/
   <br>
   Press green arrow to the right to evaluate a block of code.
   </p>
  </header>

  <main>
   <py-repl id="my-repl" auto-generate="true">
   </py-repl>
  </main>

 </body>
 
</html>
