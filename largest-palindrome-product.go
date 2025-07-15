package main

import (
	"fmt"
	"strconv"
)

//finds the largest palindrome made from the product of two 3-digit numbers
func main() {
	maximalPalindrome := 0
	for i := 999; i >= 1; i-- {
		for j := 999; j >= 1; j--{
			
			if isPalindrome(i*j) {	
				if (i*j) > maximalPalindrome {
					maximalPalindrome = (i*j)
				}
			}
		}
	}

	fmt.Println(maximalPalindrome)



}


//this takes a positive number as input and compares the digits in order to check if number is a palindrome
func isPalindrome(n int) bool {
	intstring := strconv.Itoa(n)
	for i := 0; i < len(intstring)/2; i++ {
		digit := intstring[i]
		if digit != intstring[(len(intstring)-1-i)]{ //if at any place they don't match, return false
		return false
	}
}
	 return true
}
