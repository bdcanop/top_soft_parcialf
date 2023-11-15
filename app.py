from flask import Flask

app = Flask(__name__)

@app.route('/factorial/<int(signed=True):n>')
def calc(n):
    if n < 0:
        return "intenta con uno positivo"
    if n == 0:
        return "factorial : 1"
    factorial = 1
    if n > 0:
        for i in range(1, n+1):
            factorial *= i
        return f"Factorial: {factorial}"
    
if __name__ == '__main__':
    app.run()