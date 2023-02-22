import threading, socket, json, requests, time
from concurrent.futures import ThreadPoolExecutor


start = time.perf_counter()
# task_1
# class Counter(threading.Thread):
#     counter = 0
#     rounds = 100000
#
#     def run(self):
#         for i in range(self.rounds):
#             self.counter += 1
#
#
# threads = []
# for n in range(2):
#     thread = Counter()
#     thread.run()
#     threads.append(thread)
# for thread in threads:
#     thread.start()
#     thread.join()
#
# print(threads[0].counter)

# task_2

# HOST = 'localhost'
# PORT = 65432
# ADDR = (HOST, PORT)
#
#
# def handle_client(conn, addr):
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)
#
#
# if __name__ == '__main__':
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind(ADDR)
#         s.listen()
#         while True:
#             conn, addr = s.accept()
#             thread = threading.Thread(target=handle_client, args=(conn, addr))
#             thread.start()
# task_3 Не певен чи правильно я зрозумів третє завдання, але мені чомусь здається що там малося на увазі щось інше

payload = {'subreddit': 'Python'}
url = "https://api.pushshift.io/reddit/comment/search/"


def get_comments(url, payload):
    r = requests.get(url, params=payload)
    comments = []
    time = []
    for data in range(len(r.json()["data"])):
        comment = r.json()["data"][data]["body"]
        date = r.json()["data"][data]["utc_datetime_str"]
        comments.append(comment)
        time.append(date)

    my_dict = {keys: values for (keys, values) in zip(time, comments)}
    sorted_dict = {keys: values for keys, values in sorted(my_dict.items())}

    with open("comments.json", "w") as com:
        json.dump(sorted_dict, com, indent=2)


with ThreadPoolExecutor() as executor:
    executor.submit(get_comments, url, payload)

finish = time.perf_counter()
print(str(finish-start))