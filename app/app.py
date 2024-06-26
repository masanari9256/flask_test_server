from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.json.ensure_ascii = False

# last_request_data = {}
last_request_data = {
    "comment": "/test にGETリクエストを送ることで、疎通確認ができます。\n"
               "/test にPOSTリクエストを送ることで、リクエスト内容を表示できます。\n"
               "詳しくはREADMEを確認してください。",
    "method": "なし",
    "headers": {},
    "form": {},
    "json": None
}


@app.route("/test", methods=["GET"])
def test_response():
    response_data = {
        "comment": "テストサーバ 疎通確認",
        "method": request.method,
        "headers": dict(request.headers),
        "form": request.form.to_dict(),
        "json": request.get_json(silent=True)
    }
    return jsonify(response_data), 200


@app.route("/test", methods=["POST"])
def test_request():
    global last_request_data
    last_request_data = {
        "comment": "これはテストサーバです",
        "method": request.method,
        "headers": dict(request.headers),
        "form": request.form.to_dict(),
        "json": request.get_json(silent=True)
    }
    return jsonify(last_request_data), 200


@app.route("/display", methods=["GET"])
def display_html():
    return render_template("display.html", data=last_request_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
