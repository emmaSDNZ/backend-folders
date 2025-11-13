import os

# === Configuración base ===
BASE_DIR = "backend"

# Diccionario con estructura de carpetas y archivos
structure = {
    "app": {
        "main.py": "# Punto de entrada de la aplicación\n",
        "core": {
            "__init__.py": "",
            "config.py": "# Configuración global\n",
            "security.py": "# Seguridad y autenticación\n",
            "logger.py": "# Logging y monitoreo\n",
        },
        "shared": {
            "__init__.py": "",
            "db": {
                "__init__.py": "",
                "session.py": "# Conexión con la base de datos\n",
                "init_db.py": "# Inicialización de tablas o seeds\n",
            },
            "utils": {
                "__init__.py": "",
                "validators.py": "# Validaciones generales\n",
                "formatters.py": "# Formateo de datos\n",
            },
            "ai": {
                "__init__.py": "",
                "predictor.py": "# Predicciones ML/NLP globales\n",
                "retraining_pipeline.py": "# Pipeline de reentrenamiento\n",
            },
            "messaging": {
                "__init__.py": "",
                "whatsapp_client.py": "# Integración con WhatsApp API\n",
                "email_client.py": "# Envío de correos\n",
            },
            "cron": {
                "__init__.py": "",
                "scheduler.py": "# Tareas automáticas programadas\n",
            },
        },
        "modules": {
            "patients": {
                "__init__.py": "",
                "api": {"patients_routes.py": ""},
                "controllers": {"patients_controller.py": ""},
                "services": {"patients_service.py": ""},
                "models": {"patient_model.py": ""},
                "schemas": {"patient_schema.py": ""},
            },
            "appointments": {
                "__init__.py": "",
                "api": {"appointments_routes.py": ""},
                "controllers": {"appointments_controller.py": ""},
                "services": {"appointments_service.py": ""},
                "models": {"appointment_model.py": ""},
                "schemas": {"appointment_schema.py": ""},
            },
            "results": {
                "__init__.py": "",
                "api": {"results_routes.py": ""},
                "services": {"results_service.py": ""},
                "models": {"result_model.py": ""},
            },
            "faqs": {
                "__init__.py": "",
                "api": {"faqs_routes.py": ""},
                "services": {"faqs_service.py": ""},
            },
            "human_derivation": {
                "__init__.py": "",
                "api": {"human_routes.py": ""},
                "services": {"human_service.py": ""},
            },
            "reminders": {
                "__init__.py": "",
                "api": {"reminders_routes.py": ""},
                "services": {"reminders_service.py": ""},
                "cron_jobs": {"reminders_cron.py": ""},
            },
            "analytics_ai": {
                "__init__.py": "",
                "api": {"ai_routes.py": ""},
                "services": {
                    "training_service.py": "",
                    "prediction_service.py": "",
                },
                "models": {"feedback_model.py": ""},
                "data": {"feedback_logs.csv": ""},
            },
        },
    },
    "tests": {
        "__init__.py": "",
        "test_patients.py": "",
        "test_appointments.py": "",
    },
    ".env": "",
    "requirements.txt": "",
    "Dockerfile": "",
    "docker-compose.yml": "",
    "README.md": "",
}


# === Función recursiva para crear carpetas y archivos ===
def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


if __name__ == "__main__":
    os.makedirs(BASE_DIR, exist_ok=True)
    create_structure(BASE_DIR, structure)
    print(f"✅ Estructura completa creada dentro de ./{BASE_DIR}/")
