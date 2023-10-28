def plusOne(digits):
    carry = 1  # Start with a carry of 1
    i = 0  # Initialize the index for the rightmost digit
    digits = digits[::-1]  # Reverse the array to start from the right

    while carry:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
        else:
            digits.append(carry)
            carry = 0
        i += 1

    return digits[::-1]  # Reverse the array back to the original order
