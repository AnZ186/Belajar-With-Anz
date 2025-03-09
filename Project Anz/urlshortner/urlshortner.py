import pyshorteners

url = input("Enter the URL: \n")

print("URL After Shortening :- ", pyshorteners.Shortener().tinyurl.short(url)) # Fungsinya untuk memperpendek URL
