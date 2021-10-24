

def application (environ, start_response):

    # Returns a dictionary in which the values are lists
    d = environ['QUERY_STRING'].split("&")
    print(d)
    s=""
    for el in d:
       s = s + "%s\n"%(el)
    response_body = s
    status = '200 OK'

    # Now content type is text/plain
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [str.encode(response_body)]



# Now it is serve_forever() in instead of handle_request()
