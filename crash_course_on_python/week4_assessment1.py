def format_address(address_string):
  # Declare variables
  street_number = None 
  street_name = None 
  # Separate the address string into parts
  words = address_string.split(" ", 1)
  # Traverse through the address parts
  street_number = words[0]
  street_name = words[-1]
  # Return the formatted string  
  return "house number {} on street named {}".format(street_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"