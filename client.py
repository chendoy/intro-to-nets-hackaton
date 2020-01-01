import socket, ranger, math, encoder_decoder, message, itertools as it

# client configuration #

SERVER_NAME = "127.0.0.1"
SERVER_PORT = 3200
TEAM_NAME = 'UDP MONSTERS'
OFFER_TIMEOUT = 1000  # milliseconds
NUM_OF_LETTERS = 26
WORKERS = []

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
enc_dec = encoder_decoder.Encoder_decoder()

def main():
    hashed_string = input('Welcome to ' + TEAM_NAME + '.' + ' Please enter the hash:\n')
    str_length = input('Please enter the input string length:\n')
    str_length = int(str_length)
    send_discover()
    wait_for_offers()
    jobs = create_jobs(str_length, len(WORKERS))
    send_requests(WORKERS, jobs, hashed_string)
    ans = wait_for_ack()
    print(ans)


def send_requests(workers, jobs, hashed_string):
    i = 0
    for worker in workers:
        send_request(worker, jobs[i], hashed_string)
        i = i + 1


def send_request(worker, job, hashed_string):
    length = str(len(job[0]))
    req_msg = message.Message(TEAM_NAME, message.REQUEST, hashed_string, length, job[0], job[1])
    encoded_msg = enc_dec.encode(req_msg)
    client_sock.sendto(encoded_msg, (worker[0], SERVER_PORT))


def send_discover():
    discover_msg = message.Message(TEAM_NAME, message.DISCOVER, None, None, None, None)
    encoded = enc_dec.encode(discover_msg)
    client_sock.sendto(encoded, (SERVER_NAME, SERVER_PORT))


def wait_for_offers():
    client_sock.settimeout(OFFER_TIMEOUT)
    try:
        (message, server_address) = client_sock.recvfrom(2048)
        WORKERS.append(server_address)
    except socket.timeout:
        return


def split_to_chunks(lst, each):
    return list(it.zip_longest(*[iter(lst)] * each))


def divide(length, num_servers):
    start = 'a' * length
    end = 'z' * length
    search_space = ranger.Ranger(start,end)
    num_strings = NUM_OF_LETTERS ** length
    strings = search_space.generate_all_from_to_of_len()
    each = math.ceil(num_strings / num_servers)
    chunks = split_to_chunks(strings,each)
    return chunks


def create_jobs(length, num_servers):
    jobs = []
    chunks = divide(length, num_servers)
    for chunk in chunks:
        jobs.append((chunk[0], chunk[-1]))
    return jobs


def wait_for_ack():
    while 1:
        (msg, server_address) = client_sock.recvfrom(2048)
        decoded_msg = enc_dec.decode(msg)
        if decoded_msg.type == message.ACK:
            return decoded_msg.start


if __name__ == "__main__":
    main()
