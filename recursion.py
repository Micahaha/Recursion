class recursion:  
    @staticmethod
    def factorial(n: int):
        """Computes the factorial of a specified number.

        Args:
            n (int): specified number, for example, 6

        Returns:
            int: computed factorial
        """        
    
        # this is the stopping case
        if(n == 1):
            return n 
        else:
            # this is the general rule that includes
            # the recursive call
            return n * recursion.factorial(n - 1)

    @staticmethod
    def power(number: int, power: int):
        """Takes a specified number to a specified power

        Args:
            number (int): specified number; for example, 2
            power (int): specified power for example, 5

        Returns:
            int: computed power
        """        
        # the counter variable for the loop contains 
        # the same value as power


        # the loop will repeat as long as i > 1
        # the condition that will cause the loop to stop
        # is when i == 1 -> stopping case for the loop

        # with each iteration of the loop, we're decrementing
        # the counter variable by 1
        result = 1 

        if power == 0:
            return 1
        else:
            number *= recursion.power(number,power - 1)

        return number
