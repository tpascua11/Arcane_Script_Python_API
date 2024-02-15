from server import app

if __name__ == "__main__":
    # Number of worker processes
    workers = 2
    # Bind to specific port
    bind = "0.0.0.0:5000"

    # Optionally add environment variables
    env = {"SECRET_KEY": "your_secret_key"}

    # Optionally customize other settings
    # ...

    # Start the application
    app.run(host=bind, workers=workers, **env)