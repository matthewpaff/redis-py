# Modern historical reconstruction, created 2026-11-04.
import json

def cache_json(client, key, value, ttl=60):
    """Serialize a value and give it an explicit, positive expiration."""
    ttl = int(ttl)
    if ttl < 1:
        raise ValueError("ttl must be positive")
    return client.setex(name=key, time=ttl, value=json.dumps(value))
