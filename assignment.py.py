{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6136bc33-b0d1-4874-88d3-34e5dac7bf6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The second largest number is: 45\n"
     ]
    }
   ],
   "source": [
    "def find_second_largest(numbers):\n",
    "    if len(numbers) < 2:\n",
    "        return None \n",
    "    largest = second_largest = float('-inf')\n",
    "\n",
    "    for num in numbers:\n",
    "        if num > largest:\n",
    "            second_largest = largest\n",
    "            largest = num\n",
    "        elif largest > num > second_largest:\n",
    "            second_largest = num\n",
    "\n",
    "    if second_largest == float('-inf'):\n",
    "        return None \n",
    "    return second_largest\n",
    "\n",
    "\n",
    "my_list = [10, 20, 4, 45, 99, 99]\n",
    "result = find_second_largest(my_list)\n",
    "\n",
    "if result is not None:\n",
    "    print(\"The second largest number is:\", result)\n",
    "else:\n",
    "    print(\"No second largest number found.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "60efecd3-940c-452f-b087-efafbd6f427c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorted list without duplicates: [1, 2, 3, 4, 7]\n"
     ]
    }
   ],
   "source": [
    "def remove_duplicates_and_sort(lst):\n",
    "    unique_list = []\n",
    "    for item in lst:\n",
    "        if item not in unique_list:\n",
    "            unique_list.append(item)\n",
    "    \n",
    "   \n",
    "    for i in range(len(unique_list)):\n",
    "        for j in range(i + 1, len(unique_list)):\n",
    "            if unique_list[i] > unique_list[j]:\n",
    "                unique_list[i], unique_list[j] = unique_list[j], unique_list[i]\n",
    "    \n",
    "    return unique_list\n",
    "\n",
    "\n",
    "my_list = [4, 2, 7, 2, 3, 4, 1, 7]\n",
    "result = remove_duplicates_and_sort(my_list)\n",
    "print(\"Sorted list without duplicates:\", result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "96d3aa19-25e7-4325-889b-b2f9734f1079",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum of the list: 150\n",
      "Average of the list: 30.0\n"
     ]
    }
   ],
   "source": [
    "def sum_and_average(numbers):\n",
    "    total = 0\n",
    "    count = 0\n",
    "\n",
    "    for num in numbers:\n",
    "        total += num\n",
    "        count += 1\n",
    "\n",
    "    average = total / count if count != 0 else 0\n",
    "\n",
    "    return total, average\n",
    "my_list = [10, 20, 30, 40, 50]\n",
    "total, average = sum_and_average(my_list)\n",
    "\n",
    "print(\"Sum of the list:\", total)\n",
    "print(\"Average of the list:\", average)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9f0663ef-5977-4958-9d5f-6126a995fac3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 is not a prime number.\n"
     ]
    }
   ],
   "source": [
    "def is_prime(num):\n",
    "    if num <= 1:\n",
    "        return False  # 0 and 1 are not prime numbers\n",
    "    for i in range(2, int(num**0.5) + 1):  # Only check up to sqrt(num)\n",
    "        if num % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "\n",
    "number = int(input(\"Enter a number: \"))\n",
    "if is_prime(number):\n",
    "    print(number, \"is a prime number.\")\n",
    "else:\n",
    "    print(number, \"is not a prime number.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5a3d4804-5814-472f-b1d2-ba22d4de6756",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string:  patanjali\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vowels: 4\n",
      "Consonants: 5\n",
      "Digits: 0\n",
      "Special Characters: 0\n"
     ]
    }
   ],
   "source": [
    "def count_characters(string):\n",
    "    vowels = consonants = digits = special_chars = 0\n",
    "    for char in string:\n",
    "        if char.lower() in 'aeiou':\n",
    "            vowels += 1\n",
    "        elif char.isalpha():\n",
    "            consonants += 1\n",
    "        elif char.isdigit():\n",
    "            digits += 1\n",
    "        else:\n",
    "            special_chars += 1\n",
    "    return vowels, consonants, digits, special_chars\n",
    "\n",
    "text = input(\"Enter a string: \")\n",
    "v, c, d, s = count_characters(text)\n",
    "print(\"Vowels:\", v)\n",
    "print(\"Consonants:\", c)\n",
    "print(\"Digits:\", d)\n",
    "print(\"Special Characters:\", s)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "29391df4-8ee0-40f2-a042-5bbeb68bd609",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "for num in range(1, 101):\n",
    "    if num % 2 == 0:\n",
    "        print(num)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "75478c0e-e2d9-4c5f-9af9-79a49dd4de4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9 x 1 = 9\n",
      "9 x 2 = 18\n",
      "9 x 3 = 27\n",
      "9 x 4 = 36\n",
      "9 x 5 = 45\n",
      "9 x 6 = 54\n",
      "9 x 7 = 63\n",
      "9 x 8 = 72\n",
      "9 x 9 = 81\n",
      "9 x 10 = 90\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "for i in range(1, 11):\n",
    "    print(num, \"x\", i, \"=\", num * i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c19b5f9e-02d4-49df-a03b-02505b15773e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[15, 30, 45, 60, 75, 90]\n"
     ]
    }
   ],
   "source": [
    "divisible_by_3_and_5 = []\n",
    "for num in range(1, 101):\n",
    "    if num % 3 == 0 and num % 5 == 0:\n",
    "        divisible_by_3_and_5.append(num)\n",
    "\n",
    "print(divisible_by_3_and_5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "901ac090-b8ef-4e6e-8e9d-2adafcef0960",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed number: 01\n"
     ]
    }
   ],
   "source": [
    "num = input(\"Enter a number: \")\n",
    "print(\"Reversed number:\", num[::-1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8b869733-bcd7-48c5-917f-8bfd4f847ecd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string:  xyz\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'x': 1, 'y': 1, 'z': 1}\n"
     ]
    }
   ],
   "source": [
    "def char_frequency(s):\n",
    "    freq = {}\n",
    "    for char in s:\n",
    "        freq[char] = freq.get(char, 0) + 1\n",
    "    return freq\n",
    "\n",
    "text = input(\"Enter a string: \")\n",
    "print(char_frequency(text))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ecc96bec-d3d3-4192-945b-9078e3b26318",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter n:  100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]\n"
     ]
    }
   ],
   "source": [
    "def is_prime(num):\n",
    "    if num <= 1:\n",
    "        return False\n",
    "    for i in range(2, int(num**0.5)+1):\n",
    "        if num % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def generate_primes(n):\n",
    "    primes = []\n",
    "    num = 2\n",
    "    while len(primes) < n:\n",
    "        if is_prime(num):\n",
    "            primes.append(num)\n",
    "        num += 1\n",
    "    return primes\n",
    "\n",
    "n = int(input(\"Enter n: \"))\n",
    "print(generate_primes(n))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "21445cb3-24e2-4fa9-a95f-59512245d343",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  11\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11 is a palindrome\n"
     ]
    }
   ],
   "source": [
    "num = input(\"Enter a number: \")\n",
    "if num == num[::-1]:\n",
    "    print(num, \"is a palindrome\")\n",
    "else:\n",
    "    print(num, \"is not a palindrome\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e4035a73-f930-4e2f-972c-843f0fbfa9f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter element to count:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "lst = [1, 2, 3, 2, 4, 2, 5]\n",
    "element = int(input(\"Enter element to count: \"))\n",
    "print(lst.count(element))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1c028bf1-d2f6-4bc0-8d78-d647c0677cda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500]\n"
     ]
    }
   ],
   "source": [
    "squares = [x**2 for x in range(2, 51, 2)]\n",
    "print(squares)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "214803f6-7afb-4a50-8249-f21e50fe8755",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "def unique_elements(lst):\n",
    "    unique = []\n",
    "    for item in lst:\n",
    "        if item not in unique:\n",
    "            unique.append(item)\n",
    "    return unique\n",
    "\n",
    "lst = [1, 2, 2, 3, 4, 4, 5]\n",
    "print(unique_elements(lst))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b5e8f674-1e67-48df-8fa6-fa7cc6d98548",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_even(num):\n",
    "    return \"Even\" if num % 2 == 0 else \"Odd\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "865410e1-ac05-4dfd-b6cd-8a8b0ed33bd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cumulative_sum(lst):\n",
    "    result = []\n",
    "    total = 0\n",
    "    for num in lst:\n",
    "        total += num\n",
    "        result.append(total)\n",
    "    return result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7d3a512d-0317-40be-a49a-02a031389c09",
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial(n):\n",
    "    if n == 0 or n == 1:\n",
    "        return 1\n",
    "    return n * factorial(n-1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d20f1ad2-4d8d-45e1-8873-cf9eb0418241",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fibonacci(n):\n",
    "    a, b = 0, 1\n",
    "    for _ in range(n):\n",
    "        print(a, end=' ')\n",
    "        a, b = b, a + b\n",
    "    print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1a96ecbe-ace8-4813-8636-eeab8d16df8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_palindrome(s):\n",
    "    s = s.lower()\n",
    "    return s == s[::-1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5c526eac-2987-4ed1-89cf-83c4c3733038",
   "metadata": {},
   "outputs": [],
   "source": [
    "def max_min(lst):\n",
    "    return max(lst), min(lst)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "bf3430e7-1b62-482f-ac59-fbbe4aee5922",
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "\n",
    "def is_pangram(s):\n",
    "    s = s.lower()\n",
    "    return set(string.ascii_lowercase).issubset(set(s))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "1c18230c-2665-45c5-9749-94bca284e2e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_prime(num):\n",
    "    if num < 2:\n",
    "        return False\n",
    "    for i in range(2, int(num**0.5)+1):\n",
    "        if num % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def primes_in_range(start, end):\n",
    "    return [num for num in range(start, end+1) if is_prime(num)]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "74466ccf-cc97-491e-b345-35571638f0f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_case(s):\n",
    "    upper = sum(1 for c in s if c.isupper())\n",
    "    lower = sum(1 for c in s if c.islower())\n",
    "    return upper, lower\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "34486d26-1d66-4b43-9329-2e307bd3c86b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def sum_of_digits(num):\n",
    "    return sum(int(d) for d in str(abs(num)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "ee5bc9bd-8dad-48c5-8b5e-7cfdfa33d960",
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_words(sentence):\n",
    "    return len(sentence.split())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "3a960ec8-2794-4fa5-bfbf-efe596f17c46",
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "\n",
    "def remove_punctuation(s):\n",
    "    return ''.join(ch for ch in s if ch not in string.punctuation)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "dc4df625-f9a0-4296-bbf8-fe6065a3bc5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def gcd(a, b):\n",
    "    while b:\n",
    "        a, b = b, a % b\n",
    "    return a\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "279b304c-8f95-42c1-9be4-1b044fde6259",
   "metadata": {},
   "outputs": [],
   "source": [
    "def duplicates(lst):\n",
    "    seen = set()\n",
    "    duplicates = set()\n",
    "    for item in lst:\n",
    "        if item in seen:\n",
    "            duplicates.add(item)\n",
    "        else:\n",
    "            seen.add(item)\n",
    "    return list(duplicates)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3ecea89e-39fc-4670-ba12-1259c4bdbcf0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def largest_of_three(a, b, c):\n",
    "    return max(a, b, c)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14de4315-4198-4815-8eba-639a1d9e3b1c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
