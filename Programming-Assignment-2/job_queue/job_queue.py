# python3

import queue


class JobQueue:

    class Task(object):
        def __init__(self, id):
            self.id = id
            self.next_free_time = 0

        def __lt__(self, other):
            # return self.next_free_time < other.next_free_time
            if self.next_free_time == other.next_free_time:
                return self.id < other.id
            return self.next_free_time < other.next_free_time

        def __gt__(self, other):
            if self.next_free_time == other.next_free_time:
                return self.id > other.id
            return self.next_free_time > other.next_free_time

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    def assign_jobs_better(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        q = queue.PriorityQueue()
        for i in range(self.num_workers):
            q.put(self.Task(i))
        for i in range(len(self.jobs)):
            thread = q.get()
            self.assigned_workers[i] = thread.id
            self.start_times[i] = thread.next_free_time
            thread.next_free_time = thread.next_free_time + self.jobs[i]
            q.put(thread)

    def solve(self):
        self.read_data()
        self.assign_jobs_better()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
