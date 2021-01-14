import selectors

EVENT_READ = (1 << 0)
EVENT_WRITE = (1 << 1)

print('event read: ', EVENT_READ)
# bitwise operator for event_read where bin(0b1) => '0b1'
print('event write: ', EVENT_WRITE)
# bitwise operator for event_write where bin(0b1) => '0b10'

mask = 0

if mask & EVENT_READ:
    print('mask & event_read')
if mask & EVENT_WRITE:
    print('mask & event_write')
