# Codeforces

1. Theatre Square

   * The length and breadth of the rectangle and the side of the square are inputted from the user.
   * A function is used to calculate the number of squares needed to completely cover the rectangle.
   * We find the area of the rectangle and divide it by the area of the square.
   * We use ceil function to convert the value that we get after division to get the next possible integer number.
   * This value gives us the number of flagstones.

2. Way Too Long Words

   * The number of words and the words itself is input by the user.
   * Each of the strings is iterated through a for loop.
   * If the length of the string is greater than 10 then the word is manipulated as the first character, string length-2 the last character and is stored in a list.
   * Similarly we do this process to each inputted string.
   * Using another for loop, we output all the elements in the list one by one.

3. Next Round

   * The number of teams, the position k and the scores of the teams in descending order are input by the user.
   * A loop is used to iterate over each of the scores stored in an array.
   * If the score is greater than or equal to the score of the kth team and the if the score is positive(>0) then a variable num, which is the number of teams which will advance in the next round, is incremented.
   * Num is displayed which is the required output.

4. Bit++

   * The number of statements and the statements are input by the user.
   * Each of the statements is stored in a list.
   * We will then print the sum of the count of "X++" and count of "++X" and count of "X--" and count of "--X", which will give us the output.

5. Football

   * The string which contains 0s and 1s is input by the user.
   * If "0000000" or "00000000" or "000000000" or "0000000000" or "00000000000" or "1111111" or "11111111" or "111111111" or "1111111111" or "11111111111" is there in string, we will then print "YES".
   * Else we will print "NO".
