from app import create_app

app = create_app()

if __name__ == "__main__":
    # Assurez-vous que l'application utilise le bon hôte et port pour Azure
    app.run(host="0.0.0.0", port=8000)
