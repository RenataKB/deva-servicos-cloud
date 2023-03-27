import redis

redis_cli = redis.Redis(host="localhost", port=6379)
p = redis_cli.pubsub()
p.subscribe('meucanal', 'outrocanal')
p.get_message()
