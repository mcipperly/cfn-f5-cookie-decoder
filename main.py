import struct
import sys
import json

from flask import (Flask, request, redirect)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def idx():
    return("")       


@app.route('/decode', methods=['GET'])
def decode():
    try:
        bigip_cookie = request.args.get('cookie')
        (host, port, end) = request.args.get('cookie').split('.')
    except:
        return((json.dumps({"status": "bad cookie"}),
                400,
                {"content-type": "application/json"}))

    (a, b, c, d) = [i for i in struct.pack("<I", int(host))]
    p = [i for i in struct.pack("<I", int(port))]
    portOut = p[0]*256 + p[1]
    return((json.dumps({"status": "ok",
                        "nodeinfo": "{}.{}.{}.{}:{}".format(a,b,c,d,portOut)}),
            200,
            {"content-type": "application/json"}))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

