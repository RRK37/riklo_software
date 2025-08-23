#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

std::uint64_t b_7 = 18302628885633695744;
std::uint64_t b_6 = 18158513697557839872;
std::uint64_t b_5 = 17870283321406128128;
std::uint64_t b_4 = 17293822569102704640;
std::uint64_t b_3 = 16140901064495857664;
std::uint64_t b_2 = 13835058055282163712;
std::uint64_t b_1 = 9223372036854775808;


std::uint64_t* shift(std::uint64_t initial[9], std::uint8_t b) {
    
    std::uint64_t shifted[9];
    return shifted;    
}

std::uint64_t* accumilate(std::uint64_t shifted[9], std::uint64_t accumilated[9]) {
    
    std::uint64_t accumilated[9];
    return accumilated;    
}

int get_nth_digit(std::uint64_t number, int digit) {
    
    string number_string = to_string(number);
    int length = number_string.length();
    
    if (digit > length) {
        return -1; 
    }
    return int(number_string[length-digit]);
    
}

void extraLongFactorials(int n) {
    
    std::uint8_t u_n = n;
    
    // Initial value which keeps track of the culmination of products at the start of each
    // loop. Starts at 1, since the first product is 1. 
    std::uint64_t initial [9];
    initial[0] = initial[1] = initial[2] = initial[3] = 
    initial[4] = initial[5] = initial[6] = initial[7] = 0;
    initial[8] = 1;
    
    for (std::uint8_t i = 2; i <= u_n; i++) { // Go through each of the factorial multipliers.
        std::uint64_t* accumilated;
        for (std::uint8_t b = 0; b < 7; b++) { // Check each bit in the multiplier.
            if ((1 << b) & i) { // Chech if bit 'b' in 'i' is 1.
            
                std::uint64_t* shifted  = shift(initial, b);
                accumilated             = accumilate(accumilated, shifted);
                
            }
        }
        initial[0] = accumilated[0]; initial[1] = accumilated[1]; initial[2] = accumilated[2];
        initial[3] = accumilated[3]; initial[4] = accumilated[4]; initial[5] = accumilated[5];
        initial[6] = accumilated[6]; initial[7] = accumilated[7]; initial[8] = accumilated[8];
    }
    
    std::uint64_t large_integer [9]; large_integer = initial;
    
    string result = "";
    int carry_over = 0;
    bool no_more_digits_to_add [9][64];
    for (int i = 0; i < 9; i++) for (int j = 0; j < 64; j++) no_more_digits_to_add[i][j] = 0;
    
    for (int digit = 0; digit < 158; digit++) { // 100! has 158 digits. 
        int accumilate = 0;
        for (int section = 8; section <= 0; section--){ // Each integer section of the result.
            for (uint64_t bit = 0; bit < 64; bit++) { // Each bit in the integer.
                
                // Check there are no more digits in this decimal representation of the binary value.
                // I.e. 2^7 = 128 has 3 digits, no point looking at the 4th.
                if (no_more_digits_to_add[section][bit]) continue; 
                else if (1 << bit & large_integer[section]) { // If the bit is on, find it's value. 

                    int exponent    = (8 - section) * 64 + bit;
                    int value       = pow(2, exponent);
                    
                    int nth_digit = get_nth_digit(value, bit); // Get just the necessary digit.
                    
                    if (nth_digit == -1) no_more_digits_to_add[section][bit] = True;
                    else accumilate += nth_digit;   
                }
            }
        accumilate += get_nth_digit(carry_over, 1); // Include the carry-over digit.
        result = result + to_string(accumilate)[-1]; // Save the final digit to the result string. 
        carry_over = carry_over/10 + accumilate /10; // Discard the smallest digit. (not needed)
        }
    }
    

}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    extraLongFactorials(n);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
