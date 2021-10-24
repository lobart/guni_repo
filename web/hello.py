def application(environ, start_response):
    # Returns a dictionary in which the values are lists
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    status = '200 OK'
    # Now content type is text/plain
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]

    start_response(status, response_headers)
    return iter(body)