def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 401 | 402 | 403:
            return "not allowed"
        case 404:
            return "not found"        
        case 418:
            return "i'm a teapot"
        case _: 
            return "something's wrong with the internet"

http_list = [400, 401, 404, 418, 500]
for code in http_list:
    print(http_error(code))