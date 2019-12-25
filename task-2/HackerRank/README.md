# HackerRank

1. Compare the Triplets

   * Three arrays are created,to store the ratings of Alice and Bob in the first two and the final score of both in the third array.
   * Ratings of both Alice and Bob is input by the user.
   * A function is used to compare the ratings of Alice and Bob and increment the score of the person the higher rating.
   * The score of Alice and Bob is printed.

2. Diagonal Difference

   * The user inputs the number of rows and columns of the square and its elements.
   * A function is used to calculate the sum of primary and secondary array. Let x be first index and y be the second. Then:
      * Primary diagonal y == x
      * Secondary diagonal y == n-x-1
   * Then their difference is calculated and printed.

3. Staircase

   * The user input a single integer n.
   * A function is used which prints the required staircase pattern.
   * A nested loop is used in which the outer loop and inner loop executes n times but "#" is printed only when inner loop variable is greater than a else prints " ", where a is equal to n-1 and is decremented after each outer loop execution.
   * This prints the required pattern.

4. Birthday Cake Candles

   * The user inputs the number of Candles and then the all the heights of the candles.
   * A function is used to find the number of tallest candles.
   * A for loop is used to find the tallest candle from an array.
   * Another function is used to count the number of tallest candles which would be equal to the height found earlier.
   * This count is displayed which is the required output.

5. Time Conversion

   * The user inputs time in 12 Hour format.
   * A function is used to convert the time in 12-hour format to 24-hour format.
   * The whole string containing the time is copied into a new string except the AM-PM part.
   * But if the time is AM and the hour is 12 then the new time is assingned with two zero and the remaining minutes and seconds part.
   * But if the time is AM and the hour is not 12 then the time will remain unchanged.
   * On the other hand, if time is PM and the hour is less than 12 then the hours is added to 12 and assigned along with the minutes and seconds part.
   * But if the time is PM and the hour is 12 then the time will remain unchanged.
