

def application (environ, start_response):

    # Returns a dictionary in which the values are lists
    d = environ['QUERY_STRING'].split("&")
    response_body = "\n".join(d).encode('utf-8')
    status = '200 OK'

    # Now content type is text/plain
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]



# Now it is serve_forever() in instead of handle_request()
