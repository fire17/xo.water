def encode(text, one_char, zero_char):
    # Convert the text to a list of integers representing the Unicode code points
    code_points = [ord(c) for c in text]

    # Convert each code point to binary and pad it with leading 0s to make it 8 bits long
    binary_strings = [bin(c)[2:].zfill(8) for c in code_points]

    # Join the binary strings together into a single string and then replace 1s and 0s with the specified characters
    encoded_text = "".join(binary_strings).replace(
        "1", one_char).replace("0", zero_char)

    return encoded_text


def decode(encoded_text, one_char, zero_char):
    # Replace the specified characters with 1s and 0s
    binary_string = encoded_text.replace(one_char, "1").replace(zero_char, "0")

    # Split the binary string into a list of 8-bit binary strings
    binary_strings = [binary_string[i:i+8]
                      for i in range(0, len(binary_string), 8)]

    # Convert each binary string to an integer and then a Unicode character
    decoded_text = "".join(chr(int(b, 2)) for b in binary_strings)

    return decoded_text

# char1, char2 = "A", "B"
char1, char2 = "֫", "ֿ"
char1, char2 = "֫", "ֹ"
char1, char2 = "ֿ",  "ֹ"



def makeSecret(text, one_char=char1, zero_char=char2):
    # Add the secret tags to the text
    secret_text = "<secret>{}</secret>".format(text)

    # Encode the secret text
    encoded_text = encode(secret_text, one_char, zero_char)

    return encoded_text


def detectSecret(text, one_char=char1, zero_char=char2):
    # Encode the secret tags and search for them in the text
    encoded_start_tag = encode("<secret>", one_char, zero_char)
    encoded_end_tag = encode("</secret>", one_char, zero_char)
    if encoded_start_tag not in text or encoded_end_tag not in text:
        return None, text

    # Extract the encoded secret message from the text
    start_index = text.index(encoded_start_tag) + len(encoded_start_tag)
    end_index = text.index(encoded_end_tag)
    encoded_secret_message = text[start_index:end_index]
    freeText = text[:start_index] + text[end_index:]

    return encoded_secret_message, freeText 


def recoverSecret(text, one_char=char1, zero_char=char2):
    # Check if there is a secret present in the text
    encoded_secret_message, freeText = detectSecret(text, one_char, zero_char)
    if encoded_secret_message is None:
        return None, freeText

    # Decode the secret message
    secret_message = decode(encoded_secret_message, one_char, zero_char)

    return secret_message, freeText

# def wrapSecret(text, pre="https://google.com/", post ="n1ce check it out", one_char=char1, zero_char=char2):
# def wrapSecret(text, pre="火.io/", post ="join/magic", one_char=char1, zero_char=char2):
def wrapSecret(text, pre="火.io/", post ="", one_char=char1, zero_char=char2):
    # Add the secret tags to the text
    secret_text = makeSecret(text, one_char, zero_char)
    return pre+secret_text+post


if __name__ == "__main__":
    
    text = "hello world"
    encoded_text = encode(text, char1, char2)
    # Output: "BBAABAAABBBBAAAAABBAAABBBAABBAABBBBBBBAAAABBABBBABBBBBAAAABAABBBAABBBBB"
    print(encoded_text)
    decoded_text = decode(encoded_text, char1, char2)
    print(decoded_text)  # Output: "hello world"
    assert text == decoded_text

    # Test the functions
    secret_text = "This is a secret message. fire.io"
    final = wrapSecret(secret_text)
    print(":::::::::::::::")
    print(final)
    print(":::::::::::::::")

    encoded_secret_text = makeSecret(secret_text, char1, char2)
    text = f"https://google.com/"+encoded_secret_text+"/ Some text after the secret."
    print(text)
    recovered, _ = recoverSecret(text, char1, char2)
    print(recovered)  # Output: "This is a secret message."
    assert secret_text == recovered
    print("...d0ne...")
    recovered, _ = recoverSecret("http://火.io/ֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֹֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿֿmagic", char1, char2)
    print("!!!!!!!!!!!!!!!!!!")
    print(recovered)