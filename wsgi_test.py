from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    write = start_response(status, response_headers)
    write('hello world\n')
    return [u"This is hello wsgi app".encode('utf8')]

httpd = make_server('', 8078, simple_app)
print "Serving on port 8078..."
httpd.serve_forever()
