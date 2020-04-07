class MiniLike:
    def __init__(self, hash_func, servers):
        self.hash_func = hash_func
        self.servers = servers
        self.num_servers = len(servers)

    def like(self, uid, status_id):
        key = '%s:%s' % (uid, status_id)
        server = self.get_server(key)
        server.set(key, 1)

    def unlike(self, uid, status_id):
        key = '%s:%s' % (uid, status_id)
        server = self.get_server(key)
        server.delete(key)

    def is_liked(self, uid, status_id):
        key = '%s:%s' % (uid, status_id)
        server = self.get_server(key)
        return server.get(key) == b'1'

    def get_server(self, key):
        return self.servers[self.hash_func(key) % self.num_servers]


if __name__ == '__main__':
    from redis import StrictRedis

    # ascii code of ':' is larger than any digit, so (c - '0') is non-negative
    def simple_hash(s):
        cnt, m = 0, 100
        for c in s:
            cnt += 31 * (ord(c) - ord('0'))
            cnt = cnt % m
        return cnt

    r = StrictRedis(host='localhost', port=6379)

    num_servers = 3
    redis_servers = [r] * num_servers
    mini_like = MiniLike(simple_hash, redis_servers)

    test_cases = [[1, 1], [1, 2], [2, 3], [2, 1]]

    # like actions
    mini_like.like(1, 1)
    mini_like.like(1, 2)
    mini_like.like(2, 3)
    mini_like.like(2, 1)

    print('after like actions:')
    for case in test_cases:
        print('%s like %s: %s' % (case[0], case[1], mini_like.is_liked(*case)))

    # unlike actions
    mini_like.unlike(1, 1)
    mini_like.unlike(2, 3)

    print('after unlike actions:')
    for case in test_cases:
        print('%s like %s: %s' % (case[0], case[1], mini_like.is_liked(*case)))
