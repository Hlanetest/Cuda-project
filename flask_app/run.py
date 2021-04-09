from app import api

if __name__ == "__main__":
    metrics.start_http_server(9999)
    api.run()
