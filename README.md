<h1>Lotto Game Project</h1>

<p style="text-align: justify;">
This project simulates the Italian lotto game.

For one thing, are generated the lottery tickets based on the choices performed by the user 
(numbers of tickets to generate, name of the wheel/city, type of bet, money to put, 
and amount of numbers to generate).

After that, a real extraction is simulated and is checked if there are any winning tickets.

If so, gross and net winnings are also calculated.

For more information about the rules of the game, visit:
https://www.sisal.it/lotto/come-si-gioca
</p>

<h2>Project Structure</h2>

For launch the program, start the file `lotto_game.py` 
present in the root directory and follow the instructions displayed.
Alternatively, you can enter the number of tickets to (e.g., 3) be generated 
directly from the command line as follows: `py lotto_game.py -n 3`

<h3>lotto_game.py</h3>

In this file, we find the **_business logic_** of the entire program/project.
In particular, we find:
* the requests to the user about the _**tickets number to generate**_, and for each ticket, 
  the **_type of bet_**, how many _**numbers to generate**_ (between 1 and 10), 
  the _**amount of money**_ to put (between € 1 and € 200) and the **_wheel/city_**
* the generation of the _**tickets**_
* the simulation of the lotto _**extraction**_: 
  
    https://www.servizitelevideo.rai.it/televideo/pub/pagina.jsp?p=786&s=0&r=Nazionale&idmenumain=0
* the verification of the _**winning tickets**_ and relative _**gross**_ and _**net winning**_.

<h3>lotto_game folder</h3>

In this folder are contained all the classes used in the program/project:

* <h4> bet_type.py </h4> 
  
    It contains the `BetType` class, where are representing the information about the type of possible bet. 
    Also is present the follow method:
  
    * **acquire_bet_type**
      
      It is a static method that acquires from the user a numeric a numerical value relative
      to one of the possible types of bet. 
      It returns the numerical value, and the corresponding name of the type of bet.

* <h4> city.py </h4> 
  
    It contains the `City` class, where are representing the information about each city/wheel. 
    Also is present the follow method:
  
    * **acquire_city**
      
        It is a static method that acquires from the user a numeric a numerical value relative
        to one city/wheel. 
        It returns the numerical value, and the corresponding name of the city/wheel.

* <h4> extraction.py </h4> 
   
    It contains the `Extraction` class, and inside are present the dictionary named `extraction` that will contain 
    the simulated lotto extraction and two static method:
  
    * **perform_extraction**
      
        In this method 5 random numbers are generated for each city/wheel and storage in the dictionary 
        named `extraction`.
    
    * **print_extraction**
    
        This method displays on the screen the extraction previously generated.

* <h4> number_utils.py </h4>
  
    It contains the `NumberUtils` class, and inside are present two static method:
  
    * **acquire_amount_numbers**
    
        This static method acquires from the user the amount of numbers to generate for each ticket.
  
    * **generate_numbers**

        This static method returns an ordered list of integers (between 1 and 90).
    

* <h4> ticket.py </h4>

    * **storage_ticket**
      
        This instance method storages the tickets played.

    * **check_ticket**
      
        This instance method checks whether the ticket is winning or not.

    * **print_ticket**
      
        This method prints a ticket played.

    * **acquire_number_tickets**
      
        This static method acquires from the user the number of tickets to generate.

    * **acquire_money_put_ticket**
      
        This static method acquires from the user the amount of money to put on each ticket.


* <h4> win.py </h4>

    * **calculate_gross_net_win**
      
    This instance method calculates the gross and net win for each winning ticket.
      
