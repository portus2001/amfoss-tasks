/*extern crate regex;
use regex::Regex;
use std::io;
fn main(){
  println!("enter the email id");
  let mut text= String::new();
  io::stdin()
       .read_line(&mut text) 
       .expect("failed to read a line");
  assert!(Regex::new(r"\w[a-zA-Z0-9._+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]").unwrap().is_match(&text));
 }*/

extern crate regex;

use std::io;

use regex::Regex;


fn main(){


  println!("Enter the email");

  let mut input = String::new();

  io::stdin().read_line(&mut input);

  let exp = Regex::new(r"\w[a-zA-Z0-9._+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]").unwrap();
  
  let y:bool=exp.is_match(& mut input);

  if y == true{
      println!("Email is Valid");
  }else{
      println!("Email is Invalid");
  }
}
