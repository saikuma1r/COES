from Website import create
app = create()

if __name__=='__main__':
    app.run(debug=True)
    app.run(port=3000)