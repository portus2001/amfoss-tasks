
// Grabbing DOM element
const button = document.getElementById('button');
const input = document.getElementById('username');
const display = document.getElementById('display');

const client_id = "Iv1.9e0c69672144e1df";
const client_secret = "3215d7d0b2aa060ac0d1062df249ce3a22adaf18";

// usersInfo variable will store all userdata 
var usersInfo = ''; 

// getData() fetch user data from given url & return Promise object
function getData(url){
    return new Promise(function(resolve,reject){

        // setting http request
        const xhr = new XMLHttpRequest();
        xhr.open('GET',url,true);

        xhr.onload = function(){
            // checking request status
            if(xhr.status === 200)
            {
                resolve(JSON.parse(xhr.responseText));
            }
            else{
                reject({ status:xhr.status, statusText:xhr.statusText });
            }
        }

        // handling error which may occur when getting response from server
        xhr.onerror = function(){
            reject({ status:xhr.status, statusText:xhr.statusText });

        }
        
        // sending request to server
        xhr.send();
    })
}


function clickEvent()
{
    //get input field value & convert it into array for multiple username
    const usernames = input.value.split(' ');
    // check weather input field is empty or not
    if(usernames[0] === '')
    {
        display.innerHTML = '<p class="warn">Please enter username !</p>';
        return;
    }
    else{

        // loop through each username
        usernames.forEach( username => {
            
            // github api url
            const url=`https://api.github.com/users/${username}`;
           
            // getData() return Promise
            getData(url)
            
            .then( data => {
                // create card & add userdata in it
                userInfo += 
                `<div class="card">
                    <img src=${data.avatar_url} alt="user image">
                    <img src = "https://identicons.github.com/${username}.png">
                    <div class="container">
                        <h2>${data.name}</h2>
                        <p><a href=${data.html_url} target="_blank">${data.html_url}</a></p>
                        <p>Username:  ${data.login}</p>
                        <p>Repos:  ${data.public_repos}</p>                      
                        <p>Bio:  ${data.bio}</p>
                    </div>
                </div>`;

                // display user data on webpage
                display.innerHTML = userInfo;
            })
            .catch( err => console.log(err.status,err.statusText));
        });    
      
       
       
        // reset input field value
        input.value = '';
    }
    
}


// Add click event on SUBMIT button
button.addEventListener('click',clickEvent);

// Add focus event on input field to reset display div & userInfo 
input.addEventListener('focus',()=>{display.innerHTML=''; userInfo='';});