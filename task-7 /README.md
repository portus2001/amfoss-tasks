# Task-7

# Rusted Email

## About

Write a program in Rust to find whether the given input is an email or not.
Example: good@email.com is a **VALID EMAIL**.

## How I Did

* Went through **[Regex link](https://docs.rs/regex/1.1.9/regex/)** and understood about regex.

* Learnt the basics of rust programming with the help of this **[link](https://www.youtube.com/watch?v=zF34dRivLOw)**.

* Learnt the syntax of an email with the help of this **[link](https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-)**.

* Created a regex crate in rust and made a default format of email ID.

* Input is then compared to the default email format using **is_match** function.

* If the inputted string(the email id) satisfies the regex, it prints **"Email Address is Valid."**, else prints **"Email Address is Invalid."**


