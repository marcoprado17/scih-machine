import subprocess
import threading
import datetime

SAMPLE_INTERVAL = 0.2

sample = 0
lock = threading.Lock()

def take_sample():
    global sample
    global lock

    threading.Timer(SAMPLE_INTERVAL, take_sample).start()
    sample_as_string = subprocess.check_output(["sudo", "docker", "stats", "-a", "--no-stream"])
    lines = sample_as_string.split('\n')

    this_sample = sample
    sample += 1

    for line in lines[1:-1]:
        # print(line)

        elements = line.split()
        container_id = elements[0]
        container_name = elements[1]
        cpu_percentage = elements[2]
        memory_consumption = elements[3]
        memory_available = elements[5]
        memory_percentage = elements[6]

        original_list = [this_sample, datetime.datetime.now().strftime('%s'), container_id, container_name, cpu_percentage, memory_consumption, memory_available, memory_percentage]
        stringfied_list = [str(x) for x in original_list]

        lock.acquire()
        print(','.join(stringfied_list))
        lock.release()

        #   print(elements)
        #   print(len(elements))


def main():
    take_sample()
    # print(subprocess.check_output(["sudo", "docker", "stats", "-a", "--no-stream"]))

if __name__ == "__main__":
    main()
