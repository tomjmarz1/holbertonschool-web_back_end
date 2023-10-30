const {stdin, stdout} = require('node:process');

stdout.write("Welcome to Holberton School, what is your name?")
let name;
stdin.on('readable', () =>{
    name = stdin.read();
    stdout.write("Your name is: " + name + "\nThis important software is now closing");
    
})



stdin.on('end', () => {
    stdout.write('This important software is now closing\n');
})