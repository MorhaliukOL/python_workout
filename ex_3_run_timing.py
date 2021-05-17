from utils import convert_input

def run_timing():
    """
    Ask uset how long it took to run 10 km
    and print average time
    """

    total_time = 0
    num_runs = 0
    msg = 'Enter 10 km run time (min): '

    while one_run_time := convert_input(input(msg), 'float', True):
        total_time += one_run_time
        num_runs += 1
    
    if num_runs == 0:
        print("Don't be lazy, go for a run!)")
        return

    avg_time = total_time / num_runs

    print(f'Average of {avg_time:.2f} minutes, over {num_runs} runs')




if __name__ == '__main__':
    run_timing()
