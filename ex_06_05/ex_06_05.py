# Parsing strings
# Take the following Python code that stores a string: str = 'X-DSPAM-Confidence: 0.8475 '. Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
str = 'X-DSPAM-Confidence: 0.8475 '
separator = str.find(':')
# print(separator)
confidence = str[separator+1:].strip() # deleting whitespaces
print(confidence)
print(type(confidence)) # still is a string

fconfidence = float(confidence)
print(type(fconfidence))
print(fconfidence)
