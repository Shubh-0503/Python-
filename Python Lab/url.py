#List of URLs
urls=[
    "http://example.com",
    "https://secure-site.com",
    "ftp://files.example.org",
    "https://another-secure-site.com"
    ]

#Filter out URLs that start with 'https'
https_urls=[url for url in urls if url.startswith('https')]

# Output the result
print(https_urls)
