# Cash

## About

Implement a program that calculates the minimum number of coins required to give a user change.

## How I Did

* User is asked to input the amount.

* Using a **do-while loop**, the user is again asked to input, if he gives a negative value as the amount.

* The number of **dollars are converted into cents** by multiplying the amount with 100.

* A **while** loop is used, which iterates until the amount is equal to zero.

* After each iteration, the **amount is decremented by 25 or 10 or 5 or 1**, based on the current value of amount.

* A counter is set up such that after each iteration the counter gets incremented by one.

* After all the iterations the value of the counter is printed, which gives us the minimum number of coins.