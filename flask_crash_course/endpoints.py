from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.post("/average")
def avg():
    js = request.get_json(force=True, silent=True)
    if not js or "nums" not in js:
        abort(400, "nums missing")
    try:
        nums = list(map(float, js["nums"]))
    except (TypeError, ValueError):
        abort(400, "non-numeric")
    return jsonify({"avg": sum(nums)/len(nums)}), 200