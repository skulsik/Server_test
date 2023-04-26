from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        """ Обработка GET запроса """
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("Hello, World wide web!".encode('utf-8'))

    def do_POST(self) -> None:
        """ Обработка POST запроса """
        content_length: int = int(self.headers['Content-Length'])
        data: bytes = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Your POST request!\n')
        print(f'Received data: {data.decode()}')


def run() -> None:
    """ Запуск сервера """
    server_address: tuple[str, int] = ('localhost', 8080)
    httpd = HTTPServer(server_address, Server)
    print('Starting server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
