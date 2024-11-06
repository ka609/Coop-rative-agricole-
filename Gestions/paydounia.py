# paydunya_config.py
import paydunya
from decouple import config

# Configurer PayDunya
paydunya.Payment.setup(
    master_key=config("PAYDUNYA_MASTER_KEY"),
    private_key=config("PAYDUNYA_PRIVATE_KEY"),
    public_key=config("PAYDUNYA_PUBLIC_KEY"),
    token=config("PAYDUNYA_TOKEN")
)
