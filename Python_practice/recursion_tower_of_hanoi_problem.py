
def tower_of_hanoi(disk,source_rod, middle_rod, destination_rod):
    print(f'    function entry - tower_of_hanoi({disk},{source_rod}, {middle_rod}, {destination_rod})')
    if disk == 0: # last disk 
        print(f'move {disk} from {source_rod} rod to {destination_rod}')
        return
    print(f'        fn call tower_of_hanoi({disk-1}, {source_rod}, {destination_rod}, {middle_rod})')
    tower_of_hanoi(disk-1, source_rod, destination_rod, middle_rod)

    print(f'move {disk} from {source_rod} rod to {destination_rod} rod')

    print(f'        fn call tower_of_hanoi({disk-1}, {middle_rod},{source_rod},{destination_rod})')
    tower_of_hanoi(disk-1, middle_rod,source_rod,destination_rod)

if __name__ == '__main__':
    no_of_disks=3
    #no_of_disks-1 index based access
    tower_of_hanoi(no_of_disks-1,source_rod='A', middle_rod='B', destination_rod='C')

