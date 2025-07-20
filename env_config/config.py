from pydantic_settings import BaseSettings, SettingsConfigDict

# Create class to manage environmental variables
class EnvConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)
    
    GEMINI_API_KEY:str
    OPENAI_API_KEY:str
    
    