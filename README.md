# Project Overview

This is the root directory of the project. It contains all the services and integrations required for the smart assistant.
Each service or integration has its own directory which contains the interface definition for that service.
Please see the respective directory for more information on each service or integration.

## Project Structure

```text
/project_root
  /services
    /user_understanding
      user_understanding_service.py
    /context_awareness
      context_awareness_service.py
    /proactivity
      proactivity_service.py
  /integrations
    /home_assistant
      home_assistant_service.py
    /google_assistant
      google_assistant_service.py
    /financial_services
      financial_services.py
    /health_fitness
      health_fitness_service.py
  /user_control_and_transparency
    user_control_service.py
  /privacy_and_security
    privacy_security_service.py
  /interaction
    interaction_service.py
  /sleep_and_daily_routine_tracking
    sleep_routine_service.py
  /goal_setting_and_tracking
    goal_setting_service.py
  /medication_management
    medication_management_service.py
  /time_and_task_management
    time_task_management_service.py
  /emotional_support_and_wellbeing
    emotional_support_service.py
  /email_integration_and_notifications
    email_integration_service.py
  README.md
```

## Config

config.ini

```ini
[dialogflow]
project_id = your-dialogflow-project-id
session_id = your-dialogflow-session-id

[google_assistant]
token_file = google_assistant-token-file

[openai]
api_key = your-openai-api-key

[neo4j]
uri = your-neo4j-uri
user = your-neo4j-user
password = your-neo4j-password

[transformer_model]
model_name = your-transformer-model-name
```