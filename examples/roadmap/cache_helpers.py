# Modern historical reconstruction, created 2026-11-04.
import json

def cache_json(client, key, value, ttl=60):
    """Serialize a value and give it an explicit, positive expiration."""
    ttl = int(ttl)
    if ttl < 1:
        raise ValueError("ttl must be positive")
    return client.setex(name=key, time=ttl, value=json.dumps(value))

def read_json(client, key):
    """Return a decoded value, or None for a missing cache key."""
    raw = client.get(key)
    if raw is None:
        return None
    if hasattr(raw, "decode"):
        raw = raw.decode("utf-8")
    return json.loads(raw)

def get_or_load(client, key, loader, ttl=60):
    """Load a missing value once per call and cache it with a TTL."""
    cached = read_json(client, key)
    if cached is not None:
        return cached
    value = loader()
    cache_json(client, key, value, ttl=ttl)
    return value
