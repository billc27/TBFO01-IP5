// program to check if the string is palindrome or not

function checkPalindrome(string) {

    // find the length of a string
    const len = string.length;

    // loop through half of the string
    for (let i = 0; i < len / 2; i++) {

        // check if first and last string are same
        if (string[i] !== string[len - 1 - i]) {
            return 'It is not a palindrome';
        }
    }
    return 'It is a palindrome';
}
/*
    oeirugt 4398!@#$%^*)(^$)
*/
// take input
const string = prompt('Enter a string: ');

// call the function
const value = checkPalindrome(string);

const x = () => {

}

function x(){

}

console.log(value);

