def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print domain_name("http://github.com/carbonfive/raygun")
print domain_name("http://www.zombie-bites.com")
print domain_name("https://www.cnet.com")
