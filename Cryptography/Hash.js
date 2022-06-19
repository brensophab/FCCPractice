const {createHash} = require('crypto')
//Create a string hash

function hash(input){
    return createHash('sha256').update(input).digest('base64')
}

let password = 'hi-mom'
const hash1 = hash(password)
console.log(hash1 + '\n')
password = 'hi-mom2'
const hash2 = hash(password)
console.log(hash2 + '\n')
const match = hash1 ===hash2

console.log(match ? 'Correct password': 'Incorrect password, does not match')