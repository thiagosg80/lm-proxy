from dotenv import dotenv_values


def get_env_config() -> dict:
    return dotenv_values('../resources/.env')
