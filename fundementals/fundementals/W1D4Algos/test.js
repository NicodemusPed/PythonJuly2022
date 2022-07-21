const str1 = "a x a";

function isPalindrone(str) {
    let reversed = str.split("").reverse().join("")
    return str === reversed
}

console.log(isPalindrone(str1))