from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        origen = request.form.get("origen")
        destino = request.form.get("destino")
        fecha = request.form.get("fecha")
        mensaje = f"Reserva realizada: {origen} → {destino} el {fecha}"
    return render_template("index.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
