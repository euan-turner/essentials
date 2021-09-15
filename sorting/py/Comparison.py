from Bubble import bubble_sort
from Insertion import insertion_sort
from Merge import recursive_merge
from Quicksort  import quicksort

from time import perf_counter_ns
from numpy.random import randint
from tkinter import *
from prettytable import PrettyTable
import click

##Create an array of a given size, with random integers
def create_array(size : int) -> list:
    arr = randint(0, size, size)
    return list(arr)

##Time a sorting algorithm on an array
def time_sort(arr : list, sort_alg, table : PrettyTable)-> float:
    unsorted = arr.copy()
    t_start = perf_counter_ns()
    sorted_arr = sort_alg(unsorted)
    t_end = perf_counter_ns()
    t_elapsed = t_end - t_start
    
    t = format_time(t_elapsed)

    table.add_row([sort_alg.__qualname__, len(arr), t])
    ##print(f'\nMethod: {sort_alg.__qualname__}\nArray size: {len(arr)}\nElapsed time: {t}\n')
    return t_elapsed

##Format a time with units
def format_time(t_elapsed : float):
    if t_elapsed > 1000000000:
        t = str(t_elapsed/1000000000) + 's'
    elif t_elapsed > 1000000:
        t = str(t_elapsed/1000000) + 'ms'
    elif t_elapsed > 1000:
        t = str(t_elapsed/1000) + 'μs'
    else:
        t = str(t) + 'ns'
    return t
##Testing create_array
# arr1 = create_array(10)
# arr2 = create_array(100)
# arr3 = create_array(1000)

# print(arr1, len(arr1))
# print(arr2, len(arr2))
# print(arr3, len(arr3))


##algs = [bubble_sort, insertion_sort, recursive_merge, quicksort]
algs = {
    '1' : bubble_sort,
    '2' : insertion_sort,
    '3' : recursive_merge,
    '4' : quicksort,
}
sizes = [10,100,1000,10000]

##Standard benchmark
def benchmark_all():
    table = PrettyTable(["Method", "Size", "Time"])
    for size in sizes:
        arr = create_array(size)
        for alg in algs.values():
            time_sort(arr, alg, table)
    print(table)



##GUI
class GUI():

    def __init__(self):
        ##Initial set-up
        self.root = Tk()
        self.root.geometry("300x300")
        self.root.title("Sorting Algorithms")
        self.root.configure(background = "Light Grey")

        ##Frames
        title_frame = Frame(self.root)
        title_frame.grid(row = 0, column = 0, padx = 5, pady = 5)
        entry_frame = Frame(self.root)
        entry_frame.grid(row = 1, column = 0, padx = 5, pady = 5)
        button_frame = Frame(self.root)
        button_frame.grid(row = 2, column = 0, padx = 5, pady = 5)

        ##Title
        Label(title_frame, text = "Sorting Algorithms", font=("Arial",20)).pack(expand = True)

        ##Entries
        alg_text = "Algorithm:"
        Label(entry_frame, text = alg_text, font=("Arial",15)).grid(row=0, column=0)
        self.alg_box = Listbox(entry_frame)
        self.alg_box.insert(1,"Bubble")
        self.alg_box.insert(2,"Insertion")
        self.alg_box.insert(3,"Merge")
        self.alg_box.insert(4,"Quick")
        self.alg_box.grid(row=1,column=0)
        self.arr_entry = Entry(entry_frame, width=10, bg = "white")
        self.arr_entry.grid(row=1,column=1)
        Label(entry_frame, text = "Size of Array:", font=("Arial",15)).grid(row=0,column=1)

        ##Buttons
        benchmark = Button(button_frame, text = "Benchmark", width = 8, command = self.benchmark)\
            .grid(row=0,column=0)
        average = Button(button_frame, text = "Average", width = 8, command = self.average)\
            .grid(row=0,column=1)
        single = Button(button_frame, text = "Single", width = 8, command = self.single)\
            .grid(row=0,column=2)
        self.root.mainloop()
    
    def benchmark(self):
        benchmark_all()
    
    def average(self):
        alg = str(self.alg_box.curselection()[0]+1)
        alg = algs[alg]

        size = int(self.arr_entry.get())
        table = PrettyTable(["Method", "Size", "Time"])
        total = 0
        for _ in range(10):
            arr = create_array(size)
            time = time_sort(arr,alg,table)
            total += time
        print(table)

        avg_table = PrettyTable(["Method", "Size", "Average Time"])

        average = total / 10
        avg_table.add_row([alg.__qualname__, len(arr), format_time(average)])
        print(avg_table)
        ##rint(f'\nMethod: {alg.__qualname__}\nArray size: {len(arr)}\nAverage time: {format_time(average)}\n')

    def single(self):
        alg = str(self.alg_box.curselection()[0]+1)
        alg = algs[alg]

        size = int(self.arr_entry.get())

        table = PrettyTable(["Method", "Size", "Time"])
        arr = create_array(size)
        time_sort(arr,alg, table)
        print(table)


##Main  method for use in command line interface

##Options
##GUI - Access same options through a GUI
##Benchmark - Run standard benchmark
##Alg - Specify alg for averagel, or single test (1 - Bubble, 2 - Insertion, 3 - Merge, 4 - Quick)
##Size - Specify size for average, or single test
##Average - Average of 10 tests, if not given, tests once
##Select algorithm
@click.command()
@click.option("--gui/--no-gui", default = False, help = "Run GUI")
@click.option("--benchmark/--no-benchmark", default = False, help = "Run standard benchmark")
@click.option("--alg", type = str, help = "Sort algorithm to use - 1 Bubble, 2 Insertion, 3 Merge, 4 Quick")
@click.option("--size", default = 100, help = "Size of array to use, defaults to 100")
@click.option("--avg/--no-avg", default = False, help = "Average test over 10 cases")
def main(gui : bool, benchmark : bool, alg : bool, size : bool, avg : bool):
    if gui:
        GUI()
    elif benchmark:
        benchmark_all()
    else:
        if alg not in {'1','2','3','4'}:
            print("Alg option must be 1-4")
            quit()
        if size < 1:
            print("Size must be greater than 1")
            quit()
        alg = algs[alg]
        
        if avg:
            table = PrettyTable(["Method", "Size", "Time"])
            total = 0
            for _ in range(10):
                arr = create_array(size)
                time = time_sort(arr,alg,table)
                total += time
                
            print(table)
            average = total / 10

            avg_table = PrettyTable(["Method", "Size", "Average Time"])
            avg_table.add_row([alg.__qualname__, len(arr), format_time(average)])
            print(avg_table)

        else:
            table = PrettyTable(["Method", "Size", "Time"])
            arr = create_array(size)
            time_sort(arr,alg, table)
            print(table)






if __name__ == "__main__":
    main()