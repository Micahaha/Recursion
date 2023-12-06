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


    @staticmethod
    def computeMin(nums, i: int, min: int):
        """Finds the minimum number is a specified list of numbers.

        Args:
            nums (nums): specified list
            i (int): len of min(numbers)
            min (int): minimum value in list to find

        Returns:
            int: minimum number
        """
    
        if (i == len(nums)):
            return min
        else:
            if (nums[i] <= min):
                min = nums[i]
            return recursion.computeMin(nums,i+1, min)




    @staticmethod 
    def reverse(s: str, i: int):
        """Displays a specified string in reverse.

        Args:
            s (str): specified string
        """

        # The counter variable in the loop is the index
        #  used to iterate through the characters in the string 

        # The stopping case for the loop is i == 0
        

        # with each iteration of the loop we're 
        # decrementing the counter variable 

        # when the loop stops we're printing a message 


        if( i == 0):
            print(" is the reverse of %s using a loop." % (s))
        else:

            print(s[i - 1], end="")
            recursion.reverse(s, i-1)

      





