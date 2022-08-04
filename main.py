from application import create_app, db, routes

app = create_app()

app.app_context().push