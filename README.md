<h1>Lotto Game Project</h1>

<p style="text-align: justify;">
This project simulates the Italian lotto game.

For one thing, are generated the lottery tickets based on the choices performed by the user (numbers of tickets to generate, name of the wheel/city, type of bet, money to put, and amount of numbers to generate).

After that, a real extraction is simulated and is checked if there are any winning tickets.

If so, gross and net winnings are also calculated.

For more information about the rules of the game, visit:  https://www.sisal.it/lotto/come-si-gioca
</p>


<br/><br/>
<h2>Project Structure</h2>

For launch the program, start the file  `main.py`  present in the root directory and follow the instructions displayed. 
Alternatively, you can enter the number of tickets to (e.g., 3) be generated directly from the command line as follows:  `python main.py -n 3`


<h3>lotto_game folder</h3>

* <h4>lotto_game.py</h4>
  
	 In this file, we find the  **_business logic_**  of the entire program/project. In particular, we find: 
	 * the requests to the user about the  _**tickets number to generate**_, and for each ticket, the  **_type of bet_**, how many  _**numbers to generate**_  (between 1 and 10), the  _**amount of money**_  to put (between € 1 and € 200) and the  **_wheel/city_**  
	 
	 * the generation of the  _**tickets**_
	   
	 * the simulation of the lotto  _**extraction**_:  
	 https://www.servizitelevideo.rai.it/televideo/pub/pagina.jsp?p=786&s=0&r=Nazionale&idmenumain=0 
	 
	 * the verification of the _**winning tickets**_ and relative _**gross**_ and _**net winning**_.

    
* <h4> bet_type.py </h4> 
  
  It contains the  `BetType`  class, where are representing the information about the type of possible bet. Also is present the follow method:
    
	- **acquire_bet_type**
	  
        It is a static method that acquires from the user a numeric a numerical value relative to one of the possible types of bet. It returns the numerical value, and the corresponding name of the type of bet.

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

    * **calculate_total_gross_net_amount**
      
        This instance method calculates the total gross and net win for each ticket

    * **print_ticket**
      
        This method prints a ticket played.

    * **acquire_number_tickets**
      
        This static method acquires from the user the number of tickets to generate.

    * **acquire_money_put_ticket**
      
        This static method acquires from the user the amount of money to put on each ticket.


* <h4> win.py </h4>

    * **calculate_gross_net_win**
      
        This instance method calculates the gross and net win for each winning wheel/city.
        For more information visit: https://www.estrazionedellotto.it/prontuario-vincite-lotto


<br/><br/>
<h2>Example of Program in Execution</h2>

For launch the program, **start** the file  `main.py`  present in the root directory and follow the instructions displayed: 

![image](https://user-images.githubusercontent.com/74595044/135421216-6ddedf4f-a621-40f9-b021-72aad77d335a.png)

After choosing the **number of tickets to play**, a specific **bet** can be made for **each ticket**:

![image](https://user-images.githubusercontent.com/74595044/135421537-87de7e39-aa88-4f56-9121-18831bab11e2.png)

![image](https://user-images.githubusercontent.com/74595044/135421751-dcf457ad-615c-4e91-815b-e8cab0806b80.png)

Once the tickets have been played, the system carries out the **extraction** of the numbers:

![image](https://user-images.githubusercontent.com/74595044/135421845-385a6e0b-56c4-4c1c-b8ea-f47dcb2c97d1.png)

Finally, on the basis of the extraction carried out, it is checked **whether there are any winning tickets**:

![image](https://user-images.githubusercontent.com/74595044/135422186-9ea7f3ab-3bbe-4ac8-8498-e9e187e5a2c6.png)

![image](https://user-images.githubusercontent.com/74595044/135422234-a01c3621-898e-4dd8-99c8-78b4ed95db9a.png)

The program then **ends** its execution.



