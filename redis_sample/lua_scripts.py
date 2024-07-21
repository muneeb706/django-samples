from django_redis import get_redis_connection

# This implementation uses a Lua script with Redis to handle the 
# ticket purchase atomically, preventing race conditions. 
# The sorted set is used implicitly by storing the purchasers for each event.

TICKET_PURCHASE_SCRIPT = """
local event_key = KEYS[1]
local customer_username = ARGV[1]

local available_tickets = tonumber(redis.call('GET', event_key))

if available_tickets and available_tickets > 0 then
    redis.call('DECR', event_key)
    redis.call('SADD', event_key .. ':purchasers', customer_username)
    return 1
else
    return 0
end
"""

def purchase_ticket(event_id, customer_username):
    redis_conn = get_redis_connection("default")
    event_key = f"event:{event_id}:available_tickets"
    
    result = redis_conn.eval(TICKET_PURCHASE_SCRIPT, 1, event_key, customer_username)
    return result == 1