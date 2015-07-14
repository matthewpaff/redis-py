# Roadmap example

Pass an existing Redis client to `cache_json`, `read_json`, or `get_or_load`. Keyword arguments support the historical Redis/StrictRedis `setex` parameter orderings. JSON null is treated as a cache miss. The loader should be idempotent: this simple example does not coordinate simultaneous misses. Redis errors propagate.

See RECONSTRUCTION.md for provenance and verification limits.
