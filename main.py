from flaskr import create_app, db

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    db.create_all(app=app)
    app.run(host='0.0.0.0', port=5000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
